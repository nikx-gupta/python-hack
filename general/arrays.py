hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user

# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Enter the replacement number: "))

# Step 2: write a line of code that removes the last element from the list.
print("Deleting the last number: ", hat_list[4])
del hat_list[4]

# Step 3: write a line of code that prints the length of the existing list.
print("Length: ", len(hat_list))

print("hatList: ", hat_list)

# Adding to the List
my_list = []  # Creating an empty list.
for i in range(5):
    my_list.append(i + 1)
print("my_list: ", my_list)

# ---- Using Slice Indices ----
my_list = [8, 10, 6, 2, 4]
print("Slice: Full: [:] => ", my_list[:])
print("Slice: Start Index: [1:] => ", my_list[1:])
print("Slice: Start & End Index: [1:4] => ", my_list[1:4])
print("Slice: Till End Index: [:4] => ", my_list[:4])
print("Slice: Negative Index: [:-1] => ", my_list[:-1])

# ---- Initializing the list with data ----
# Format - [<expr> for x in range() <optional condition expr>]
squares = [x ** 2 for x in range(12)]
print("Initial List with Squares: ", squares)
print("Extract Only Even: ", [[x for x in squares if x % 2 == 0]])

# ---- Two Dimensional List ----
board = []
for i in range(8):
    row = [2 for i in range(i)]
    board.append(row)
print("Two Dimensional using for loop: ", board)
# Compact  way
board = [[2 for x in range(i)] for i in range(8)]
print("Two Dimensional using compact method: ", board)

