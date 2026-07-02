import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# 日本語フォント設定（Mac向け）
plt.rcParams["font.family"] = "Hiragino Sans"

names = []
departments = []
scores = []

with open("課題3.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        names.append(row["名前"])
        departments.append(row["所属"])
        scores.append(int(row["スコア"]))

# 1. 所属ごとの人数を集計
department_counts = defaultdict(int)

for department in departments:
    department_counts[department] += 1

# 2. 所属ごとの平均スコアを集計
department_score_totals = defaultdict(int)
department_score_counts = defaultdict(int)

for department, score in zip(departments, scores):
    department_score_totals[department] += score
    department_score_counts[department] += 1

department_average_scores = {}

for department in department_score_totals:
    department_average_scores[department] = (
        department_score_totals[department] / department_score_counts[department]
    )

# 1つ目：円グラフ
plt.figure()
plt.pie(
    department_counts.values(),
    labels=department_counts.keys(),
    autopct="%1.1f%%"
)
plt.title("所属ごとの参加者割合")
plt.savefig("department_pie_chart.png")
plt.close()

# 2つ目：棒グラフ
plt.figure()
plt.bar(
    department_average_scores.keys(),
    department_average_scores.values()
)
plt.title("所属ごとの平均スコア")
plt.xlabel("所属")
plt.ylabel("平均スコア")
plt.ylim(0, 100)
plt.savefig("department_average_bar_chart.png")
plt.close()

# 3つ目：ヒストグラム
plt.figure()
plt.hist(scores, bins=10)
plt.title("スコア分布")
plt.xlabel("スコア")
plt.ylabel("人数")
plt.savefig("score_histogram.png")
plt.close()

print("=== グラフ作成完了 ===")
print("department_pie_chart.png を保存しました")
print("department_average_bar_chart.png を保存しました")
print("score_histogram.png を保存しました")