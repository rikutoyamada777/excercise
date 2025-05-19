def get_max(*a):
    x = 0
    for num in a:
        if num >= x:
            x = num
    return x


kosuu = int(input("入力する個数を入力してね ==> "))
numbers = [int(input(f"{i+1}番目の数値を入力してね ==> ")) for i in range(kosuu)]
print("最大値:", get_max(*numbers))
