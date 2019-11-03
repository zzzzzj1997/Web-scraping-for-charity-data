#################'Revenue & Expenses' PART##########
import selenium
import splinter
from splinter import Browser
import csv
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
from selenium import webdriver
driver = webdriver.Firefox(executable_path = r'F:\python\Scripts\geckodriver')
browser = Browser('firefox')

def writeHead(t):
	element = browser.find_by_id('fiscal-year-select').first
	element.select(str(t))
	headers = ['Name','Year']
	num_table = len(driver.find_element_by_xpath('//*[@id="fin-data-revexp-' + str(t) + '"]/div/div').find_elements_by_tag_name("table"))
	for j in range(1, num_table + 1):
		num_row = len(driver.find_element_by_xpath('//*[@id="fin-data-revexp-' + str(t) + '"]/div/div/table[' + str(j) + ']').find_elements_by_tag_name("tr"))
		for i in range(num_row - 2, -1, -1):
			superpath1 = '//*[@id="fin-data-revexp-' + str(t) + '"]/div/div/table[' + str(j) + ']/tbody/tr[last()-' + str(i) + ']/td[1]'
			if j == 3:
				superpath1 = '//*[@id="fin-data-revexp-' + str(t) + '"]/div/div/table[3]/thead/tr[last()-' + str(i) + ']/th[1]'
			head = browser.find_by_xpath(superpath1)
			headers.append(head.value)
	writer.writerow(headers)
def Extract_yearly_asset(t,writer):
	element = browser.find_by_id('fiscal-year-select').first
	element.select(str(t))
	name = browser.find_by_xpath('//*[@class="profile-org-name"]')
	assetdata = [name.value]
	ppyear = '//*[@id="fin-data-revexp-' + str(t) + '"]/div/div/div[2]/span[2]'
	years = browser.find_by_xpath(ppyear)
	assetdata.append(years.value)
	num_table = len(driver.find_element_by_xpath('//*[@id="fin-data-revexp-' + str(t) + '"]/div/div').find_elements_by_tag_name("table"))
	for j in range(1,num_table+1):
		num_row = len(driver.find_element_by_xpath('//*[@id="fin-data-revexp-' + str(t) + '"]/div/div/table['+ str(j) +']').find_elements_by_tag_name("tr"))
		for i in range(num_row-2, -1, -1):
			superpath2 = '//*[@id="fin-data-revexp-'+ str(t) + '"]/div/div/table[' + str(j) + ']/tbody/tr[last()-' + str(i) + ']/td[2]'
			if j ==3:
				superpath2 = '//*[@id="fin-data-revexp-' + str(t) + '"]/div/div/table[3]/thead/tr[last()-' + str(i) + ']/th[2]'
			values = browser.find_by_xpath(superpath2)
			assetdata.append(values.value)
	writer.writerow(assetdata)
f = open('c:\\url.txt', 'r')
with open("reve.csv",'w',encoding='utf-8') as fileout:
	writer = csv.writer(fileout)
	headflag = 0
	i = 0
	for url in f:
		print(url)
		browser.visit(url)
		driver.get(url)
		if headflag ==0:
			writeHead(0)
			headflag = 1
		for i in range(0,22):
			try:
				Extract_yearly_asset(i,writer)
			except:
				print(i)