import requests
from bs4 import BeautifulSoup
import pandas as pd

url_list = []
for i in range(1,8):
  common_url = f'https://github.com/topics/postgresql?page={i}'     #f stands for format
  url_list.append(common_url)

base_url = 'https://github.com/'
repository_list = []
sr_no = 1
for entry in url_list:
  all_raw_data = requests.get(entry).text
  all_soup = BeautifulSoup(all_raw_data, 'lxml')
  all_entry = all_soup.find_all('article', class_='border rounded color-shadow-small color-bg-subtle my-4')

  for i in all_entry:
      if sr_no>200:
        continue
      else:
        # for extracting names of repositories
        a = i.find('a',class_='text-bold wb-break-word').text
        repository_name = a.strip()
        # for extracting the urls of the repositories
        url = i.find('a', class_='text-bold wb-break-word')['href']
        repository_url = base_url + url
        # for extracting the stars (ratings) of each repositories
        star = i.find('span', class_='Counter js-social-count').text
        # for extracting the usernames of the contributors
        username_str =''
        username = i.find('h3', class_='f3 color-fg-muted text-normal lh-condensed').text.strip()
        username_str += username
        splitted_str = username_str.split(' ')
        user_name = splitted_str[0]
        user_name = user_name.strip()

        repository_page_1 = {
            'Sr_No':sr_no,
            'Repository Name':repository_name,
            'Username':user_name,
            'Star':star,
            'Repository Url':repository_url
        }
        repository_list.append(repository_page_1)
        sr_no+=1 

df = pd.DataFrame(repository_list)
df
