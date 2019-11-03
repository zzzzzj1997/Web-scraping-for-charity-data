import selenium
import splinter
from splinter import Browser
import csv
import sys
from selenium import webdriver
driver = webdriver.Firefox(executable_path = r'F:\python\Scripts\geckodriver')
browser = Browser('firefox')
'''
###########STEP1 GET THE URLS OF RATING PAGES##########
f = open('c:\\Users\\Administrator\\url.txt', 'r')# url of the search results
with open("rating_url.csv",'w',encoding='utf-8') as fileout:
	writer = csv.writer(fileout)
	for url in f:
		driver.get(url)
		div = driver.find_elements_by_xpath('//*[@class="charity-name-desktop"]')
		for j in div:
			a = j.find_element_by_tag_name('a')
			href = a.get_attribute('href')
			writer.writerow(href)
######After this, I use excel to replace 'summary' with 'history' in the links to create history_page_url and save them into 'uu.txt'.(Save the 'click'.)
######If you don't have names of the list of charities,then can use this to extract names from search result page:
	names = browser.find_by_xpath('//*[@class="charity-name-desktop"]')
	for j in names:
		obj = [j.value]
'''
##########STEP2 SAVE THE HISTORICAL RATINGS########
def rat():
	name = browser.find_by_xpath('//*[@class="charityname"]')
	h = [name.value]
	y = ['name']
	r = h
	print(h)
	num_row = len(driver.find_element_by_xpath('//*[@id="summary"]/div[2]/div/div/table/tbody').find_elements_by_tag_name("tr"))
	for i in range(num_row - 2, -1, -1):
		try:
			yearpath = '//*[@id="summary"]/div[2]/div/div/table/tbody/tr[last()-' + str(i) + ']/td[1]'
			ratingpath = '//*[@id="summary"]/div[2]/div/div/table/tbody/tr[last()-' + str(i) + ']/td[3]'
			try:
				div = driver.find_elements_by_xpath(yearpath)
				for j in div:
					a = j.find_element_by_tag_name('a')
			except:
				year = browser.find_by_xpath(yearpath)
				y.append(year.value)
				rating = browser.find_by_xpath(ratingpath)
				r.append(rating.value)
		except:
			print(i)
	writer.writerow(y)
	writer.writerow(r)
f = open('c:\\Users\\Administrator\\uu.txt', 'r')
with open("rating_data3.csv",'w',encoding='utf-8') as fileout:
	writer = csv.writer(fileout)
	for url in f:
		browser.visit(url)
		driver.get(url)
		rat()