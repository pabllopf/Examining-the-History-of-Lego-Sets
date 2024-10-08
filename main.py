# Import pandas and read in the DataFrame, and inspect it
import pandas as pd
lego_sets = pd.read_csv('data/lego_sets.csv')
lego_sets.head()

# Drop relevant missing rows
lego_sets_clean = lego_sets.dropna(subset=['set_num', 'name', 'theme_name'])
lego_sets_clean.head()

# Get list of licensed sets
parent_themes = pd.read_csv('data/parent_themes.csv')
licensed_themes = parent_themes[parent_themes['is_licensed']]['name']
licensed_themes.head()

# Subset for licensed sets
licensed = lego_sets_clean['parent_theme'].isin(licensed_themes)
licensed_sets = lego_sets_clean[licensed]
licensed_sets.head()

# Calculate the percentage of licensed sets that are Star Wars themed
all_sets = len(licensed_sets)
star_wars_sets = len(licensed_sets[licensed_sets['parent_theme'] == 'Star Wars'])
ratio = star_wars_sets / all_sets
the_force = int(ratio * 100)
print(f'The percentage of licensed sets that are Star Wars themed is {the_force}%.')

# Create a pivot table of sets released by theme per year
licensed_pivot = licensed_sets.pivot_table(index='year', columns='parent_theme', values='set_num', aggfunc='count')

# Find the year when the most Star Wars sets were released
licensed_pivot.sort_values(by="Star Wars", ascending=False)["Star Wars"]
new_era = 2016
print(f'The year when the most Star Wars sets were released was {new_era}.')
