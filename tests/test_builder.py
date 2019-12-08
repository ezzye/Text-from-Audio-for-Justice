import os
import unittest
from builder import ChunkBuilder
from exceptions import InputError
from taj import load_file, load_json
from utils import load_document, load_fixture


class TestChunkBuilder(unittest.TestCase):

    def test_compile_ffmpeg_cli(self):
        builder = ChunkBuilder()
        chunk_phrases = [
            {'name': 'chunk1', 'start': 0.0, 'end': 5.21},
            {'name': 'chunk2', 'start': 5.21, 'end': 10.29},
            {'name': 'chunk3', 'start': 10.29, 'end': 40.20}
        ]
        audio_source_wav = 'fixtures/20191130-2034_Test1.wav'
        audio_source = builder.convert_wav_to_mp3(audio_source_wav)
        actual = builder.compile_ffmpeg_cli(chunk_phrases, audio_source)
        expected = (['ffmpeg -i fixtures/20191130-2034_Test1.mp3 -ss 0.0 -to 5.21 -c copy chunk1.mp3',
                     'ffmpeg -i fixtures/20191130-2034_Test1.mp3 -ss 5.21 -to 10.29 -c copy chunk2.mp3',
                     'ffmpeg -i fixtures/20191130-2034_Test1.mp3 -ss 10.29 -c copy chunk3.mp3'])
        if os.path.exists(audio_source):
            os.remove(audio_source)
        else:
            print("File does not exist")
        self.assertEqual(actual, expected)

    def test_compile_ffmpeg_cli_single(self):
        builder = ChunkBuilder()
        chunk_phrases = [
            {'name': 'chunk1', 'start': 3.0, 'end': 5.21}
        ]
        audio_source_wav = 'fixtures/20191130-2034_Test1.wav'
        audio_source = builder.convert_wav_to_mp3(audio_source_wav)
        actual = builder.compile_ffmpeg_cli(chunk_phrases, audio_source)
        expected = (['ffmpeg -i fixtures/20191130-2034_Test1.mp3 -ss 3.0 -c copy chunk1.mp3'])
        if os.path.exists(audio_source):
            os.remove(audio_source)
        else:
            print("File does not exist")
        self.assertEqual(actual, expected)

    def test_builder_for_using_split_markup(self):
        chunk_build = ChunkBuilder()
        audio_source_wav = 'fixtures/20191130-2034_Test1.wav'
        audio_source = chunk_build.convert_wav_to_mp3(audio_source_wav)
        markedup_taj_file = load_document('test2.taj')
        transcription = load_fixture('transcription.json')
        chunk_phrase = chunk_build.compile_chunk_phrases(transcription, markedup_taj_file)
        time_code_and_outputs = chunk_build.compile_ffmpeg_cli(chunk_phrase, audio_source)
        chunk_build.build(time_code_and_outputs)
        test_files = [
            audio_source,
            'chunk1.mp3',
            'chunk2.mp3',
            'chunk3.mp3',
            'chunk4.mp3'
        ]
        for test_file in test_files:
            if os.path.exists(test_file):
                os.remove(test_file)
            else:
                print("File does not exist")

    def test_auto_make_markedup(self):
        builder = ChunkBuilder()
        transcription = load_fixture('kaldi_small_doc.json')
        expected = "Oh.| And A A over"
        path = 'fixtures/auto_markup.taj'
        builder.make_markup_file(transcription, path)
        self.assertTrue(os.path.exists(path))
        actual = load_file(path)
        self.assertEqual(actual, expected)

    def test_extract_markup_from_transcript(self):
        builder = ChunkBuilder()
        transcription = load_fixture('transcription.json')
        path = 'fixtures/extracted_markup.taj'
        path = builder.extract_markup_file(transcription, path)
        self.assertTrue(os.path.exists(path))


    def test_compile_chunk_phrase(self):
        builder = ChunkBuilder()
        transcription = load_fixture('kaldi_small_doc.json')
        markedup_taj_file = builder.make_markup_file(transcription["punct"])
        expected = [
            {'name': 'chunk1', 'start': 0.0, 'end': 1.13},
            {'name': 'chunk2', 'start': 1.13, 'end': 21.7}
        ]
        actual = builder.compile_chunk_phrases(transcription, markedup_taj_file)
        self.assertEqual(actual, expected)

    def test_compile_chunk_phrase_bigger_file(self):
        builder = ChunkBuilder()
        transcription = load_fixture('transcription.json')
        markedup_taj_file = load_document('test2.taj')
        expected = [
            {'name': 'chunk1', 'start': 0.1, 'end': 6.26},
            {'name': 'chunk2', 'start': 6.66, 'end': 11.66},
            {'name': 'chunk3', 'start': 11.76, 'end': 20.79},
            {'name': 'chunk4', 'start': 21.01, 'end': 29.76}
        ]
        actual = builder.compile_chunk_phrases(transcription, markedup_taj_file)
        self.assertEqual(actual, expected)

    def test_compile_ffmpeg_cli_empty(self):
        builder = ChunkBuilder()
        chunk_phrases = []
        audio_source_wav = 'fixtures/20191130-2034_Test1.wav'
        audio_source = builder.convert_wav_to_mp3(audio_source_wav)
        with self.assertRaises(InputError) as context:
            builder.compile_ffmpeg_cli(chunk_phrases, audio_source)
        if os.path.exists(audio_source):
            os.remove(audio_source)
        else:
            print("File does not exist")

    def test_mode_auto_markup_man(self):
        builder = ChunkBuilder()
        path_man = ''
        path_auto = 'fixtures/markup_test.taj'
        builder.make_markup('fixtures/kaldi_small_doc.json', path_man, path_auto)
        expected = "Oh.| And A A over"
        actual = load_file(path_auto)
        self.assertEqual(actual, expected)

    def test_mode_extract_markup_auto(self):
        builder = ChunkBuilder()
        path_man = 'fixtures/markup_test2.taj'
        path_auto = ''
        builder.make_markup('fixtures/kaldi_small_doc.json', path_man, path_auto)
        expected = "Oh. And A A over"
        actual = load_file(path_man)
        self.assertEqual(actual, expected)

    def test_mode_chunk(self):
        builder = ChunkBuilder()
        audio_path = 'fixtures/20191130-2034_Test1.wav'
        transcript_path = 'fixtures/transcription.json'
        markup_path = 'fixtures/test2.taj'
        audio_output_path = 'fixtures/chunk'
        expected_output_files = [
            'fixtures/chunk1.mp3',
            'fixtures/chunk2.mp3',
            'fixtures/chunk3.mp3',
            'fixtures/chunk4.mp3',
        ]
        for existing_file in expected_output_files:
            if os.path.exists(existing_file):
                os.remove(existing_file)
        list_of_output_files = builder.chunk(audio_path, transcript_path, markup_path, audio_output_path)
        self.assertEqual(list_of_output_files, expected_output_files)
        for path in expected_output_files:
            os.path.exists(path)

    # Example ffmpeg commands
    # ffmpeg -i 20191130-2034_Test1.wav -vn -ar 44100 -ac 2 -b:a 192k test1.mp3
    # ffmpeg -i test1.mp3 -ss 0.0 -to 5.21 -c copy chunk1.mp3
