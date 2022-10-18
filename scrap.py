import csv
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import csv

driver_path = str(Path("chromedriver").resolve())


def write_csv_file(data):
    with open('results.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        fields = ['name', 'description', 'phone', 'address']
        writer.writerow(fields)

        for i in data:
            writer.writerow(i)


def main():
    driver = webdriver.Chrome(executable_path=driver_path)
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


main()
