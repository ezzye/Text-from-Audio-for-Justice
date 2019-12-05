import unittest

from builder import ChunkBuilder
from exceptions import InputError
from start_end_builder import ChunkPhraseBuilder
from utils import load_document, load_fixture


class TestChunkBuilder(unittest.TestCase):

    def test_compile_timecodes(self):
        builder = ChunkBuilder()
        chunk_phrases = [
            {'name': 'chunk1', 'start': 0.0, 'end': 5.21},
            {'name': 'chunk2', 'start': 5.21, 'end': 10.29},
            {'name': 'chunk3', 'start': 10.29, 'end': 40.20}
        ]
        actual = builder.compile_ffmpeg_cli(chunk_phrases)
        expected = (['0.0 -to 5.21 -c copy chunk1.mp3',
                     '5.21 -to 10.29 -c copy chunk2.mp3',
                     '10.29 -c copy chunk3.mp3'])
        self.assertEqual(actual, expected)

    def test_compile_timecodes_single(self):
        builder = ChunkBuilder()
        chunk_phrases = [
            {'name': 'chunk1', 'start': 3.0, 'end': 5.21}
        ]
        actual = builder.compile_ffmpeg_cli(chunk_phrases)
        expected = (['3.0 -c copy chunk1.mp3'])
        self.assertEqual(actual, expected)

    def test_builder_for_mp3_file(self):
        phrase_builder = ChunkPhraseBuilder()
        chunk_build = ChunkBuilder()
        audio_source_wav = 'fixtures/20191130-2034_Test1.wav'
        audio_source = chunk_build.convert_wav_to_mp3(audio_source_wav)
        print(f'audio_source: {audio_source}')
        markedup_taj_file = load_document('test2.taj')
        print(f'markedup_taj_file: {markedup_taj_file}')
        transcription = load_fixture('transcription.json')
        chunk_phrase = phrase_builder.compile_chunk_phrases(transcription, markedup_taj_file)
        print(f'chunk_phrase: {chunk_phrase}')
        time_code_and_outputs = chunk_build.compile_ffmpeg_cli(chunk_phrase)
        print(f'time_code_and_outputs: {time_code_and_outputs}')
        chunk_build.build(audio_source, time_code_and_outputs)

    def test_compile_timecodes_empty(self):
        builder = ChunkBuilder()
        chunk_phrases = []
        with self.assertRaises(InputError) as context:
            builder.compile_ffmpeg_cli(chunk_phrases)
            self.assertEqual('Something is wrong - chunk phrase list empty!',context.exception)

    # Example ffmpeg commands
    # ffmpeg -i 20191130-2034_Test1.wav -vn -ar 44100 -ac 2 -b:a 192k test1.mp3
    # ffmpeg -i test1.mp3 -ss 0.0 -to 5.21 -c copy chunk1.mp3
