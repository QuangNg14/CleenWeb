import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from mlab import *
from models.classModels import *

connect()
df = pd.read_excel('treehugger.xlsx', sheet_name='pyexcel_sheet1')
# print(df)
for i in range(0, len(df)):  
  post = Post(
    author = df['Author Name'][i],
    author_pic = df['Author Pic'][i],
    date = df['Date'][i],
    link = df['Link'][i],
    picture_link = df['Picture'][i],
    picture_type = df['Picture Type'][i],
    title = df['Title'][i],
    Title_post = df['Each_Web_Title'][i],
    author_name = df['author_name'][i],
    author_link = df['author_link'][i],
    Time = df['Time'][i],
    author_pic_small = df['author_pic_small'][i],
    Content = df['Content'][i],
    status = ' '
  )


  post.save()

