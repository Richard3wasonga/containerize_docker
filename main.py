from bs4 import BeautifulSoup
import requests
import csv

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

# article = soup.find('div', class_='article')
# print(article) 

# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)

#     try:
#         summary = article.p.text
#     except Exception as e:
#         summary = None

#     print(summary)
#     print()


csv_file = open('bss_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'channel_link'])

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

notice = soup.find('div', class_='container')

# print(notice.prettify())

headline = notice.h1.text
print(headline)

paragraph = notice.find('p').text

print(paragraph)



youtube_channel = notice.find('a')['href']
print(youtube_channel)

csv_writer.writerow([headline, paragraph, youtube_channel])
csv_file.close()

