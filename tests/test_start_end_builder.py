import os
import unittest

from start_end_builder import ChunkPhraseBuilder
from utils import load_fixture, load__document


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

