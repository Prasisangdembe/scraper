import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
print(url)
# Parsing the HTML
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
# print(soup.prettify())
# soup.find('table')
# soup.find_all()
#taking only one table using indexing
table=soup.find_all('table')[1]
#reading the titles
word_titles=table.find_all('th')
print(word_titles)
#in / fromat
final_titles=[title.text for title in word_titles]
print(final_titles)
# removing /format
final_titles=[title.text.strip() for title in word_titles]
print(final_titles)

#keeping those titles into dataframe
df=pd.DataFrame(columns=final_titles)
print(df)

## getting datas
column_data=table.find_all('tr')

for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    print(individual_row_data)
    length=len(df)
    df.loc[length]=individual_row_data

print(df)
df.to_csv('scrape.csv',index=False)



