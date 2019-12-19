from builder import ChunkBuilder
from exceptions import InputError
from argparser import parse_args


def main():
    args = parse_args()
    builder = ChunkBuilder()
    try:
        builder.compose(args.mode, args.transcript, args.audio_source,
                        args.markup_file, args.split_sentences, args.audio_output,
                        args.doc_output, args.validate, args.audio_output_chunks,
                        args.word_output_file, args.online_folder, args.doc_output)
    except InputError as e:
        print(f'{InputError.__name__}:\n\t{e}')


if __name__ == '__main__':
    main()
