import requests
from bs4 import BeautifulSoup

headers={
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'
}

for page in range(1,5):
	html=requests.get('https://www.qiushibaike.com/text/page/{}/',format(page),headers=headers)
	soup=BeautifulSoup(html.text,'lxml')
	articles=soup.select('.article.block.untagged.mb15')
	for article in articles:
		author=article.select('.author.clearfix h2')[0].text
		content=article.select('span')[0].text
		print(author,content)
		