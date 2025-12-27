import datetime
import os
from argparse import Namespace

import pytest

from Expense import Expense
from FileHandler import FileHandler, updateExpenseInDataFile

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



def test_add_expense_white_box(printAndDelete):
    """Users can add an expense with a description and amount."""

    amount = 40.00
    description = "McLanche Feliz"

    expense = Expense.add(amount, description, handler=fileHandler)

    expenseDataFromJsonFile = fileHandler.getById(expense.getId())
    assert expense.getId() == expenseDataFromJsonFile["id"]
    assert expense.getAmount() == expenseDataFromJsonFile["amount"]
    assert expense.getDescription() == expenseDataFromJsonFile["description"]
    assert expense.getCreationDate().isoformat() == expenseDataFromJsonFile["creationDate"]



def test_update_expense_white_box():
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


def test_delete_expense():
    """Users can delete an expense."""
    assert False

def test_view_all_expenses():
    """Users can view all expenses."""
    assert False

def test_summarize_all_expenses():
    """Users can view a summary of all expenses."""
    assert False

def test_summarize_expenses_for_specific_month():
    """Users can view a summary of expenses for a specific month (of current year)."""
    assert False