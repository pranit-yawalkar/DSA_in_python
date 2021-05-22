expense = [2200, 2350, 2600, 2130, 2190, 2000]

jan_feb_extra = expense[1] - expense[0]
print(jan_feb_extra)

first_quarter_expense = expense[0] + expense[1] + expense[2]
print(first_quarter_expense)

print("Did i spent 2000 in any month?", 2000 in expense)

expense.append(1980)
expense[3] = expense[3] - 200
print("Expense in the month of april: ", expense[3])

heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]
print(len(heroes))
heroes.append("black panther")
heroes.remove("black panther")
heroes.insert(3, "black panther")
print(heroes)
heroes[1:3] = ["doctor strange"]
print(heroes)

# print(dir(heroes))
heroes.sort()
print(heroes)
