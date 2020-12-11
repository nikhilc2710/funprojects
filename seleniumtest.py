import time
from selenium import webdriver
import traceback as tb
import time
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
l=["secretonlyiknow"]
for i in range(2,6):
    l+=[f"secretonlyiknows"]
megalist=[]
for xx in l:
    driver.get(xx)
    elems = driver.find_elements_by_css_selector(".city_tab [href]")
    try:
        for index,i in enumerate( elems):
            if "View Email ID" in i.text:
                x=i.get_attribute('href')
                r=requests.get(x)
                soup = BeautifulSoup(r.text, 'html.parser')
                mails = soup.findAll("td", {"class": "table_space_td_right1"})
                megalist.append( mails[-1].text.split())
    except:
        pass
with open('your_file.txt', 'w+') as f:
    for item in megalist:
        if len(item)>1:
            x=" ".join(item)
            f.write(f'{x}\n')
        else:
            f.write(f'{item}\n')
driver.quit()

# woodrange2@gmail.com
# justpython@1