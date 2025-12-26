import datetime
import os

import pytest

from Expense import Expense
from FileHandler import FileHandler

TEST_ENV = "test"
fileHandler: FileHandler = FileHandler.getFileHandler("test")


@pytest.fixture(autouse=True)
def tearDown():
    """Fixture to delete the test_data.json file before each test."""
    test_file = fileHandler.jsonFilename
    if os.path.exists(test_file):
        os.remove(test_file)


def test_add_expense(tearDown):
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