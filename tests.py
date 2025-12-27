import datetime
import os

import pytest

from Expense import Expense
from FileHandler import FileHandler

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



def test_add_expense(printAndDelete):
    """Users can add an expense with a description and amount."""


    # criar expense
    amount = 40.00
    description = "McLanche Feliz"

    expense = Expense.add(amount, description, handler=fileHandler)

    expenseDataFromJsonFile = fileHandler.getById(expense.getId())
    assert expense.getId() == expenseDataFromJsonFile["id"]
    assert expense.getAmount() == expenseDataFromJsonFile["amount"]
    assert expense.getDescription() == expenseDataFromJsonFile["description"]
    assert expense.getCreationDate().isoformat() == expenseDataFromJsonFile["creationDate"]






def test_update_expense():
    """Users can update an expense."""
    assert False

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