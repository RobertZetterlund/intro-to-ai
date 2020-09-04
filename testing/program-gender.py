# coding=iso8859_10
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./chalmers-approved.csv", encoding="iso8859_10")

diff = "diff %\-enheter"

df = df[df["Utbildningens namn"].str.contains("CIVILINGENJOR")]

df["Utbildningens namn"] = df["Utbildningens namn"].apply(lambda x: str(x)[:-15])

df["totalt"] = df["Kvinnor totalt"] + df["Man totalt"]

df = df.drop(
    columns=[
        "Termin",
        "Program/kurs",
        "Anm.kod",
        "Kvinnor 1:a hand",
        "Man 1:a hand",
        "Univ/hogskola",
    ]
)

total_female_applicants = df["Kvinnor totalt"].sum()
total_male_applicants = df["Man totalt"].sum()

df["Kvinnor %"] = (100 * df["Kvinnor totalt"] / total_female_applicants).round(2)
df["Man %"] = (100 * df["Man totalt"] / total_male_applicants).round(2)

df[diff] = df["Man %"] - df["Kvinnor %"]


df = df.sort_values(by=diff, ascending=True)
print(df)

difference = df[diff]


# y = ["{} to {} years".format(i, i + 4) for i in range(0, 90, 4)]
# d_1 = np.random.randint(0, 150, 23)
# d_2 = -1 * d_1

colors = np.where(df[diff] < 0, "pink", "blue")

fig, ax = plt.subplots()
ax.bar(df["Utbildningens namn"], df[diff], color=colors)
ax.set_yticks(np.arange(-8, 9, 4))


# Formatting x labels
plt.xticks(rotation=90)
plt.title("Differences in number of applicants to programs by gender at Chalmers")
plt.ylabel("Difference (men % - women %)")

plt.tight_layout()

plt.savefig("../assignment1/fig/program-gender-difference")