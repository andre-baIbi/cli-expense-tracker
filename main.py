from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument("args", nargs="*")

args = parser.parse_args().args

if __name__ == '__main__':
    ...