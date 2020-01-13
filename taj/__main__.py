from chunk_speaker import ChunkSpeaker
from converter import Converter
from exceptions import InputError
from argparser import parse_args
from transcriber import Transcriber


def main():
    args = parse_args()
    transcribe = Transcriber()
    chunker = ChunkSpeaker()
    converter = Converter()
    try:
        if args.mode == 'transcribe':
            transcribe.transcribe(
                args.input_folder,
                args.output_folder
            )
        if args.mode == 'chunk_speaker':
            chunker.chunk(
                args.audio_input_path,
                args.speech_segmentation_path,
                args.output_folder
            )
        if args.mode == 'convert':
            converter.convert(
                args.type,
                args.online_folder,
                args.chunks_text_path,
                args.output_folder
            )

    except InputError as e:
        print(f'{InputError.__name__}:\n\t{e}')


if __name__ == '__main__':
    main()
