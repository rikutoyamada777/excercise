nenrei=input("年齢を入力してください:0~100==>")
nenrei=int(nenrei)


if nenrei < 0 or nenrei > 100 :
   print("エラー:入力しなおしてください")
elif nenrei <= 19:
    print("未成年です。","\n"
          "地方自治体によっては医療費が￥200のところも。")
elif nenrei >= 60:
    print("定年後も元気100%で過ごしてください")
else:
    print("成年です。", "\n"
          "飲酒・喫煙は控えめに")

