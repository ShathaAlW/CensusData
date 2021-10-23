import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

census = pd.read_csv('census_data.csv', index_col=0)
print(census.head())


# inspecting data types
print(census.dtypes)


# 'birth_year' data type has been assigned as object (str) while it should be an int
print(census['birth_year'].unique())


# replace 'missing' value with 1967
census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
print(census['birth_year'].unique())


# change data type from objective (str) to int
census['birth_year'] = census['birth_year'].astype('int')
print(census.dtypes)


# average birth year
print('Average birth year:')
print(census['birth_year'].mean())


# convert 'higher_tax' to category type with order: strongly disagree < disagree < neutral < agree < strongly agree
correct_order = ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree']
census['higher_tax'] = pd.Categorical(census['higher_tax'], correct_order, ordered= True)
print(census['higher_tax'].unique())


# median sentiment of 'higher_tax'
census['higher_tax'] = census['higher_tax'].cat.codes
median_index = census['higher_tax'].median()

print('Median sentiment of higher tax for wealthy:')
print(correct_order[int(median_index)])


# One-Hot encode of 'marital_status'
census = pd.get_dummies(data= census, columns= ['marital_status'])
print(census.head())


# Extra: using label coding - uncomment One-Hot encode code, for this to work
print(census['marital_status'].unique())
correct_order = ['single', 'married', 'divorced', 'widowed']
census['marital_status'] = pd.Categorical(census['marital_status'], correct_order, ordered= True)
census['marital_codes'] = census['marital_status'].cat.codes
print(census.head())


# Extra: create 'age-group' with 5-year increment. Then, label encode age groups
census['age'] = 2021 - census['birth_year']
print(census.head())

print(min(census['age'].unique()))
print(max(census['age'].unique()))

bins = [x for x in range(10, 86, 5)]
labels = ['10-15','16-20', '21-25', '26-30','31-35', '36-40','41-45', '46-50', '51-55', '56-60', '61-65', '66-70', '71-75', '76-80','81-85']
census['age_group'] = pd.cut(census['age'], bins= bins, labels= labels)

census['age_group'] = pd.Categorical(census['age_group'], labels, ordered= True)
print(census['age_group'].unique())

census['age_group_codes'] = census['age_group'].cat.codes
print(census.head())

# barplot of age groups in census
plt.figure(figsize=(10,6))
sns.countplot(x= 'age_group', data= census)
plt.title('Age group counts in census', fontsize= 14)
plt.xlabel('Age group', fontsize= 12)
plt.ylabel('Counts', fontsize= 12)
plt.xticks(rotation= 90)
plt.show()
