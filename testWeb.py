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

# import urllib.request
# import re
# import argparse
# from bs4 import BeautifulSoup 

# webURL = "http://www.bplisn.net.cn/"
# u = urllib.request.urlopen(webURL)
# content = u.read()
# soup = BeautifulSoup(content)

# itemList = soup.find_all(div=re.compile("读者卡号".encode("utf-8")))
# for item in itemList:
	# try:
		# print(item.string)
	# except AttributeError:
		# continue
		
import smtplib

ser = smtplib.SMTP()
ser.set_debuglevel(1)
ser.connect("smtp.qq.com")


