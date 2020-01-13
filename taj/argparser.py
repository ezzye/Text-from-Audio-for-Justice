import argparse


def parse_args():
    parser = argparse.ArgumentParser('taj')
    parser.add_argument(
        'mode',
        type=str,
        choices=('transcribe', 'chunk_speaker', 'convert'),
        help='the mode of operation: \n\t{\'transcribe\', \'chunk_speaker\', \'convert\'}'
    )
    parser.add_argument(
        '--input_folder',
        '-i',
        type=str,
        help='path to the audio file folder',
        default='')
    parser.add_argument(
        '--output_folder',
        '-o',
        type=str,
        help='path to output folder',
        default='')
    parser.add_argument(
        '--speech_segmentation_path',
        '-s',
        type=str,
        help='path to segmentation.json file',
        default='')
    parser.add_argument(
        '--audio_input_path',
        '-j',
        type=str,
        help='path to the audio file',
        default='')
    parser.add_argument(
        '--type',
        '-t',
        type=str,
        help='path to the audio file',
        default='')
    parser.add_argument(
        '--online_folder',
        '-f',
        type=str,
        help='path to the audio file',
        default='')
    parser.add_argument(
        '--chunks_text_path',
        '-c',
        type=str,
        help='path to the audio file',
        default='')
    return parser.parse_args()

