from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.treehugger.com/"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")    # thu vien 


soup = BeautifulSoup(text, "html.parser")


cblockcards = soup.find("div","c-block__cards")

article_news = cblockcards.find_all("article","c-article c-article--card")

hot_news_all = soup.find("section","c-layout__column c-layout__column--rail")

hot_news = hot_news_all.find_all("section","c-block")


# create a list
link_list = []
string = "https://www.treehugger.com/"
pictures_list = []
title_list = []

new_items = []
new_items2 = []
picture_type = []
text_content = []
for article in article_news:
    div = article.find("div","c-article__container")
    if div is not None:
        div2 = div.find("div","c-article__summary")
        div3 = div2.h3.a
        title = div3.text 
        link= string + div3["href"]
        link_list.append(link)
        

        div4 = div.find("div","c-article__image")
        div5 = div4.a.img
        picture = div5["src"]
        
        
        div6 = div2.find("div","c-article__category")
        pic_type = div6.a.text

        div7 = div2.find("div","c-article__byline")
        author_pic = div7.img
        author_pic_link = author_pic["src"]

        div8 = div2.find("span")
        div9 = div8.a.text 
        author_content = "By " + div9

        div10 = div8.find("a","c-article__published")
        date = div10.text


        item_content = {
                "Title" : title,
                "Link"  : link,
                "Picture" : picture,
                "Picture Type": pic_type,
                "Author Pic": author_pic_link,
                "Author Name": author_content,
                "Date":date                
            }
        new_items.append(item_content)

# for links in link_list:
#   item_content2 = {}
#   url = links
#   connection = urlopen(url)
#   raw_data = connection.read()
#   text = raw_data.decode("utf-8")
#   soup1 = BeautifulSoup(text, "html.parser")
  
#   # web_title = soup1.find("header","c-article__header")
#   # web_title2 = web_title.h1.string
#   primary_content = soup1.find("div","c-article__primary-content")
#   pictures = primary_content.find_all("div","th_img")
#   content1 = primary_content.find_all("p")
#   # item_content2 = {
#   #     "Web_picture":pictures
#   # }
#   for cont in content1:
#     content2 = cont.text
#     item_content2 = {
#       "content" : content2
#     }
#     new_items2.append(item_content2)
for hot in hot_news:
  hot_news_2 = hot.find_all("article","c-article c-article--summary c-article--numbered")
  for hot1 in hot_news_2:
    hot_news_3 = hot1.find("div","c-article__container")
    
    hot_news_4 = hot_news_3.find("div","c-article__image")
    hot_news_5 = hot_news_3.find("div","c-article__summary")
    hot_news_6 = hot_news_4.a
    
    hot_news_7 = hot_news_5.find("h3","c-article__headline")
    hot_news_8 = hot_news_7.a
    hotnew_link = "https://www.treehugger.com/" + hot_news_8["href"]
    hotnew_content = hot_news_8.text

    hot_news_9 = hot_news_4.a.img
    hotnew_image = hot_news_9["src"]

    item_content2 = {
      "HotNewImage":hotnew_image,
      "HotNewLink":hotnew_link,
      "HotNewContent":hotnew_content
    }
    
    new_items2.append(item_content2)

pyexcel.save_as(records = new_items, dest_file_name="treehugger.xlsx")
# pyexcel.save_as(records = new_items2, dest_file_name="treehugger2.xlsx")

