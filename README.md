# cli-expense-tracker
https://roadmap.sh/projects/expense-tracker

Also training my TDD skills...

## Setup
- Install Python 3.8+
- Clone the project
- Access its root dir through CLI

## How to use it
```bash
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

$ expense-tracker summary --month 8
# Total expenses for August: $20
```
**Docs at:** `py .\expense-tracker.py --help`

### Features
- **add (working and tested)**
- **update (working and tested)**
- **delete (working and tested)**
- _list (todo)_
- _summary (todo)_
- _filtered summary (todo)_
- _extras: black-box testing (todo)_
- _extras: export to CSV (todo)_


**Tasks**
- [X] Users can add an expense with a description and amount.
- [X] Users can update an expense.
- [X] Users can delete an expense.
- [ ] Users can view all expenses. (**list**)
- [ ] Users can view a summary of all expenses. (**summary**)
- [ ] Users can view a summary of expenses for a specific month (of current year).
- [ ] Add expense categories and allow users to filter expenses by category. (**filterByCategory**)
- [ ] Allow users to export expenses to a CSV file.

**Disclaimer: No AI was used developing this program. Only docs**
