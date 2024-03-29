from lxml import etree
import requests
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


url = 'https://www.nature.com/nature/research'
data = requests.get(url, headers=headers).text
s=etree.HTML(data)
test = s.xpath('//*[@id="content"]/div[2]/div/div/div/div/div/ul/li/article/div/h3/a/text()')
pattern = re.compile('\s{16}')
collect_data = []

for i in range(0,49):
	result = re.sub(pattern, '',test[i])
	print("index:%2d, title: %s" % (i, result))
	collect_data.append({
			'index' : i,
			'title' : result
		   })
	time.sleep(0.2)

with open('data.json', 'w') as f:
	json.dump(collect_data, f)
