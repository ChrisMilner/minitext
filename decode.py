from argparse import ArgumentParser

from minitext import decode


if __name__ == "__main__":
    parser = ArgumentParser(prog="MiniText Encode")
    parser.add_argument("filename")

    args = parser.parse_args()

    with open(args.filename, 'rb') as f:
        print(decode(f.read()))
