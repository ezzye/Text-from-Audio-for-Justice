import argparse


def parse_args():
    parser = argparse.ArgumentParser('taj')
    parser.add_argument('mode',
                        type=str,
                        choices=('transcribe', 'chunk', 'make_markup'),
                        help='the mode of operation: \n\t{\'transcribe\', \'chunk\', \'make_markup\'}')
    parser.add_argument(
        '--audio_source',
        '-s',
        type=str,
        help='path to the audio file to chunk. Must have  either mp3 or wav extension',
        default='input/audio.wav')
    parser.add_argument(
        '--transcript',
        '-t',
        type=str,
        help='path of Kaldi json transcript file',
        default='input/transcription.json')
    parser.add_argument(
        '--markup_file',
        '-m',
        type=str,
        help='output path of taj markup file',
        default='input/markup_file.taj')
    parser.add_argument(
        '--split_sentences',
        '-n',
        type=str,
        help='output path of taj markup file',
        default='')
    parser.add_argument(
        '--audio_output',
        '-o',
        type=str,
        help='output path for chunk files',
        default='output/chunk')
    parser.add_argument(
        '--doc_output',
        '-d',
        type=str,
        help='output path for MS Word file',
        default='output/output.doc')
    parser.add_argument(
        '--validate',
        '-v',
        action='store_true',
        help='validate created transcript before building audio chunks',
        default=False)
    return parser.parse_args()


