import os
import random
from argparse import Namespace
from subprocess import run, CompletedProcess

import pytest

from Expense import Expense
from FileHandler import FileHandler, updateExpenseInDataFile, deleteById, listAllExpenses

TEST_ENV = "test"
fileHandler: FileHandler = FileHandler.getFileHandler("test")


def printContentsFromFile(test_file):
    with open(test_file, "r") as file:
        contents = file.read()
    print(f"\n{"="*50}\nCONTENTS OF {test_file}:\n{contents}\n\n")

@pytest.fixture(autouse=True)
def printAndDelete():
    test_file = fileHandler.jsonFilename

    yield

    if os.path.exists(test_file):
        printContentsFromFile(test_file)
        os.remove(test_file)
        print(f"Test file {test_file} deleted")


class TestWhiteBox:
    def test_add_expense_white_box(self, printAndDelete):
        """Users can add an expense with a description and amount."""

        amount = 40.00
        description = "McLanche Feliz"

        expense = Expense.add(amount, description, handler=fileHandler)

        expenseDataFromJsonFile = fileHandler.getById(expense.getId())
        assert expense.getId() == expenseDataFromJsonFile["id"]
        assert expense.getAmount() == expenseDataFromJsonFile["amount"]
        assert expense.getDescription() == expenseDataFromJsonFile["description"]
        assert expense.getCreationDate().isoformat() == expenseDataFromJsonFile["creationDate"]

    def test_update_expense_white_box(self):
        """Users can update an expense."""
        _ = Expense.add(20.0, "Lunch", handler=fileHandler)
        _ = Expense.add(50.0, "Groceries", handler=fileHandler)

        expectedAmount = 100.0
        description = "Utilities"
        expenseToTest = Expense.add(expectedAmount, description, handler=fileHandler)
        expectedDate = expenseToTest.getCreationDate()

        testId = expenseToTest.getId()

        newDescription = "Music and Stuff"

        # Simulates user input
        updateNamespace = Namespace()
        updateNamespace.__setattr__("id", testId)
        updateNamespace.__setattr__("description", newDescription)

        updateExpenseInDataFile(updateNamespace, fileHandler)

        expenseDataFromJsonFile = fileHandler.getById(testId)

        assert expectedAmount == expenseDataFromJsonFile["amount"]
        assert newDescription == expenseDataFromJsonFile["description"]
        assert expectedDate.isoformat() == expenseDataFromJsonFile["creationDate"]

    def test_delete_expense(self):
        """Users can delete an expense."""
        #  create expenses
        _ = Expense.add(20.0, "Lunch", handler=fileHandler)
        _ = Expense.add(50.0, "Groceries", handler=fileHandler)
        target = Expense.add(100, "Forgot...", handler=fileHandler)

        #  check all saved expenses
        expensesSize = len(list(fileHandler.parseDataFromJsonFile()))

        #  delete expense
        deleteById(str(target.getId()), fileHandler)

        #  check if expense was removed
        assert len(fileHandler.parseDataFromJsonFile()) == expensesSize - 1


def runTestCommand(commandStr: str) -> CompletedProcess:
    EXPENSE_TRACKER_COMMAND = "py .\\expense-tracker.py "
    TEST_KEYWORD = " --test"

    return run((EXPENSE_TRACKER_COMMAND + commandStr + TEST_KEYWORD).split(" "), capture_output=True)


def getSummaryValueFromSummaryStdout(summarizeCommand):
    return float(
                str(
                    runTestCommand(summarizeCommand).stdout)
                        .split("$")[1]
                        .replace("\\r", "")
                        .replace("\\n", "")[:-1]
            )


class TestBlackBox:
    def test_list_all_expenses(self):
        """Users can view all expenses."""
        # create 10 expenses

        amounts = []

        for _ in range(25):
            amount = str(random.randint(1, 1000))
            amounts.append(amount)
            addCommand = f"add --description Drugstore --amount {amount}"
            runTestCommand(addCommand)

        # show all expenses
        listCommand = "list"
        result = str(runTestCommand(listCommand).stdout)

        assert True == all([str(amount_) in result for amount_ in amounts])

    def test_summarize_all_expenses(self):
        """Users can view a summary of all expenses."""
        amounts = []

        for _ in range(25):
            amount = random.randint(1, 1000)
            amounts.append(amount)
            addCommand = f"add --description expense --amount {str(amount)}"
            runTestCommand(addCommand)

        summarizeCommand = "summary"
        result = getSummaryValueFromSummaryStdout(summarizeCommand)

        assert result == sum(amounts)

    def test_summarize_expenses_for_specific_month(self):
        """Users can view a summary of expenses for a specific month (of current year)."""
        assert False