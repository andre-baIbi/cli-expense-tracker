import datetime
from Category import Category
from FileHandler import FileHandler



class Expense:
    _id: int
    _creationDate: datetime.datetime
    _amount: float
    _description: str
    _category: Category
    _fileHandler: FileHandler

    def __init__(self, amount: float, description: str, category: Category, handler):
        self._amount = amount
        self._description = description
        self._category = category
        self._creationDate = datetime.datetime.now()
        self._fileHandler = handler
        self._id = self._fileHandler.getLatestId()

    def getId(self):
        return self._id

    def getAmount(self):
        return self._amount

    def getDescription(self):
        return self._description

    def getCategory(self):
        return self._category

    def getCreationDate(self):
        return self._creationDate

    @classmethod
    def add(cls, amount: float, description: str, handler=None, category: Category = Category.UNDEFINED):
        if not handler:
            handler = FileHandler.getFileHandler("prd")

        expense = cls(amount, description, category, handler)
        expense.addExpenseToFile()
        return expense

    def addExpenseToFile(self):
        data = self._fileHandler.parseDataFromJsonFile()
        data[self.getId()] = self.toDict()
        self._fileHandler.saveDataInJsonFile(data)

    def toDict(self):
        return {
            "id": self.getId(),
            "amount": self.getAmount(),
            "description": self.getDescription(),
            "category": self.getCategory().value,
            "creationDate": self.getCreationDate().isoformat(),
        }


if __name__ == '__main__':
    ...