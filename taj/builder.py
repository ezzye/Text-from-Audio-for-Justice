import shlex
import subprocess

from exceptions import InputError


class ChunkBuilder(object):
    def build(self, audio_source, time_code_and_outputs):
        for time_code_and_output in time_code_and_outputs:
            self.build_step(audio_source, time_code_and_output)

    def build_step(self, audio_source, time_code_and_output):
        params = shlex.split(time_code_and_output)
        options = [
            'ffmpeg',
            '-i', audio_source,
            '-ss',
            params[0],
            params[1],
            params[2],
            params[3],
            params[4],
            params[5],
        ]
        print(f'Options: {options}')
        subprocess.call(options)

    #     ffmpeg -i fixtures/20191130-2034_Test1.wav -ss 0.1 -to 6.26 -c copy chunk1.mp3

    def compile_ffmpeg_cli(self, chunk_phrases):
        """compile chunk_phrases to ffmpeg chunks"""
        if len(chunk_phrases) == 0:
            raise InputError('Something is wrong - chunk phrase list empty!')
        return self.compile_chunks(chunk_phrases)

    def compile_chunks(self, chunk_phrases):
        chunk_list = []
        for chunk_phrase in chunk_phrases:
            chunk_list.append(f'{chunk_phrase["start"]} -to {chunk_phrase["end"]} -c copy {chunk_phrase["name"]}.mp3')
        chunk_list[-1] = f'{chunk_phrases[-1]["start"]} -c copy {chunk_phrases[-1]["name"]}.mp3'
        return chunk_list

    def convert_wav_to_mp3(self, wav_file):
        mp3_file = f'{wav_file.split(".")[0]}.mp3'
        print(f'mp3 file: {mp3_file}')
        options = [
            'ffmpeg',
            '-i', wav_file,
            '-vn',
            '-ar', '44100',
            '-ac', '2',
            '-b:a',
            '192k',
            mp3_file
        ]
        print(options)
        subprocess.call(options)
        return f'{wav_file.split(".")[0]}.mp3'
# ffmpeg -i 20191130-2034_Test1.wav -vn -ar 44100 -ac 2 -b:a 192k test1.mp3
