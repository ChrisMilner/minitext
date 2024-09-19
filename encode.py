from argparse import ArgumentParser

from minitext import encode


if __name__ == "__main__":
    parser = ArgumentParser(prog="MiniText Encode")
    parser.add_argument("text")
    parser.add_argument("filename")

    args = parser.parse_args()

    with open(args.filename, 'wb') as f:
        f.write(encode(args.text))
