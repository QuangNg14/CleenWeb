from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.treehugger.com/"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")    # thu vien 

new_item = []

soup = BeautifulSoup(text, "html.parser")

block = soup.find("section","c-layout__column c-layout__column--rail")
block2 = block.find_all("section","c-block")

for blo in block2 :
  block3 = blo.find_all("article","c-article c-article--summary c-article--numbered")
  for blo1 in block3:
    div = blo1.find("div","c-article__container")
    div1 = div.find("div","c-article__image")
    div2 = div.find("div","c-article__summary")

    div3 = div1.a.img
    div6 = div1.a
    source = url+ div6["href"]

    picture_link = div3["src"]

    div4 = div2.h3
    title = div4.text
    item_content = {
      "picture_link" : picture_link,
      "title": title,
      "source":source

    }
    new_item.append(item_content)

# for pile in block2:
#   pile1 = pile.find_all("article","c-article c-article--summary")
#   for pile2 in pile1:
#     pile3 = pile2.find("div","c-article__container")
#     pile4 = pile3.find("div","c-article__image")
#     pile5 = pile3.find("div","c-article__summary")

#     pile6 = pile4.a
#     picture_link = url+ pile6["href"]

#     pile7 = pile5.h3
#     title = pile7.text
#     pile8 = pile7.a
#     source = url+ pile8["href"]

#     item_content = {
#       "source": source,
#       "picture_link":picture_link,
#       "title":title
#     }
#     new_item.append(item_content)

    

pyexcel.save_as(records = new_item, dest_file_name="treehugger_right_craw.xlsx")

