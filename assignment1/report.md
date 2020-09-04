# Assignment 1: Introduction to Data Science and Python
## Tobias Lindroth: x hrs
## Robert Zetterlund: y hrs

# Task 1

### State the Assumptions and decisions

- Decisions

  - We selected two datasets from different sources. We found datasets containing both life expectancy and GDP per capita. But we wanted to use two datasets for the learning of experience of merging datasets. 
  - We decided to merge the data-sets and only include entities within both.
  - We selected year 2017 because that was the latest year that both our datasets had data from.


- Assumptions
  - We assume that the spelling of countries and the use of the country code are consistent across the datasets.
  - We assume numerical values of the data we plan to plot
  - We assume that the datasets have data over similar countries
  - We assume that the data is correctly formatted according to .csv-standards
  - We assume that within a dataset there is no duplicated entries

###  A scatter plot of GDP per capita vs life expectancy.

![img](fig/gdp_life.png)

## Question A - Which countries have a life expectancy higher than one standard deviation above the mean?

Out of the 182 entities examined, the following had a life expectancy higher than one standard deviation above the mean:


- Anguilla
- Australia
- Austria
- Belgium
- Bermuda
- Canada
- Cayman Islands
- Cyprus
- Denmark
- Finland
- France
- Germany
- Greece
- Hong Kong
- Iceland
- Ireland
- Israel
- Italy
- Japan
- Luxembourg
- Macao
- Malta
- Netherlands
- New Zealand
- Norway
- Portugal
- Singapore
- Slovenia
- South Korea
- Spain
- Sweden
- Switzerland
- United Kingdom

(33 entities)

```python
# Get standard deviation and mean from dataframe
life_std = np.std(merged_entries[LIFE])
life_mean = np.mean(merged_entries[LIFE])
# Filter based on entries which value is larger than mean + one standard deviation
high_life = merged_entries[merged_entries[LIFE] > life_mean+life_std]
```

To asses how reasonable 33 entities are we use an ideal normal distribution of 182 entities. In an normal distribution approximately 15.7% (28 entities) of the population lies above the range of `mean+sigma`. In our case, `33/182` equals `0.18` (18.1%) which we (without going into more math) deem to be similar.



## Question B - Which countries have high life expectancy but have low GDP?

We assume that a country has a low GDP if their GDP is lower than 0.253 standard deviation below the mean. Meaning that they are a part of the bottom 40%.

Furthermore, we assume that a high life expectancy is higher than 0.253 standard deviation above the mean. Meaning that they are a part of the top 40%.

Using these assumptions, the countries that have high life expectancy but low GDP are shown in blue:

- Albania
- Algeria
- Anguilla
- Antigua and Barbuda
- Barbados
- Bosnia and Herzegovina
- Brazil
- China
- Colombia
- Ecuador
- Honduras
- Macedonia
- Maldives
- Morocco
- Peru
- Saint Lucia
- Sri Lanka
- Tunisia
- Turks and Caicos Islands
- Vietnam

(20 entities)

![img](fig/gdp_life_b.png)

We assume that a high GDP is correlated to high life-expectancy due to having the means to improve living conditions. 

To asses how reasonable 20 entities are we think about Venn Diagrams.

* There should be about 40% of the entities having a high GDP, group named HG.
* There should be about 40% of the entities having a low life expectaction, group named LE.

* If the union between HG and LE amounts to 40% of the entities, we have a strong correlation.
* If it is 0%, we have no correlation at all.

* If the distribution were to be completely uncorrelated, we would assume that we would get (0.4*.0.4)100% = 16% of the entities. 


Our 20 entities is approximately 11% of the population, which is lower than a uncorrelated scenario. When we calculate the union of high gdp and high life expectation we get 27% of the total population, which is higher than a uncorrelated scenario. This suggests to us that there is a correlation.

Therefore we find the number of entities reasonable because we believe that the correlation between the high life-expectancy and high gdp are relatively high.


## Question C - Does every strong economy have high life expectancy?

We assume that a GDP higher than `0.253 * standard deviation`, meaning that they are a part of the top 40%, indicates a strong economy.

Using this assumption and the previously stated assumption about a high life expectancy, the countries that have a strong economy, but not a high life expectancy, are:

- Seychelles
- Trinidad and Tobago

```python
# merge dataframes
merged_entries = pd.merge(gdp_entries, life_entries, on=["Code", "Year", "Entity"])

# get standard deviation and mean from entries (same for life_std and life_mean)
gdp_std = np.std(merged_entries[GDP])
gdp_mean = np.mean(merged_entries[GDP])

# filter based on having strong economy
strong_economy = merged_entries[
    merged_entries[GDP] > gdp_mean + gdp_std * STD_CONSTANT
]
```

![img](fig/gdp_life_c.png)


The 2 entities is approximately 4 % out of the countries with a strong economy. This indicates that the correlation between having a high GDP and a high life expectancy is strong. This correlation seems reasonable since having a strong economy will make it easier to for example provide good healthcare, living conditions etc. 

## Question D - Clean the data

The rows that we removed were those not containing data from the year that we were examining (2017), or the Entity not being available in both datasets. After the removal of rows we decided to remove the columns *Code* and *Year* as they were no longer pertaining to the assignment. Important to note is that the information of the dataframe now showing data from the year 2017 is excluded. However, instead of having 2017 repeated through an entire column, we add the year to the column name of Entity. Making `Entity` be `Entity, 2017`. Note that we are aware that this restricts the re-usability of the dataframe, as the convention of naming the field `Entity`, but for the sake of this assignment we allow this.


**We merged the datasets:**

```python
# merge entries with inner join. Excluding entities not available in both datasets.
merged_entries = pd.merge(gdp_entries, life_entries, on=["Code", "Year", "Entity"])
```

**We removed:**

- All the rows that didn't have the year we were interested in.

```python
# Filter based on year
merged_entries = merged_entries[(merged_entries["Year"] == SELECTED_YEAR)]
```

- Columns with data that wasn't used in any of the tasks. Meaning, we removed the "Code" and "Year" columns.

```python
# Drop Code and Year columns, also rename
df_clean = merged_entries.drop(columns=["Code", "Year"])
df_clean = df_clean.rename(columns={GDP: "GDP (2011 international-$)", 'Entity': "Entity, {SELECTED_YEAR}"})

df_clean.head(2)
```

| index | Entity (2017)  | GDP ((2011 international-\$)) | Life expectancy (years) |
| ----- | -------       | ----------------------------- | ----------------------- |
| 0     | Albania | 9544.7402                     | 76.562                  |
| 1     | Algeria | 12590.2260                    | 74.938                  |
| 2     | Angola  | 5988.5347                     | 55.350                  |

<!--- Något om att vi funderade på att ta bort alla rader som ej blev "utvalda" av varken task A, task B, task C ? --->

# Task 2

## Boxplots

In this section we present Boxplots that we made.

### New cases of Covid-19 in August in Sweden, Norway, Denmark and Finland

The following code snippet highlights part of the program relevant to creating the boxplot-graph.

```python
# Define which locations that are of interest
locationList = ["Sweden", "Norway", "Finland", "Denmark"]
# Filter based on locationList
entries = df[(df["location"].isin(locationList))]
# Filter based on date being august 2020
entries = entries[(entries["date"].str.contains("2020-08"))]

# Define function for extracting new_cases based on location
def extract_new_cases(location):
    return entries.loc[entries["location"] == location]["new_cases"]

# Create a matrix containing each dataset in an array.
location_data_matrix = [extract_new_cases(location) for location in locationList]

# Boxplot
bp = ax.boxplot(location_data_matrix)
```

The graph explores the spread the reporting of new cases of Covid-19 vary in nordic countries during the month of August.
![img](fig/boxplot_covid.png)



## Scatterplots

Below are scatterplots exploring correlation between two datasets.

### Annual working hours per person vs Happiness

![img](fig/working-hours-happiness.png)

The graph shows that there is some correlation between how much you work and your happiness. It seems reasonable that the amount of work would affect the happiness as with more work you won't have as much spare time to do things you enjoy and like. Of course, there are also many other factors that affects one's happiness, but it still seems reasonable that there is at least a weak causation between amount of work and happiness.



### Internet usage vs one person households

The graph shows that there is some correlation between the percentage of the population that uses the internet and the share of one person households.

![img](fig/internet_household.png)

## The correlation between age and happiness

The following graphs explores the notion that being happy makes you live a longer life.

![img](fig/median-age_happiness.png)
