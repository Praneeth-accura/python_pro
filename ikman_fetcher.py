from bs4 import BeautifulSoup
import json
import logging
import requests

url = 'https://ikman.lk/en/ads?by_paying_member=0&sort=relevance&buy_now=0&query=bmw&page=1'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
logging.basicConfig(filename='app.log', level=logging.INFO)

def get_title(add_list):
    try:
        return add_list.find('span', attrs={"class": "title--3yncE"}).text.encode('utf-8')
    except Exception as e:
        logging.error('Error occurred ' + str(e))


def get_price(add_list):
    try:        
        return add_list.find('div', attrs={"class": "price--3SnqI color--t0tGX"}).text.encode('utf-8')
    except Exception as e:
        logging.error('Error occurred ' + str(e))


def get_decription(add_list):
    try:       
        return add_list.find('div', attrs={"class": "description--2-ez3"}).text.encode('utf-8')
    except Exception as e:
       logging.error('Error occurred ' + str(e))


def get_objetc_details():
    object_list = []
    try:
      for add_list in content.findAll('div', attrs={"class": "container--2uFyv"}):
          list = {
              "title": get_title(add_list),
              "price": get_price(add_list),
              "short_decription":  get_decription(add_list),
          }
          object_list.append(list)
      return object_list
    except Exception as e:
          logging.error('Error occurred ' + str(e))


print(get_objetc_details())
# with open('data.json', 'w', encoding='utf-8') as f:
#   json.dump(get_objetc_details(), f, ensure_ascii=False, indent=4)
