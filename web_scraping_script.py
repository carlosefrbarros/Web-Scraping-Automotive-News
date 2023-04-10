# Web Scraping Automotive News
# This project was made to help a friend in his academic research, he is researching news about eletric cars in Brazil
# With the URLs from his Zotero references, I scraped and saved in .txt files

import pandas as pd
import requests
from bs4 import BeautifulSoup

url_excel = 'D:/INFO/Projetos Ciência de Dados/Web-Scraping-Automobile-News/References.xlsx'
output_folder = 'D:/INFO/Projetos Ciência de Dados/Web-Scraping-Automobile-News/Text'

# read xlsx to dataframe
df = pd.read_excel(url_excel)

# loop through url column of dataframe
for i, row in df.iterrows():

    # request to the urls
    response = requests.get(row['Url'])

    # scrape urls
    soup = BeautifulSoup(response.content, 'html.parser')
    url_title = soup.find('title')
    url_content = soup.find('div', class_='post-area__text')
    url_text = url_title.text.strip().replace(' | Automotive Business', '') + '\n' + url_content.text.strip()
    print('Scraped URL {}'.format(i+1))

    # write content to .txt file
    adress = output_folder + '/URL_' + str(i+1) + '.txt'
    text_file = open(adress, 'w', encoding='utf-8')
    text_file.write(url_text)
    text_file.close()
