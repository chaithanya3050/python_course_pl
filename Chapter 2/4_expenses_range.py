expenses = []
total = 0
for i in range(7):
    expenses.append(float(input("Enter an Expense:")))
total = sum(expenses)

print ("You Spent $", total)
print ("You Spent $", total, sep="")