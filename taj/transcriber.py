import glob
import json
import os

from builder import ChunkBuilder

builder = ChunkBuilder()


class Transcriber(object):
    def transcribe(self, input_folder, output_folder):
        audio_files = glob.glob(f'{input_folder}/*.wav')
        for index, audio_source in enumerate(audio_files):
            print(f'input_folder: {input_folder}, output_folder: {output_folder}')
            builder.transcribe_audio(audio_source, output_folder)
            self.chunk_file(audio_source, output_folder)
            output_folder = f'{output_folder.split("_")[0]}_{index}'

    def chunk_file(self, audio_source, output):
        filename_in = audio_source.split("/")[-1].split(".")[0]
        json_segments_path = f'{output}/results/{filename_in}/segments'
        output_path = f'{output}/{filename_in}'
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        text_path = f'{output}/{filename_in}/text'
        segments_path = f'{output}/{filename_in}/segments'
        wav_scp_path = f'{output}/{filename_in}/wav.scp'
        text_list, segments_list, wav_scp_list = [], [], []
        segment_files = sorted(glob.glob(f'{json_segments_path}/*.json'))
        for index, item in enumerate(segment_files):
            with open(item, "r", encoding='utf-8') as fp:
                transcription = json.load(fp)
            if len(transcription["words"]) > 0:
                start_end = self.start_and_end(transcription)
                file_output_path = self.chunk_audio_file(audio_source, output, start_end)
                start, end = start_end
                count = index + 1
                utt_ref = f'{filename_in}_S{count:06}MSU_{start}_{end}'
                words = f'{transcription["punct"]}'
                file_ref = f'{filename_in}_{start}_{end}'
                text_list.append(f'{utt_ref} {words}\n')
                segments_list.append(f'{utt_ref} {file_ref} {start} {end}\n')
                wav_scp_list.append(f'{file_ref} {file_output_path}\n')
        self.write_to_file(text_path, ''.join(text_list))
        self.write_to_file(segments_path, ''.join(segments_list))
        self.write_to_file(wav_scp_path, ''.join(wav_scp_list))

    def start_and_end(self, transcription):
        return (
            transcription["words"][0]["start"],
            transcription["words"][-1]["end"]
        )

    def chunk_audio_file(self, audio_source, output, start_end):
        start, end = start_end
        file_name_ext = audio_source.split(".")[-1]
        filename_in = audio_source.split("/")[-1].split(".")[0]
        file_path = f'{output}/{filename_in}/{filename_in}_{start}_{end}.{file_name_ext}'
        ffmpeg_cli = f'ffmpeg -i {audio_source} -ss {start} -to {end} -c copy -y {file_path}'
        builder.build([ffmpeg_cli])
        return file_path

    def write_to_file(self, path, content):
        with open(path, "w", encoding='utf-8') as fp:
            fp.write(''.join(content))
