import argparse


def parse_args():
    parser = argparse.ArgumentParser('taj')
    parser.add_argument('mode',
                        type=str,
                        choices=('batch', 'transcribe', 'chunk', 'make_markup', 'word'),
                        help='the mode of operation: \n\t{\'batch\', \'transcribe\', \'chunk\', \'make_markup\', \'batch\'}')
    parser.add_argument(
        '--audio_source',
        '-s',
        type=str,
        help='path to the audio file to chunk. Must have  either mp3 or wav extension',
        default='audio.wav')
    parser.add_argument(
        '--audio_output_chunks',
        '-c',
        type=str,
        help='path to name of output chunks',
        default='chunk')
    parser.add_argument(
        '--word_output_file',
        '-w',
        type=str,
        help='path of word output file',
        default='document.docx')
    parser.add_argument(
        '--online_folder',
        '-f',
        type=str,
        help='http url of folder of audio_files',
        default='')
    parser.add_argument(
        '--transcription_output',
        '-p',
        type=str,
        help='path of transcription output file',
        default='transcription.json')
    parser.add_argument(
        '--transcript',
        '-t',
        type=str,
        help='path of Kaldi json transcript file',
        default='transcription.json')
    # duplicate argument
    parser.add_argument(
        '--markup_file',
        '-m',
        type=str,
        help='output path of taj markup file',
        default='markup_file.taj')
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
        default='chunk')
    parser.add_argument(
        '--doc_output',
        '-d',
        type=str,
        help='output path for MS Word file',
        default='output.doc')
    parser.add_argument(
        '--validate',
        '-v',
        action='store_true',
        help='validate created transcript before building audio chunks',
        default=False)
    return parser.parse_args()
