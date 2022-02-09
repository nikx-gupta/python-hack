# Swap list with indices
my_list = [10, 1, 8, 3, 5]
my_list[1], my_list[2] = my_list[2], my_list[1]

# Reverse list
# for Odd number list the middle number will be preserved
my_list = [10, 1, 8, 3, 5]
list_len = len(my_list)
print("Original list: ", my_list)
for i in range(list_len // 2):
    my_list[i], my_list[-1 - i] = my_list[-1 - i], my_list[i]
print("Reverse Swap: ", my_list)

# Append to the list
beatles = []

# Step - 1: Add Manual
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Step 1: Add Manual: ", beatles)

# Step 2: Prompt for Addition
beatles.append(input("Enter First Name: "))
beatles.append(input("Enter Second Name: "))
print("Step 2: Prompt for Addition: ", beatles)

# Step 3: Remove element from list
del beatles[1]
print("Step 3: Remove: ", beatles)

# step 4: Insert Element
beatles.insert(0, "Ringo Starr")
print("Step 4: Insert Element: ", beatles)

# testing list length
print("The Fab", len(beatles))

# Copy list
my_list = [8, 10, 6, 2, 4]
print("Orig List: ", my_list)
my_list_2 = my_list[:]
my_list[0] = 20
print("Copied List: ", my_list_2)

my_list = [1,2,3]
for v in range(len(my_list)):
    my_list.insert(1,my_list[v])
print(my_list)
