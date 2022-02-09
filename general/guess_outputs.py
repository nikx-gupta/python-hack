my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

var = 1
while var < 10:
    print("#")
    var = var << 1

for i in range(1):
    print("#")
else:
    print("#")

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

t = [[3 - i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)
