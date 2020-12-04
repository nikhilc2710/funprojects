# import requests
# from bs4 import BeautifulSoup
# from collections import defaultdict
# import re
# page = requests.get("https://www.sanfoundry.com/engineering-mathematics-questions-answers-laplace-transform-properties-1/")
# soup = BeautifulSoup(page.content, 'html.parser')
# temp=soup.find_all(class_='entry-content')
# arr=temp[0].get_text().splitlines()
# ques=[]
# ans=[]
# options=defaultdict(list)
# for i in arr:
#     # if i:
#     #     print(i)
#     if re.search('^\s*[0-9].',i):
#         ques.append(i)
#     if re.search(r"^[a-z]+\)",i):
#         opt=re.search(r"^[a-z]+\)",i).group(0)
#         options[opt].append(i)
#     if i.replace(' ','').startswith('ViewAnswerAnswer:'):
#         ans.append(i.strip('View AnswerAnswer:'))
    
# # print(list(zip(ques,ans)))
# print(list(zip(ans,range(1,16))))
# print(options['a)'])
import random
s=[{random.randint(1,999):'something'} for _ in range(10)]
for i in s:
    print(i[i.keys()])
