from bs4 import BeautifulSoup
import requests
import csv
import textwrap

with open("quotes.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote","Author","Tags","Birth Date","Birth Location"])

    html_file = requests.get("https://quotes.toscrape.com/").text
    soup = BeautifulSoup(html_file,"lxml")
    quotes = soup.select("div.quote")

    for quote in quotes:
        title = quote.select_one("span.text").text.strip()
        wrapped = textwrap.fill(title, width=40)
        author_name = quote.select_one("small.author").text.strip()
        tags = [tag.text for tag in quote.select("a.tag")]


        author_link = quote.select_one("a")["href"]
        full_link = "https://quotes.toscrape.com/"+ author_link

        author_html = requests.get(full_link).text
        author_soup = BeautifulSoup(author_html,"lxml")

        author_dob = author_soup.select_one("span.author-born-date").get_text()
        author_location = author_soup.select_one("span.author-born-location").get_text()
        
        
        writer.writerow([title, author_name,  ", ".join(tags) , author_dob, author_location])