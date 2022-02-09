# --- For Loop
# The last digit is exclusive. Eg. for 10 items 10 is exclusive as starting index is 0
for i in range(10):
    print("With Only Count: ", i)

for i in range(10):
    print("With Zero Base Start and Count: ", i)

for i in range(1, 10):
    print("With Custom Start and Count: ", i)

for i in range(1, 10, 2):
    print("With Custom Start and Custom Increment: ", i)

# For with Arrays
my_list = [1, 2, 3, 4]
for i in range(my_list):
    print("With List: ", i)
