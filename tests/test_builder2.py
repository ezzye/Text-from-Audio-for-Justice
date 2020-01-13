import glob
import os
import unittest

from chunk_speaker import ChunkSpeaker
from converter import Converter
from transcriber import Transcriber
from utils import load_fixture_rel, load_document_rel


class MyTestCase(unittest.TestCase):
    def test_transcribe_new(self):
        transcriber = Transcriber()
        audio_input_folder = 'input1'
        output_folder = 'output1'
        transcriber.transcribe(audio_input_folder, output_folder)
        expected_transcription = load_fixture_rel(f'fixture2/{output_folder}/transcription.json')
        expected_text = load_document_rel(f'fixture2/{output_folder}/text')
        expected_segments = load_document_rel(f'fixture2/{output_folder}/segments')
        expected_wav_spc = load_document_rel(f'fixture2/{output_folder}/wav.scp')
        transcription = load_fixture_rel(f'{output_folder}/results/20191130-2034_Test1/transcription.json')
        text = load_document_rel(f'{output_folder}/20191130-2034_Test1/text')
        segments = load_document_rel(f'{output_folder}/20191130-2034_Test1/segments')
        wav_scp = load_document_rel(f'{output_folder}/20191130-2034_Test1/wav.scp')
        self.validate_file(text, expected_text)
        self.validate_file(segments, expected_segments)
        self.validate_file(wav_scp, expected_wav_spc)
        self.validate_json(transcription, expected_transcription)

    def validate_file(self, text, expected_text):
        for index, text_line in enumerate(text.splitlines()):
            self.assertEqual(text_line, expected_text.splitlines()[index])

    def validate_json(self, json_items, expected_json_items):
        for index, item in enumerate(json_items['words']):
            self.assertEqual(item, expected_json_items['words'][index])

    def test_chunk_speaker(self):
        chunker = ChunkSpeaker()
        audio_input_path = 'input1/20191130-2034_Test1.wav'
        output_folder = 'output_spk1'
        speech_segmentation_path = 'output1/results/20191130-2034_Test1/segmentation.json'
        chunker.chunk(audio_input_path, speech_segmentation_path, output_folder)
        expected_files = glob.glob(f'{output_folder}/20191130-2034_Test1/20191130-2034_Test1*.wav')
        self.assertEqual(len(expected_files), 4)

    def test_transcribe_new_more_than_one_audio_file(self):
        print(f'running______________......................................')
        transcriber = Transcriber()
        audio_input_folder = 'input3'
        output_folder = 'output3'
        transcriber.transcribe(audio_input_folder, output_folder)
        self.assertEqual(1, 1)

    def test_convert_to_word_document(self):
        converter = Converter()
        type = 'word'
        online_folder = 'https://testconvert2.s3-eu-west-1.amazonaws.com'
        chunks_text_path = 'output1/20191130-2034_Test1'
        output_folder = 'output1/files'

        expected_output_path = 'output1/files/20191130-2034_Test1.doc'
        converter.convert(type, online_folder, chunks_text_path, output_folder)
        self.assertTrue(os.path.exists(expected_output_path))


if __name__ == '__main__':
    unittest.main()
