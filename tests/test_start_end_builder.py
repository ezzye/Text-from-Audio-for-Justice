import os
import unittest
from builtins import print

from start_end_builder import ChunkPhraseBuilder
from utils import load_fixture, load_document


class TestChunkPhraseBuilder(unittest.TestCase):
    def test_make_markedup(self):
        builder = ChunkPhraseBuilder()
        transcription = load_fixture('kaldi_small_doc.json')
        expected = "Oh.| And A A over"
        actual = builder.make_markup_file(transcription["punct"])
        self.assertEqual(actual, expected)

    def test_compile_chunk_phrase(self):
        builder = ChunkPhraseBuilder()
        transcription = load_fixture('kaldi_small_doc.json')
        markedup_taj_file = builder.make_markup_file(transcription["punct"])
        expected = [
            {'name': 'chunk1', 'start': 0.0, 'end': 1.13},
            {'name': 'chunk2', 'start': 1.13, 'end': 21.7}
        ]
        actual = builder.compile_chunk_phrases(transcription, markedup_taj_file)
        self.assertEqual(actual, expected)

    def test_compile_chunk_phrase_bigger_file(self):
        builder = ChunkPhraseBuilder()
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

    def test_test_filename_created(self):
        builder = ChunkPhraseBuilder()
        transcription = load_fixture('transcription.json')
        filename = builder.extract_markup_file(transcription)
        path = f'fixtures/{filename}.taj'
        self.assertTrue(os.path.exists(path))
        if os.path.exists(path):
            os.remove(path)
        else:
            print("File does not exist")
