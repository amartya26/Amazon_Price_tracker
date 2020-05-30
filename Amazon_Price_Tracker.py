import requests as re
from bs4 import BeautifulSoup as bs
import smtplib
import time

URL = 'https://www.amazon.in/BassHeads-152-Secure-Braided-Earphones/dp/B07KY3K2YG/ref=pd_rhf_sc_p_img_7?_encoding=UTF8&psc=1&refRID=A7EG3ZHAFEKQJAZMHHSF'

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
def check_price():
    page = re.get(URL, headers= headers)

    soup = bs(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find( id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if(converted_price < 499):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 499):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vermaamartya0226@gmail.com', 'yrprldhxjaogwiey')

    subject= 'The Price of Boat earphones Fell down'
    body = "ChecK the Amazon link: https://www.amazon.in/BassHeads-152-Secure-Braided-Earphones/dp/B07KY3K2YG/ref=pd_rhf_sc_p_img_7?_encoding=UTF8&psc=1&refRID=A7EG3ZHAFEKQJAZMHHSF "
    
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail (
        "vermaamartya0226@gmail.com",
        "hofferalex755@gmail.com",
        msg)
    print("Hey Mail has Been Sent!!")
    server.quit()

while(True):
    
    check_price()
    time.sleep(60*60*12)