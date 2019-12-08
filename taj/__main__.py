from builder import ChunkBuilder
from exceptions import InputError
from taj.argparser import parse_args


def main():
    args = parse_args()
    builder = ChunkBuilder()
    try:
        pass
    except InputError as e:
        print(f'{InputError.__name__}:\n\t{e}')


if __name__ == '__main__':
    main()
