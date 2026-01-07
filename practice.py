import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self,url):
        self.url=url
        self.user_agent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
        self.response=requests.get(url=self.url,headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response , "lxml")
    def product_title(self):
        title = self.soup.find("span",{"class":"LMizgS"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found"
    def product_price(self):
        price = self.soup.find("div",{"class":"hZ3P6w bnqy13"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag Not Found"



device= PriceTracer("https://www.flipkart.com/apple-iphone-16-black-128-gb/p/itmb07d67f995271?pid=MOBH4DQFG8NKFRDY&lid=LSTMOBH4DQFG8NKFRDYNBDOZI&marketplace=FLIPKART&q=iphone+16&store=tyy%2F4io&spotlightTagId=default_BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=0e3a5bda-09cd-460a-afcb-5b3330075e11.MOBH4DQFG8NKFRDY.SEARCH&ppt=sp&ppn=sp&ssid=8nztyzcag00000001767763261285&qH=9ea15d2374058112")
print(device.product_title())
print(device.product_price())

