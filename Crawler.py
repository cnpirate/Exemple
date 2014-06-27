# import urllib.request
# from bs4 import BeautifulSoup
# import pickle as p

# webURL = 'http://www.baidu.com' 

# u = urllib.request.urlopen(webURL)
# buffer = u.read()
# print(len(buffer))
# print(u.info())

# soup = BeautifulSoup(buffer)

# f = open("test.html", "w")
# p.dump(soup, f)
# f.close()

import urllib.request
import re
import argparse
from bs4 import BeautifulSoup 
 
class Crawler(object):

	def __init__(self, args):
		self.ns = args.ns

	def _getSoup(self, url):
		req = urllib.request.urlopen(
			url = url)
		content = req.read()
		return BeautifulSoup(content)

	def _isLastPage(self, soup):
		if not soup.find(text=re.compile("End of list.")):
			return False
		else:
			return True

	def _getItem(self, soup):
		itemList = soup.findAll('li')
		for item in itemList:
			print(item.find('a').string)

	def _getNextPage(self, soup):
		nextUrl = 'http://www.sitedossier.com' + soup.ol.nextSibling.nextSibling.get('href')
		self.soup = self._getSoup(nextUrl)

	def start(self):
		url = 'http://www.sitedossier.com/nameserver/' + self.ns
		self.soup = self._getSoup(url)
		self._getItem(self.soup)
		while not self._isLastPage(self.soup):
			self._getNextPage(self.soup)
			self._getItem(self.soup)

def main():
	parser = argparse.ArgumentParser(description='A crawler for sitedossier.com') 
	parser.add_argument('-ns', type=str, required=True, metavar='NAMESERVER', dest='ns', help='Specify the nameserver')
	args = parser.parse_args()

	crawler = Crawler(args)
	crawler.start()

if __name__ == '__main__':
	main()