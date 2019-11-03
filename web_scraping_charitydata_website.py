import selenium
from splinter import Browser
import csv
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
from selenium import webdriver
driver = webdriver.Firefox(executable_path = r'geckodriver')
browser = Browser('firefox')

def Extract_Items():
    url = 'https://www.charitydata.ca/charity/next-canada/815198403RR0001/'
    browser.visit(url)
    driver.get(url)
    driver.implicitly_wait(10)
    num_row = len(driver.find_element_by_xpath('//*[@class="assets print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    row = []
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="financial"]/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    browser.find_by_xpath("//a[@href='#liabilities']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="liabilities print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="liabilities print"]/div/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    browser.find_by_xpath("//a[@href='#revenue']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="revenue print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="revenue print"]/div/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    browser.find_by_xpath("//a[@href='#expenditures']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="expenditures print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="expenditures print"]/div/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    num_row = len(driver.find_element_by_xpath('//*[@class="expenditures print"]/div[2]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="expenditures print"]/div[2]/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    browser.find_by_xpath("//a[@href='#employees']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="employees print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="employees print"]/div/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    num_row2 = len(driver.find_element_by_xpath('//*[@class="employees print"]/div[2]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row2-1, -1, -1):
        superpath = '//*[@class="employees print"]/div[2]/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    browser.click_link_by_text('Fundraising')
    num_row = len(driver.find_element_by_xpath('//*[@class="fundraising print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        if i == 47 or i == 24 or i == 15:
            continue
        else:
            superpath = '//*[@class="fundraising print"]/div/table/tbody/tr[last()-' + str(i) + ']/th'
            assets = browser.find_by_xpath(superpath)
            row.append(assets.value)
    browser.find_by_xpath("//a[@href='#programs']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="programs print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="programs print"]/div/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    num_row2 = len(driver.find_element_by_xpath('//*[@class="programs print"]/div[2]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row2-1, -1, -1):
        superpath = '//*[@class="programs print"]/div[2]/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    num_row3 = len(driver.find_element_by_xpath('//*[@class="programs print"]/div[3]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row3-1, -1, -1):
        superpath = '//*[@class="programs print"]/div[3]/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    num_row4 = len(driver.find_element_by_xpath('//*[@class="programs print"]/div[4]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row4-1, -1, -1):
        superpath = '//*[@class="programs print"]/div[4]/table/tbody/tr[last()-' + str(i) + ']/th'
        assets = browser.find_by_xpath(superpath)
        row.append(assets.value)
    writer.writerow(row)

def Extract_yearly_asset(t,writer):
#    superpath = '//*[@class="overview"]/div/h2'
#    n = browser.find_by_xpath(superpath)
    name = []
    num_row = len(driver.find_element_by_xpath('//*[@class="assets print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="financial"]/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)

#def Extract_yearly_liabilities(t):
    browser.find_by_xpath("//a[@href='#liabilities']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="liabilities print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="liabilities print"]/div/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
#def Extract_yearly_revenue(t):
    browser.find_by_xpath("//a[@href='#revenue']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="revenue print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="revenue print"]/div/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
#def Extract_yearly_expenditures(t):
    browser.find_by_xpath("//a[@href='#expenditures']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="expenditures print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="expenditures print"]/div/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
    num_row = len(driver.find_element_by_xpath('//*[@class="expenditures print"]/div[2]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="expenditures print"]/div[2]/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
#def Extract_yearly_employees(t):
    browser.find_by_xpath("//a[@href='#employees']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="employees print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="employees print"]/div/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
    num_row2 = len(driver.find_element_by_xpath('//*[@class="employees print"]/div[2]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row2-1, -1, -1):
        superpath = '//*[@class="employees print"]/div[2]/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
#def Extract_yearly_Fundraising(t):

    browser.click_link_by_text('Fundraising')
    num_row = len(driver.find_element_by_xpath('//*[@class="fundraising print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        if i == 47 or i == 24 or i == 15:
            continue
        else:
            superpath = '//*[@class="fundraising print"]/div/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
            assets = browser.find_by_xpath(superpath)
            name.append(assets.value)
#def Extract_yearly_programs(t):
    browser.find_by_xpath("//a[@href='#programs']").click()
    num_row = len(driver.find_element_by_xpath('//*[@class="programs print"]/div/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row-1, -1, -1):
        superpath = '//*[@class="programs print"]/div/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
    num_row2 = len(driver.find_element_by_xpath('//*[@class="programs print"]/div[contains(.,"Foreign Activities")]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row2-1, -1, -1):
        superpath = '//*[@class="programs print"]/div[contains(.,"Foreign Activities")]/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
    num_row3 = len(driver.find_element_by_xpath('//*[@class="programs print"]/div[contains(.,"Are any projects undertaken")]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row3-1, -1, -1):
        superpath = '//*[@class="programs print"]/div[contains(.,"Are any projects undertaken")]/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
    num_row4 = len(driver.find_element_by_xpath('//*[@class="programs print"]/div[contains(.,"Political Activities")]/table[1]/tbody').find_elements_by_tag_name("tr"))
    for i in range(num_row4-1, -1, -1):
        superpath = '//*[@class="programs print"]/div[contains(.,"Political Activities")]/table/tbody/tr[last()-' + str(i) + ']/td['+ str(t) +']'
        assets = browser.find_by_xpath(superpath)
        name.append(assets.value)
    writer.writerow(name)

f = open('urls.txt', 'r')
with open("Charity2009.csv",'w',encoding='utf-8') as fileout:
    writer = csv.writer(fileout)
    Extract_Items()
    for url in f:
        browser.visit(url)
        driver.get(url)
        Extract_yearly_asset(9,writer)