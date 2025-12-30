from argparse import ArgumentParser, Namespace

from Expense import Expense, Category
from FileHandler import FileHandler, updateExpenseInDataFile, deleteById, listAllExpenses, summaryOfExpenses

parser = ArgumentParser()

parser.add_argument("command", choices=["add", "list", "summary", "delete", "update"])
parser.add_argument("--description", type=str)
parser.add_argument("--amount", help="Must be a float or float castable string",type=float)
parser.add_argument("--id", type=int, help="Expense id on datafile")
parser.add_argument("--category", choices=[category.value for category in Category], default=Category.UNDEFINED)
parser.add_argument("--test", action="store_true")
parser.add_argument("--month", choices=[_ for _ in range(1, 13)], type=int, help="YTD scope, e.g., if today is 01/08/2025 and you type '9', fetches expenses from September/2024.")
parser.add_argument("--year", type=int)
parser.add_argument("--testCase", type=str, default=None, help="Only for testing purposes, do not use.")

args = parser.parse_args()
command = args.command

env = "test" if args.test else "prd"
fileHandler = FileHandler(env, testCase=args.testCase)


months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}




if __name__ == '__main__':
    if command == "add":
        if args.amount:
            category = Category(args.category) if args.category else Category.UNDEFINED

            Expense.add(args.amount, args.description, category=category, handler=fileHandler)
        else:
            print("There must be an amount set!")

    elif command == "update":
        if args.id:
            updateExpenseInDataFile(args, fileHandler)

        else:
            print("Error: Insert expense ID.")

    elif command == "delete":
        if args.id:
            deleteById(str(args.id), fileHandler)
        else:
            print("Error: Insert expense ID.")

    elif command == "list":
        listAllExpenses(fileHandler, printable=True)

    elif command == "summary":
        print(f"Total Expenses{f" for month {months[args.month]}" if args.month else ""}: ${summaryOfExpenses(fileHandler, 
                                                    filters={
                                                        "category": Category(args.category),
                                                        "month" : args.month,
                                                        "year" : args.year
                                                        }
                                                    )}")

    else:
        print(f"There is no command named {command}, type -help for more information.")