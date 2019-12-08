import shlex
import subprocess
import re

from exceptions import InputError
from taj import load_file, load_json


class ChunkBuilder(object):
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
        return list_of_output_files

    def compile_ffmpeg_cli(self, chunk_phrases, audiofile):
        ffmpeg_cli = []
        if len(chunk_phrases) == 0:
            raise InputError('Something is wrong - chunk phrase list empty!')

        for chunk_phrase in chunk_phrases:
            ffmpeg_cli.append(f'ffmpeg -i {audiofile} -ss {chunk_phrase["start"]} -to {chunk_phrase["end"]} -c copy {chunk_phrase["name"]}.mp3')

        ffmpeg_cli[-1] = f'ffmpeg -i {audiofile} -ss {chunk_phrases[-1]["start"]} -c copy {chunk_phrases[-1]["name"]}.mp3'
        return ffmpeg_cli

    def compile_chunk_phrases(self, transcription, markedup_taj_file, audio_output_path):
        chunk_list = markedup_taj_file.split('|')
        chunk_word_list = []
        words = transcription['words']
        word_count_end = 0
        chunk_phrases = []
        for chunk in chunk_list:
            chunk_words = chunk.split()
            chunk_word_list.append(chunk_words)
        for index, chunk_word in enumerate(chunk_word_list):
            word_count_start = word_count_end
            word_count_end = word_count_start + len(chunk_word)
            start = words[word_count_start]['start']
            end = words[word_count_end-1]['end']
            chunk_phrases.append({'name': f'{audio_output_path}{index + 1}', 'start': start, 'end': end})
        return chunk_phrases

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

    # ffmpeg -i 20191130-2034_Test1.wav -vn -ar 44100 -ac 2 -b:a 192k test1.mp3
    # ffmpeg -i fixtures/20191130-2034_Test1.wav -ss 0.1 -to 6.26 -c copy chunk1.mp3


