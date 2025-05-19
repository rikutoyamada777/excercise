result = 0

def sum(x):
    global result
    mae = result
    result += x
    return str(mae)+"+"+str(x)+"=>"+str(result)

while True:
    try:
        s = input("Please input number ==> ")
        num = int(s)
        print(sum(num))
    except ValueError:
        print("Not a number is inputted Program exit")
        break