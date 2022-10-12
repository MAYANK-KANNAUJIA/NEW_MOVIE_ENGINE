import streamlit as st
import bs4
import urllib.request as url
from PIL import Image

st.title("MOVIE SEARCH ENGINE WEB APPLICATION........")
st.header("WEB APPLICATION USING STREAMLIT.......")
st.sidebar.header("...About me...")
st.sidebar.text('''This web application is designed
 by Mayank Kannaujia , 
 a student of B.Sc(H) electronics,

Sri Aurobindo College,
 University of Delhi''')
st.write(".............................WELCOME TO ALL.......................")
st.text("I would like to sincerely thanks my teachers for organising such a knowledgefull session ")
st.text('''The python addon course give a brief knowledge to the students''')
import datetime as dt
st.date_input("Today is :", dt.datetime.now())
movie_name=st.text_input("ENTER MOVIE NAME:")

if st.button("SEARCH"):
        st.spinner("wait a second....")
        time.sleep(5)
        st.success("SUCCESS")
#movie_name=movie_name.replace(" ","+")
path=f"https://www.imdb.com/search/={movie_name}"
response= url.urlopen(path)
page=bs4.BeautifulSoup(response,"lxml")
titles=page.find("h1",{"class":"sc-b73cd867-0 eKrKux"})
print("TITLE:",titles.text)
rating=page.find("span",{"class":"sc-7ab21ed2-1 jGRxWM"})
print("RATINGS:",rating.text)
st.balloons()