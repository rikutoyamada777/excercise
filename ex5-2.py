def greet(name,time):
    if time=="morning":
        print(name+"さん、おはようございます。")
    elif time=="noon":
        print(name+"さん、こんにちは。")
    elif time=="evening":
        print(name+"さん、こんばんは。")
    else:
        print(name+"さん、その時間帯は設定されていません")


a=input("名前を入力してください==>")
b=input("時間帯を入力してください(morning,noon,evening)==>")
greet(a,b)

