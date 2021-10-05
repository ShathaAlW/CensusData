# CensusData

cleaning census data, which has 8 columns: first_name, last_name, birth_year, voted , num_children, income_year, higher_tax, marital_status

income_year: The average yearly income the respondent earns
higher_tax: The respondent’s answer to the question: “Rate your agreement with the statement: the wealthy should pay higher taxes.”

The code includes:
- assessing variable type, inspecting data types and altering data.
also:
- one-Hot encoding 'marital_status' in case the Census team wants to use machine learining models in the future.
- label encoding 'marital_status' which could help the Census team use machine learning to predict if a respondent thinks the wealthy should pay higher taxes based on their marital status.
- Extra: extracting 'age' of respondents from 'birth_age'. Then creating new variable 'age_group' with five-year increment.
- Extra: label encoding 'age_group' to assist the Census team in the event they would like to use machine learning to predict if a respondent thinks the wealthy should pay higher taxes based on their age group.

credit to: Codecademy
