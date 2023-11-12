import requests 
from bs4 import BeautifulSoup 

link = input("Enter link: ")
r = requests.get(link) 

soup = BeautifulSoup(r.content, 'html.parser') 

s = soup.find('pre') 

data = f"""{soup.find('h1').text}


{s.text}
"""

with open(f'{link.split("/")[-1]}.txt', 'w') as tabfile:
    tabfile.write(data)
