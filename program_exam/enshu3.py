print("    ", end="")
for i in range(1, 10):
    print(f"{i:>3} ", end="")
print()

for i in range(1, 10):
    print(f"{i:>3} ", end="")
    for j in range(1, 10):
        product = i * j
        if product % 6 == 0:
            print(f"{'##':>3} ", end="")
        elif product % 2 == 0:
            print(f"{'**':>3} ", end="")
        elif product % 3 == 0:
            print(f"{'@@':>3} ", end="")
        else:
            print(f"{product:>3} ", end="")
    print()