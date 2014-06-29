import urllib.request
import re
import argparse
from bs4 import BeautifulSoup 

webURL = "http://www.bplisn.net.cn/"
u = urllib.request.urlopen(webURL)
content = u.read()
soup = BeautifulSoup(content)

itemList = soup.find_all('div')
for item in itemList:
	try:
		print(item.find('a').string)
	except AttributeError:
		continue
		


