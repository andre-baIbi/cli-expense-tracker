from argparse import ArgumentParser

from Expense import Expense
from FileHandler import FileHandler

parser = ArgumentParser()

parser.add_argument("command", help="May be: <add / list / summary / delete>")
parser.add_argument("--description", type=str, default="")
parser.add_argument("--amount", help="Must be a float or float castable string",type=float)

args = parser.parse_args()
command = args.command
fileHandler = FileHandler(env="prd")

if __name__ == '__main__':
    if command == "add":
        if args.amount:
            Expense.add(args.amount, args.description, handler=fileHandler)
        else:
            print("There must be an amount set!")

    else:
        print(f"There is no command named {command}, type -help for more information.")