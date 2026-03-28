from bs4 import BeautifulSoup
import requests
import csv


html_file = requests.get("https://quotes.toscrape.com/").text
soup = BeautifulSoup(html_file,"lxml")
quote = soup.select_one("div.quote")

print(quote)
