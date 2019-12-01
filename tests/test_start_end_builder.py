import unittest

from start_end_builder import ChunkPhraseBuilder
from tests import load_fixture, load__document


class TestChunkPhraseBuilder(unittest.TestCase):
    def test_compile_chunk_phrase(self):
        builder = ChunkPhraseBuilder()
        transcription = load_fixture('kaldi_small_doc')
        markedup_taj_file = load__document('markedup.taj')
        expected = [
            {'name': 'chunk1', 'start': 0.0, 'end': 1.64},
            {'name': 'chunk2', 'start': 1.9, 'end': 21.7}
        ]
        actual = builder.compile_chunk_phrases(transcription, markedup_taj_file)
        self.assertEqual(actual, expected)
