import csv
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import csv
import time

from selenium.webdriver.common.by import By

driver_path = str(Path("chromedriver").resolve())


def write_csv_file(data):
    with open('computer_data_1.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        fields = ['name', 'description', 'phone', 'address']
        writer.writerow(fields)

        for i in data:
            writer.writerow(i)


def write_csv_file_1(data):
    with open('computer_data_1.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        fields = ['name', 'description', 'phone', 'address']
        writer.writerow(fields)

        for i in data:
            writer.writerow(i)


driver = webdriver.Chrome(executable_path=driver_path)


def main():
    for page in range(1, 35):
        url = F'https://www.yellowpages.com.au/search/listings?clue=Electricians+%26+Electrical+Contractors&locationClue=New+South+Wales&pageNumber={page}'
        driver.get(url)
        tree = driver.page_source
        tree = html.fromstring(tree)
        num = 1
        list = []
        for i in tree.xpath(
                '//div[@class="Box__Div-sc-dws99b-0 iOfhmk MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded"]'):
            phone = i.xpath('.//span[@class="MuiButton-label"]/text()')
            name = i.xpath(
                './/a[@class="MuiTypography-root MuiLink-root MuiLink-underlineNone MuiTypography-colorPrimary"]/h3/text()')
            sub = i.xpath('.//div[@class="Box__Div-sc-dws99b-0 bKFqNV"]/p/text()')
            addr = i.xpath(
                './/div[@class="Box__Div-sc-dws99b-0 cdNnEE"]/div/a/p/text()')
            print(num, phone[1], name[0], sub[0], addr)

            list_1 = [name[0], sub[0], phone[1], addr]

            list.append(list_1)
            num += 1
        write_csv_file(list)
        print(page)
    driver.close()


def computer_data():
    for page in range(1, 27):
        url = F'https://www.yellowpages.com.au/search/listings?clue=Computer+Networking+%26+Installation&locationClue=New+South+Wales&pageNumber={page}'
        driver.get(url)
        tree = driver.page_source
        tree = html.fromstring(tree)
        num = 1
        list = []
        for i in tree.xpath(
                '//div[@class="Box__Div-sc-dws99b-0 iOfhmk MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded"]'):
            phone_val = i.xpath('.//span[@class="MuiButton-label"]/text()')
            name = i.xpath(
                './/a[@class="MuiTypography-root MuiLink-root MuiLink-underlineNone MuiTypography-colorPrimary"]/h3/text()')
            sub = i.xpath('.//div[@class="Box__Div-sc-dws99b-0 bKFqNV"]/p/text()')
            addr = i.xpath(
                './/div[@class="Box__Div-sc-dws99b-0 cdNnEE"]/div/a/p/text()')
            if 'Call' in phone_val:
                phone = phone_val[1]
            else:
                phone = phone_val
            print(num, phone, name[0], sub[0], addr)

            list_1 = [name[0], sub[0], phone, addr]

            list.append(list_1)
            num += 1
        write_csv_file(list)
        print(page)
    driver.close()


def computer_data_true_website():
    for page in range(406,450):
        url = F'https://www.truelocal.com.au/search/computer-and-it-services/new-south-wales?page={page}'
        driver.get(url)
        tree_1 = driver.page_source
        tree = html.fromstring(tree_1)
        time.sleep(5)
        num = 1
        list = []
        value_list = []
        data = []
        h1 = driver.find_elements(By.TAG_NAME, "p")
        h2 = driver.find_elements(By.TAG_NAME, "span")
        ul = driver.find_elements(By.TAG_NAME, "ul")
        li = driver.find_elements(By.TAG_NAME, "li")
        n = 0
        for j in li:
            list_1 = [j.text]
            list.append(list_1)
        for k in list:
            if ' ' in k[0]:
                value_list.append(k)
        for i in value_list:
            n += 1
            if 1 < n < 13:
                # print(i[0].splitlines())
                catag = i[0].splitlines()[0]
                phone = i[0].splitlines()[2]
                addr = i[0].splitlines()[4]
                if i[0].splitlines()[3] == 'OPENING HOURS':
                    name = i[0].splitlines()[5]
                    if 'AM' in i[0].splitlines()[4]:
                        addr = i[0].splitlines()[6]
                else:
                    name = i[0].splitlines()[3]
                print(n, catag, name, phone, addr)
                final_value = [catag, name, phone, addr]
                data.append(final_value)
        print('page No:',page)
        write_csv_file_1(data)
    driver.close()


if __name__ == '__main__':
    computer_data_true_website()
    # computer_data()

    # main()
