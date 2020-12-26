import requests
from bs4 import BeautifulSoup
from itertools import chain
from multiprocessing import Pool
import sys
def mailfinder(url):
    r=requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    mails = soup.findAll("div", {"class": "city_tab"})
    hotel_ref=[i.find('a',href=True)['href']for i in mails  if "View Email ID" in i.text ]
    return hotel_ref
    
def mailextractor(ref):
    r=requests.get(ref)
    soup = BeautifulSoup(r.text, 'lxml')
    mails = soup.findAll("td", {"class": "table_space_td_right1"})
    return  mails[-1].text.split(',')


if __name__ == "__main__":
    _,url,start,end=sys.argv
    l=[url+f"/pag={i}/" for i in range(int(start),int(end)+1)]
    with Pool(12) as p:
        mp=p.map_async(mailfinder, l).get()
    _hotel_ref=list(chain(*mp))
    with Pool(12) as p:
        mails=p.map(mailextractor, _hotel_ref)
    with open('mail.txt', 'w+') as f:
        for item in mails:
            x=' '.join(item)
            f.write(f'{x}\n')
