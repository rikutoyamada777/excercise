# (1)
a = [10, 8, 12, 17, 5]

# (2)
print("(2)", a[-1])

# (3)
a.append(13)
print("(3)", a)

# (4)
b = sorted(a)
print("(4)", "a=", a, ",", "b=", b)

# (5)
d = {'dog': '犬', 'cat': '猫', 'bird': '鳥'}

# (6)
print("(6)", d['cat'])

# (7)
print("(7)", "monkey=", 'monkey' in d)
print("(7)*", "cat=", 'cat' in d)
