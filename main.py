from bs4 import BeautifulSoup
import requests
import smtplib

LINK = "https://www.jumia.com.ng/generic-s20-wireless-bluetooth-earphone-touch-led-stereo-audio-black-252700580.html"
my_email = "mzscripterx5@gmail.com"
password = "ndgw loxf bhqi hiyw"
response = requests.get(LINK)
response.raise_for_status
jumia_code = response.text
soup = BeautifulSoup(jumia_code, "html.parser")

price = soup.find(name="span", class_="-b -ubpt -tal -fs24 -prxs")
splited = price.text.split(" ")
splited_f = splited[1].split(",")
cost_s = ""
for i in splited_f:
    cost_s += i
cost = float(cost_s)
print(cost)

if cost <= 7000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Buy the earpod!!\n\nThe price of the earpod is less than 5000, click the link to buy now:\n{LINK}")
        connection.close()