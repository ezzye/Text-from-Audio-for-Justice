import json
import os

from builder import ChunkBuilder
from transcriber import Transcriber

transcriber = Transcriber()
builder = ChunkBuilder()


class ChunkSpeaker(object):

    def chunk(self, audio_input_path, speech_segmentation_path, output_folder):
        with open(speech_segmentation_path, "r", encoding='utf-8') as fp:
            segmentation = json.load(fp)
        filename = audio_input_path.split("/")[-1].split(".")[0]
        os.makedirs(f'{output_folder}/{filename}')
        for item in segmentation['segments']:
            start_end = (item['start'], round(item['start'] + item['duration'], 2))
            transcriber.chunk_audio_file(audio_input_path, output_folder, start_end)
