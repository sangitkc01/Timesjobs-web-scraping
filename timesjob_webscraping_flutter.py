from bs4 import BeautifulSoup
import requests

unfamiliar_skill=input('enter = ')
print(f" Filtering Out {unfamiliar_skill} ")

html_get=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=flutter&txtLocation=").text
soup=BeautifulSoup(html_get,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

for job in jobs:

      Published_date=job.find('span',class_="sim-posted").text
      if 'few' in Published_date:
            Company_name=job.find('h3',class_="joblist-comp-name").text.upper()
            skills=job.find('span',class_="srp-skills").text.replace(" ","")
            more_info=job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                  print(f"Company_Name = {Company_name.strip()}\n")
                  print(f" Skills = {skills.strip()}\n")
                  print(f" More-Info = {more_info}")                  
                  
                  print("")