expenses = []
total = 0
num_expeses = int(input("Enter # of expenses: "))
for i in range(num_expeses):
    expenses.append(float(input("Enter an Expense: ")))
total = sum(expenses)

print ("You Spent $", total)
print ("You Spent $", total, sep="")