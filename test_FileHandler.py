import datetime

from Category import Category
from FileHandler import matchWithExpectedCategory, isExpenseFromMonth, isExpenseFromYear


class TestFileHandler:
    CREATION_DATE_KEYWORD = "creationDate"

    def test_match_with_expected_category_false(self):
        assert False == matchWithExpectedCategory(Category.HEALTH, {"category": Category.UNDEFINED})

    def test_match_with_expected_category_true(self):
        assert True == matchWithExpectedCategory(Category.UNDEFINED, {"category": Category.HEALTH})

    def test_is_expense_from_month_case_this_year_true(self):
        result = isExpenseFromMonth(12, {self.CREATION_DATE_KEYWORD: "2025-12-22T13:32:55.880110"},
                                    currentDate=datetime.datetime(2025, 12, 29))
        assert True == result

    def test_is_expense_from_month_case_this_past_year_true(self):
        result = isExpenseFromMonth(2, {self.CREATION_DATE_KEYWORD: "2024-02-22T13:32:55.880110"},
                                    currentDate=datetime.datetime(2025, 1, 11))
        assert True == result

    def test_is_expense_from_month_case_this_year_false(self):
        result = isExpenseFromMonth(10, {self.CREATION_DATE_KEYWORD: "2025-12-22T13:32:55.880110"},
                                    currentDate=datetime.datetime(2025, 12, 29))
        assert False == result

    def test_is_expense_from_month_case_this_past_year_false(self):
        result = isExpenseFromMonth(2, {self.CREATION_DATE_KEYWORD: "2024-03-22T13:32:55.880110"},
                                    currentDate=datetime.datetime(2025, 1, 11))
        assert False == result

    def test_is_expense_from_year_true(self):
        result = isExpenseFromYear(2025, {self.CREATION_DATE_KEYWORD: "2025-03-22T13:32:55.880110"})
        assert result

    def test_is_expense_from_year_false(self):
        result = isExpenseFromYear(2025, {self.CREATION_DATE_KEYWORD: "2024-03-22T13:32:55.880110"})
        assert not result
