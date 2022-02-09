my_list = [8, 10, 6, 2, 4]

print("Actual List: ", my_list)
swap_occured = True
while swap_occured:
    swap_occured = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swap_occured = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("Sorted List: ", my_list)

# BuiltIn Sort
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print("BuiltIn Sort: ", my_list)


