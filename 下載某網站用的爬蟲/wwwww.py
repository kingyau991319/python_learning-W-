import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import re

url  = ''
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all('img')

folder_path = './photo/'

if os.path.exists(folder_path) == False:
    os.makedirs(folder_path)

for index,item in enumerate(items):

	if item:	
		pattern = re.compile(r"https://(.*?).jpg")
		new_item = str(item)
		new_item = pattern.findall(new_item)
		new_item = "https://" + new_item[0] + ".jpg"  

		html = requests.get(new_item)
		img_name = folder_path + str(index + 1) +'.jpg'

		with open(img_name, 'wb') as file:
			file.write(html.content)
			file.flush()
		file.close()

print('ok')
