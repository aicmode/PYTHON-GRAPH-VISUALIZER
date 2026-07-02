import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# 日本語フォント設定（Mac向け）
plt.rcParams["font.family"] = "Hiragino Sans"
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["font.size"] = 11
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 12

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

colors = ["#4E79A7", "#F28E2B", "#59A14F", "#E15759", "#76B7B2", "#EDC948"]

# 1つ目：円グラフ
fig, ax = plt.subplots(figsize=(7, 6), facecolor="white")
wedges, texts, autotexts = ax.pie(
    department_counts.values(),
    labels=department_counts.keys(),
    autopct="%1.1f%%",
    pctdistance=0.79,
    startangle=90,
    counterclock=False,
    colors=colors[:len(department_counts)],
    wedgeprops={"width": 0.42, "edgecolor": "white", "linewidth": 2},
    textprops={"fontsize": 11, "color": "#333333"}
)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_weight("bold")
    autotext.set_color("white")
ax.text(
    0,
    0,
    f"参加者\n{len(scores)}名",
    ha="center",
    va="center",
    fontsize=18,
    fontweight="bold",
    color="#333333"
)
ax.set_title("所属ごとの参加者割合", pad=18, fontweight="bold")
ax.axis("equal")
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
plt.savefig("department_pie_chart.png", dpi=150, bbox_inches="tight")
plt.close()

# 2つ目：棒グラフ
fig, ax = plt.subplots(figsize=(8, 5), facecolor="white")
bars = ax.bar(
    department_average_scores.keys(),
    department_average_scores.values(),
    color=colors[:len(department_average_scores)],
    edgecolor="white",
    linewidth=1.5
)
ax.set_title("所属ごとの平均スコア", pad=16, fontweight="bold")
ax.set_xlabel("所属", labelpad=10)
ax.set_ylabel("平均スコア", labelpad=10)
ax.set_ylim(0, 100)
ax.grid(axis="y", color="#DDDDDD", linewidth=0.8, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(axis="x", labelsize=11)
ax.tick_params(axis="y", labelsize=10)
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1.5,
        f"{height:.1f}",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
        color="#333333"
    )
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
plt.savefig("department_average_bar_chart.png", dpi=150, bbox_inches="tight")
plt.close()

# 3つ目：ヒストグラム
fig, ax = plt.subplots(figsize=(8, 5), facecolor="white")
ax.hist(
    scores,
    bins=10,
    color="#4E79A7",
    edgecolor="white",
    linewidth=1.5
)
average_score = sum(scores) / len(scores)
ax.axvline(
    average_score,
    color="#E15759",
    linestyle="--",
    linewidth=2,
    label=f"平均：{average_score:.1f}点"
)
ax.set_title("スコア分布", pad=16, fontweight="bold")
ax.set_xlabel("スコア", labelpad=10)
ax.set_ylabel("人数", labelpad=10)
ax.grid(axis="y", color="#DDDDDD", linewidth=0.8, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)
ax.legend(frameon=False, fontsize=11)
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
plt.savefig("score_histogram.png", dpi=150, bbox_inches="tight")
plt.close()

print("=== グラフ作成完了 ===")
print("department_pie_chart.png を保存しました")
print("department_average_bar_chart.png を保存しました")
print("score_histogram.png を保存しました")
