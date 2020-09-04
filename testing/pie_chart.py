# coding=iso8859_10
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# use pandas to read csv
df = pd.read_csv("./chalmers-approved.csv", encoding="iso8859_10")

df = df[df["Utbildningens namn"].str.contains("CIVILINGENJOR")].sort_values(
    by=["Man totalt"]
)

# print(df["Utbildningens namn"].head(1).map(lambda x: str(x)[:-15]))
print(df["Utbildningens namn"].map(lambda x: str(x)[:-15]))

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis("equal")
programs = df["Utbildningens namn"].map(lambda x: str(x)[:-15])
sectionColorsDICT = {
    "AUTOMATION OCH MEKATRONIK": "grey",
    "BIOTEKNIK": "#01271D",
    "DATATEKNIK": "orange",
    "ELEKTROTEKNIK": "yellow",
    "INDUSTRIELL EKONOMI": "purple",
    "INFORMATIONSTEKNIK": "cyan",
    "KEMITEKNIK": "#047155",
    "KEMITEKNIK MED FYSIK": "#09ECB0",
    "MASKINTEKNIK": "#442222",
    "TEKNISK DESIGN": "magenta",
    "TEKNISK FYSIK": "#1a1a1a",
    "SAMHALLSBYGGNADSTEKNIK": "blue",
    "TEKNISK MATEMATIK": "#221111",
    "MEDICINTEKNIK": "#ee77ff",
    "GLOBALA SYSTEM": "#C97D60",
}
colors = [sectionColorsDICT[program] for program in programs]
students_f = df["Man totalt"]
# students_m = df["Män totalt"]
ax.pie(
    students_f,
    labels=programs,
    autopct="%1.1f%%",
    colors=colors,
    explode=students_f / 6000,
)

plt.show()
