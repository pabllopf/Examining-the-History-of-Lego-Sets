


# Description: 
The Rebrickable dataset includes data on every LEGO set that has ever been sold; the names of the sets, what bricks they contain, etc. It might be small bricks, but this is big data! In this project, you will use this dataset together with the pandas library to dig into the history of Lego's licensed sets, including uncovering the percentage of all licensed sets that are Star Wars themed.


# Project Instructions
The team responsible for the Star Wars partnership has asked for specific information in preparation for their meeting:

What percentage of all licensed sets ever released were Star Wars themed? Save your answer as a variable the_force, as an integer (e.g. 25).

In which year was the highest number of Star Wars sets released? Save your answer as a variable new_era, as an integer (e.g. 2012).


Lego is a household name across the world, supported by a diverse toy line, hit movies, and a series of successful video games. In this project, we are going to explore a key development in the history of Lego: the introduction of licensed sets such as Star Wars, Super Heroes, and Harry Potter.

The introduction of its first licensed series, Star Wars, was a hit that sparked a series of collaborations with more themed sets. The partnerships team has asked you to perform an analysis of this success, and before diving into the analysis, they have suggested reading the descriptions of the two datasets to use, reported below.

## The Data

You have been provided with two datasets to use. A summary and preview are provided below.

## lego_sets.csv

| Column     | Description              |
|------------|--------------------------|
| `"set_num"` | A code that is unique to each set in the dataset. This column is critical, and a missing value indicates the set is a duplicate or invalid! |
| `"name"` | The name of the set. |
| `"year"` | The date the set was released. |
| `"num_parts"` | The number of parts contained in the set. This column is not central to our analyses, so missing values are acceptable. |
| `"theme_name"` | The name of the sub-theme of the set. |
| `"parent_theme"` | The name of the parent theme the set belongs to. Matches the name column of the parent_themes csv file.
|

## parent_themes.csv

| Column     | Description              |
|------------|--------------------------|
| `"id"` | A code that is unique to every theme. |
| `"name"` | The name of the parent theme. |
| `"is_licensed"` | A Boolean column specifying whether the theme is a licensed theme. |
