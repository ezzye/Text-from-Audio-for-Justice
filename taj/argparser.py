import argparse


def parse_args():
    parser = argparse.ArgumentParser('taj')
    parser.add_argument(
        'mode',
        type=str,
        choices=('transcribe'),
        help='the mode of operation: \n\t{\'batch\', \'transcribe\', \'chunk\', \'make_markup\', \'batch\'}'
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
    return parser.parse_args()
