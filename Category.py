from enum import StrEnum


class Category(StrEnum):
    UNDEFINED = "UNDEFINED" # Generic Option
    FOOD = "FOOD"
    BILL = "BILLING"
    INVESTMENT = "INVESTMENT"
    HEALTH = "HEALTH"