# import required files and modules
import requests
from bs4 import BeautifulSoup
import time
# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
# send a request to fetch HTML of the page
response = requests.get('https://www.amazon.in/Lenovo-L22e-20-Monitor-Display-inputs/dp/B07SGDWMCG/ref=sr_1_1?dchild=1&keywords=monitor+lenovo&qid=1595088224&s=electronics&sr=1-1', headers=headers)
# create the soup object
soup = BeautifulSoup(response.content, 'html.parser')
# change the encoding to utf-8
soup.encode('utf-8')
def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  print(price+"₹")

  #converting the string amount to float
  converted_price = float(price[0:5])
  print(converted_price)
  #using strip to remove extra spaces in the title
  print(title.strip())
