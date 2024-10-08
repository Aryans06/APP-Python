from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.worldometers.info/world-population/population-by-country/'

response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
rows=soup.find('table',{'id':'example2'}).find('tbody').find_all('tr')

countries_list=[]

for row in rows:
  dic={}
  
  dic['Country']=row.find_all('td')[1].text
  dic['Population 2024']=row.find_all('td')[2].text
  dic['Land Area']=row.find_all('td')[6].text
  
  countries_list.append(dic)
  
  
  
  
  df=pd.DataFrame(countries_list)
  df.to_excel('countries_data1.xlsx',index=False)