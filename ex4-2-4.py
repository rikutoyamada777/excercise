students_data = [
    {"name": "A", "math": 85, "english": 92, "science": 78},
    {"name": "B", "math": 70, "english": 81, "science": 88},
    {"name": "C", "math": 95, "english": 88, "science": 92},
    {"name": "D", "math": 60, "english": 75, "science": 70},
    {"name": "E", "math": 88, "english": 90, "science": 85},
]

#①
math_list = [i["math"] for i in students_data]
ave=sum(math_list)/len(math_list)
print("①数学の平均点",ave)

#②
mostsan = ""
most_score = 0

for j in students_data:
    if most_score <= j["science"]:
        most_score = j["science"]
        mostsan = j["name"]+"さん"

print("②全体の理科の最高点",most_score, "取得者",mostsan)

#③

for k in students_data:
    k["total"] = k["math"] + k["english"] + k["science"]

for l in students_data:
    print(f"{l}")
