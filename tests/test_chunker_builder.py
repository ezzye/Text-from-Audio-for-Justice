import unittest

from builder import ChunkBuilder
from exceptions import InputError


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

    def test_compile_timecodes_empty(self):
        builder = ChunkBuilder()
        chunk_phrases = []
        with self.assertRaises(InputError) as context:
            builder.compile_ffmpeg_cli(chunk_phrases)
            self.assertEqual('Something is wrong - chunk phrase list empty!',context.exception)

    # Example ffmpeg commands
    # ffmpeg -i 20191130-2034_Test1.wav -vn -ar 44100 -ac 2 -b:a 192k test1.mp3
    # ffmpeg -i test1.mp3 -ss 0.0 -to 5.21 -c copy chunk1.mp3
