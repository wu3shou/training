import requests
from bs4 import BeautifulSoup


headers={
	'uesr-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'
	}
for page in range(1,5):
	html=requests.get('https://www.shixiseng.com/interns?page={}&type=intern&keyword=python',format(page),headers=headers)
	soup=BeautifulSoup(html.text,'lxml')
	offers=soup.select('.intern-wrap.intern-item')
	for offer in offers:
		url=offer.select('.f-l.intern-detail__job a')[0]['href']
		print(url)


