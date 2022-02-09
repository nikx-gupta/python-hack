
name = input("Enter name: ")

# De Morgan Law

p = name == "s1"
q = name == "s2"
cond1 = not(p and q)
cond2 = not p or not q

print("Always: cond1: ", cond1, " = cond2: ", cond2)

