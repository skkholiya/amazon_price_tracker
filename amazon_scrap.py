import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B085J1PFYB/ref=pd_sbs_1?pd_rd_w=CxIpV&pf_rd_p=99c630ba-ffa4-4940-9542-3945145447d6&pf_rd_r=2QVZ4D4SJ6NH7ANJT2NJ&pd_rd_r=faa24b4a-29d5-45b4-8a64-fb153cec35aa&pd_rd_wg=rhiyF&pd_rd_i=B085J1PFYB&psc=1"

headers = {
"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'
}

def check_price():
  page = requests.get(url, headers = headers);
  soup = BeautifulSoup(page.content, 'html.parser');
  #getting phone name
  title = soup.find(id="productTitle").get_text().strip();
  #price of phone
  price_str = soup.find(id="priceblock_ourprice").get_text().strip();
  #converted to integer
  converted_price = "".join([element for element in price_str if element.isdigit()])

  actual_price = float(converted_price[0:5])
  excepted_price_rupees = 36999.0

  #checking if price is less than or equal to what you want.
  if actual_price <= excepted_price_rupees:
    send_mail();
    print("Message Sent.")
 
 
def send_mail():
	server = smtplib.SMTP("smtp.gmail.com",587);
	server.ehlo();
       #Starting TLS Security
	server.starttls();
	server.ehlo();  
	
	#your mail and password
	server.login("xyz@gmail.com","mremckosdjpbwmab")
	
	#subject of mail
	subject = "Price fell down"
	
	#message to be sent.
	body = "Check the amazon link. https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B085J1PFYB/ref=pd_sbs_1?pd_rd_w=CxIpV&pf_rd_p=99c630ba-ffa4-4940-9542-3945145447d6&pf_rd_r=2QVZ4D4SJ6NH7ANJT2NJ&pd_rd_r=faa24b4a-29d5-45b4-8a64-fb153cec35aa&pd_rd_wg=rhiyF&pd_rd_i=B085J1PFYB&psc=1"
	
	#message containing subject and body
	msg = f"Subject: {subject} \n\n {body}";
	
	# your-mail, reciver-mail, message
	server.sendmail("xyz@gmail.com","xyz@outlook.com",msg);
	
	print("Email Has Been Sent.");


check_price();
  
  


