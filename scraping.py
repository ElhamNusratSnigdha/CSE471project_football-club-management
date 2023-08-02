from bs4 import BeautifulSoup
import requests
import re


html_text = requests.get('https://onefootball.com/en/team/barcelona-5').text
soup = BeautifulSoup(html_text, 'lxml')
titles = soup.find_all('p', class_=re.compile(("^NewsTeaserV2_teaser__title")))
teasers = soup.find_all('p', class_=re.compile(("^NewsTeaserV2_teaser__preview")))
aS =soup.find_all('a', class_=re.compile(("^NewsTeaserV2_teaser__content")))
for title, url in zip(titles, aS): 
    titleText = title.text
    news_html = requests.get('https://onefootball.com' + url['href']).text
    news_soup = BeautifulSoup(news_html, 'lxml')
    article_paragraphs = news_soup.find_all('div', class_=re.compile(("^ArticleParagraph")))
    articleText = ''
    for article in article_paragraphs:
        if article.p:
            articleText += article.p.text
    
    