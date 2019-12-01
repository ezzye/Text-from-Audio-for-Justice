import subprocess

from exceptions import InputError


class ChunkBuilder(object):
    def build(self, audio_source, time_code_and_outputs):
        for time_code_and_output in time_code_and_outputs:
            self.build_step(audio_source, time_code_and_output)

    def build_step(self, audio_source, time_code_and_output):
        options = [
            'ffmpeg',
            '-i', audio_source,
            '-ss',
            time_code_and_output
        ]
        subprocess.call(options)

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
