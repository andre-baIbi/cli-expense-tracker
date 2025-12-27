from argparse import ArgumentParser, Namespace

from Expense import Expense, Category
from FileHandler import FileHandler, updateExpenseInDataFile

parser = ArgumentParser()

parser.add_argument("command", choices=["add", "list", "summary", "delete", "update"])
parser.add_argument("--description", type=str)
parser.add_argument("--amount", help="Must be a float or float castable string",type=float)
parser.add_argument("--id", type=int, help="Expense id on datafile")
parser.add_argument("--category", choices=[category.value for category in Category])

args = parser.parse_args()
command = args.command
fileHandler = FileHandler(env="prd")





if __name__ == '__main__':
    if command == "add":
        if args.amount:
            Expense.add(args.amount, args.description, handler=fileHandler)
        else:
            print("There must be an amount set!")

    elif command == "update":
        if args.id:
            updateExpenseInDataFile(args, fileHandler)

        else:
            print("Error: Insert expense ID.")

    else:
        print(f"There is no command named {command}, type -help for more information.")