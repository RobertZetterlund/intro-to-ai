import pandas as pd
import matplotlib.pyplot as plt

SELECTED_DATE = "2020-08-31"
df = pd.read_csv("../res/owid-covid-data.csv")


countryList = ["Sweden", "Norway", "Finland", "Denmark"]

entries = df[(df["location"].isin(countryList))]

entries = entries[(entries["date"].str.contains("2020-08"))]

entries = entries[["location", "date", "new_cases"]]


def extract_data(country):
    return entries.loc[entries["location"] == country]["new_cases"]


country_data = [extract_data(country) for country in countryList]

(fig, ax) = plt.subplots()
# Create an axes instance
bp = ax.boxplot(country_data)


ax.set_title("New cases of corona in nordic countries in August")
# ax.legend(
#    [bp["boxes"][0], bp["boxes"][1], bp["boxes"][2], bp["boxes"][3]],
#    countryList,
#    loc="upper right",
# )

plt.xticks(range(1, len(countryList) + 1), countryList)
plt.savefig("../fig/boxplot_covid.png")
# plt.show()
