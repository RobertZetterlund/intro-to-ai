import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("../res/merit-based-on-parents.csv")

df = df.loc[df["svensk och utlandsk bakgrund"] == "svensk bakgrund"]

labels = ["forgymnasial", "gymnasial", "eftergymnasial"]


def getMerit(label, gender):
    label_data = df.loc[df["foraldrars utbildningsniva"] == label]
    return label_data.loc[label_data["kon"] == gender]


men_merits = [getMerit(label, "pojkar") for label in labels]
women_merits = [getMerit(label, "flickor") for label in labels]

print(men_merits)
print(women_merits)
