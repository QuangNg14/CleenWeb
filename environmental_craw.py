from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
 

# links of title
# for link in links:
# +link+'.html'

url = "https://www.treehugger.com/"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")    # thu vien 


soup = BeautifulSoup(text, "html.parser")


cblockcards = soup.find("div","c-block__cards")

article_news = cblockcards.find_all("article","c-article c-article--card")

# create a list
link_list = []
string = "https://www.treehugger.com/"
pictures_list = []
title_list = []
content_list = []

new_items = []
new_items_eachweb = []
for article in article_news:
  div = article.find("div","c-article__container")
  if div is not None:
    div2 = div.find("div","c-article__summary")
    div3 = div2.h3.a
    title = div3.text 
    link= string + div3["href"]
    link_list.append(link)


for link in link_list:
  item_content2 = {}
  url = link
  connection = urlopen(url)
  raw_data = connection.read()
  text = raw_data.decode("utf-8")
  soup = BeautifulSoup(text, "html.parser")
  
  # web_title = soup.find("header","c-article__header")
  # web_title2 = web_title.h1.string

  primary_content = soup.find("div","c-article__primary-content")
  pictures = primary_content.find_all("div","th_img")
  content1 = primary_content.find_all("p")
  item_content2 = {
      "Web_picture":pictures
  }
  for cont in content1:
    content2 = cont.text 
    # if content2 is not None:
    #   item_content2['content'] = content2
    #   print(item_content2)
    print(content2)
    print("************************")

# df = pd.read_excel('File.xlsx', sheetname='Sheet1')
 
# print("Column headings:")
# print(df.columns)

# pyexcel.save_as(records = content_list, dest_file_name="treehugger_content.xlsx")

	# new_items_eachweb.append(item_content2)

	# for pic in pictures:
  #   pic_link_1 = pic.img
  #   pic_link_2 = pic_link_1["src"]
  #   item_content3 = {
  #       "Content_side_picture_link" : pic_link_2 
  #     }
  #   new_items_eachweb.append(item_content3)








