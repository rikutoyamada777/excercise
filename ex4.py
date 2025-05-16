#(1)
import random

prob=random.randint(1,100)
money=random.randint(1000,10000)

print ("(1)降水確率",prob,"%","所持金",money,"円")
if prob >= 80:
    print("天気が悪いので今日は家で過ごしましょう")
elif prob >= 40 and money >= 5000:
    print("雨が降りそうなので今日は映画を見に行きましょう")
elif prob < 40 and money >= 5000:
    print("天気がいいので今日は遠出しましょう")
elif prob < 40 and money < 5000:
    print("今日は近場で遊びましょう")
elif prob >= 40 and money < 5000:
    print("雨が降りそうなので友達の家で遊びましょう")

# (2)
ksum = 0
i = 1

while i <= 100:
    if i % 2 == 1:
        ksum += i
    i += 1
print("(2)",ksum)

# (3)
kisum = 0
j = 1

for j in range(1, 100):

    if j % 2 == 1:
        kisum += j
    j += 1
print("(3)",kisum)

#(4)
I=[h for h in range(1,11) if h % 2 == 0]
