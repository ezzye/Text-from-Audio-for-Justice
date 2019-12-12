import shlex
import subprocess
import re
import json
import os

from exceptions import InputError


class ChunkBuilder(object):
    def compose(self, mode, transcript, audio_source, markup_file, split_sentences, audio_output, doc_output, validate):
        if mode == 'make_markup':
            self.make_markup(transcript, markup_file, split_sentences)
        if mode == 'chunk':
            self.chunk(audio_source, transcript, markup_file, audio_output)
        if mode == 'transcribe':
            pass

    def build(self, ffmpeg_cli):
        for ffmpeg_cli_item in ffmpeg_cli:
            options = shlex.split(ffmpeg_cli_item)
            subprocess.call(options)

    def make_markup(self, transcription_path, path_man, path_auto):
        transcript = load_json(transcription_path)
        if path_auto == '':
            path = self.extract_markup_file(transcript, path_man)
        else:
            path = self.make_markup_file(transcript, path_auto)
        return path

    def chunk(self,audio_path, transcript_path, markup_path, audio_output_path):
        transcript = load_json(transcript_path)
        markup_file = load_file(markup_path)
        chunk_phrases = self.compile_chunk_phrases(transcript, markup_file, audio_output_path)
        ffmpeg_cli_list = self.compile_ffmpeg_cli(chunk_phrases, audio_path)
        list_of_output_files = []
        for chunk_phrase in chunk_phrases:
            list_of_output_files.append(f'{chunk_phrase["name"]}.mp3')
        self.build(ffmpeg_cli_list)
        print(f'list_of_output_files: {list_of_output_files}')
        return list_of_output_files

    def compile_ffmpeg_cli(self, chunk_phrases, audiofile):
        ffmpeg_cli = []
        if len(chunk_phrases) == 0:
            raise InputError('Something is wrong - chunk phrase list empty!')
        if audiofile.split(".")[-1] == 'wav':
            audiofile = self.convert_wav_to_mp3(audiofile)
        if audiofile.split(".")[-1] != 'mp3':
            raise Exception("OMG! The input audio file needs to be in wav or mp3 format.")

        for chunk_phrase in chunk_phrases:
            ffmpeg_cli.append(f'ffmpeg -i {audiofile} -ss {chunk_phrase["start"]} -to {chunk_phrase["end"]} -c copy -y {chunk_phrase["name"]}.mp3')

        ffmpeg_cli[-1] = f'ffmpeg -i {audiofile} -ss {chunk_phrases[-1]["start"]} -c copy -y {chunk_phrases[-1]["name"]}.mp3'
        print(f'ffmpeg_cli: {ffmpeg_cli}')
        return ffmpeg_cli

    def compile_chunk_phrases(self, transcription, markedup_taj_file, audio_output_path):
        chunk_list = markedup_taj_file.split('|')
        print(f'size of chunk list: {len(chunk_list)}')
        for index, chunk in enumerate(chunk_list):
            print(f'chunk {index} is {chunk}')
        chunk_word_list = []
        words = transcription['words']
        word_count_end = 0
        chunk_phrases = []
        for chunk in chunk_list:
            chunk_words = chunk.split()
            print(f'size of chunk: {len(chunk_words)} words')
            if len(chunk_words) > 0:
                chunk_word_list.append(chunk_words)
        for index, chunk_word in enumerate(chunk_word_list):
            word_count_start = word_count_end
            word_count_end = word_count_start + len(chunk_word)
            start = words[word_count_start]['start']
            end = words[word_count_end-1]['end']
            chunk_phrases.append({'name': f'{audio_output_path}{index + 1}', 'start': start, 'end': end})
        print(f'chunk_phrases: {chunk_phrases}')
        return chunk_phrases

    def transcribe_audio(self, audio_source, doc_output):
        current_working_dir = os.getcwd()
        audio_file_name = audio_source.split("/")[-1].split(".")[0]
        print(f'before conversion: {audio_source}')
        if audio_source.split('.')[-1] == 'wav':
            audio_source = self.convert_wav_to_mp3(audio_source)
        print(f'after conversion: {audio_source}')
        if audio_source.split('.')[-1] != 'mp3':
            raise Exception("OMG! The input audio file needs to be in wav or mp3 format.")
        instruction = f'docker run --rm  -v "{current_working_dir}:/tmp/media" --name bbc-kaldi-container  artifactory-noforge.virt.ch.bbc.co.uk:8443/bbc-kaldi:0.0.11 bbc-kaldi /tmp/media/{audio_source} /tmp/media/{doc_output}'
        options = shlex.split(instruction)
        subprocess.call(options)
        return f'{doc_output}/results/{audio_file_name}/transcription.json'

    # docker run --rm  -v "/Users/MyLaptop/Media:/tmp/media" \
    #     --name bbc-kaldi-container  artifactory-noforge.virt.ch.bbc.co.uk:8443/bbc-kaldi:0.0.11 bbc-kaldi \
    #     /tmp/media/20190111-230000-bbc-news-h264lg.mp4 \
    #     /tmp/media/20190111-230000-bbc-news-h264lg

    def make_markup_file(self, transcription, path):
        punct = transcription["punct"]
        markup = re.sub(r"\.", ".|", punct )
        with open(path, "w", encoding='utf-8') as fp:
            fp.write(markup)
        return path

    def extract_markup_file(self, transcription, path):
        with open(path, "w", encoding='utf-8') as fp:
            fp.write(transcription['punct'])
        return path

    def convert_wav_to_mp3(self, wav_file):
        mp3_file = f'{wav_file.split(".")[0]}.mp3'
        options = [
            'ffmpeg',
            '-y',
            '-i', wav_file,
            '-vn',
            '-ar', '44100',
            '-ac', '2',
            '-b:a',
            '192k',
            mp3_file
        ]
        subprocess.call(options)
        return f'{wav_file.split(".")[0]}.mp3'


def load_json(path):
    with open(path, encoding='utf-8') as fp:
        return json.load(fp)


def load_file(path):
    with open(path, encoding='utf-8') as fp:
        return fp.read()

    # ffmpeg -i 20191130-2034_Test1.wav -vn -ar 44100 -ac 2 -b:a 192k test1.mp3
    # ffmpeg -i fixtures/20191130-2034_Test1.wav -ss 0.1 -to 6.26 -c copy chunk1.mp3


