"""
	Script to scrape a page of Shopping.com.
	if only keyword is given the script will give the number of total items available at sopping.com for that specific keyword.
	if along with keyword page number is also given, the script will return information of all the products in that specific page for that
	specific keyword.
	if you want to give space separated keywords please wrap them in quotes.

	Usage : python problem2.py <keyword> <page>
"""
import urllib2
from bs4 import BeautifulSoup
import sys

page = ""
keyword = ""
pageset = False

sys.argv.append("something") #appneding some string to judge whether command line arguments are provided or not

if sys.argv[1] != "something":
	keyword = "?KW=" + sys.argv[1]
else:
	print "No Argument Provided!"
	exit() 
if sys.argv[2] != "something":
	page = "~PG-" + sys.argv[2]
	pageset = True

url = "http://www.shopping.com/products" + page + keyword 

resp = urllib2.urlopen(url)
respHtml = resp.read()
soup = BeautifulSoup(respHtml, "html5lib")  #initializing soup object using html5lib parser

if pageset:  # if-else for judging whether we have to find product details or no. of products
	products = soup.find_all('div', {'class' : 'gridBox deal  '})  #getting all the products from DOM.
	productDetails = []
	for product in products:
		temp = {}
		if product.find('a', {'class' : 'productName '}) is not None:
			if product.find('a', {'class' : 'productName '}).find('span') is not None:
				temp['title'] = product.find('a', {'class' : 'productName '}).find('span')['title']
		if product.find('span', {'class' : 'productPrice'}) is not None:
			temp['price'] = product.find('span', {'class' : 'productPrice'}).getText().strip()
		if product.find('a', {'class' : 'newMerchantName'}) is not None:
			temp['merchant'] = product.find('a', {'class' : 'newMerchantName'}).getText().strip()
		if product.find('div', {'class' : 'taxShippingArea'}) is not None:
			temp['shipping'] = product.find('div', {'class' : 'taxShippingArea'}).getText().strip()
		productDetails.append(temp)
	i = 1
	for productDetail in productDetails:
		print "-------------------------------\n          PRODUCT " + str(i) + "          \n-------------------------------"
		for productDetailTitle, ProductDetailResult in productDetail.iteritems():
			print productDetailTitle + " : " + ProductDetailResult
		i+=1
else:
	if soup.find('span', {'class' : 'numTotalResults'}) is not None:
		totalCount = soup.find('span', {'class' : 'numTotalResults'}).getText().strip()
		totalCount = totalCount.split(' of ')[-1].strip()
		print "Total Products : " + str(totalCount)
	else:
		print "Result Not Found!"



