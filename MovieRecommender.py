
import streamlit as st
import pickle
import numpy as np
import sklearn as sns
import pandas as pd
from PIL import Image

model = pickle.load(open('movieRecc.pkl','rb'))
# titles = pickle.load(open('titles.pkl','rb'))
dict1 = pickle.load(open('moviesList.pkl','rb'))

helper = pickle.load(open('dictionaryMovie.pkl','rb'))

# import requests
# cover = requests.get('https://www.googleapis.com/books/v1/volumes?q=isbn:0771595158')
# fox = cover.json()
# print(fox)


engl = "qwertyuiopasdfghjklzxcvbnm7894561230.*/-+-()&^%*&$#@!'\{}<>:-"

def isEnglish(st):

    for i in st:
        if i not in engl:
            return 0
    return 1
def recommededMovies(movie):

    movies = sorted(list(enumerate(model[movie])), reverse=True, key=lambda x: x[1])[1:15]

    reccmMovies = []

    for i in movies:
        reccmMovies.append(i[0])

    return reccmMovies

def output(movie):

    listMovies = recommededMovies(helper[str(movie).lower()])
    pos = 1
    helpful = 1
    # string.replace(" ", "")
    for i in listMovies:
        if(isEnglish(dict1['original_title'][i].replace(" ", "")) and helpful <= 6):
            st.text(str(helpful) + ". " + dict1['original_title'][i].upper())
            helpful+= 1

        # st.text(str(pos) + ". " + dict1['original_title'][i].upper())
        pos += 1



def funcCall():
    # st.set_page_config(layout="wide")

    image = Image.open('logoMovie.jpg')
    wallpaper = Image.open('wallpaperMovieRecc.jpg')

    st.image(wallpaper, caption="Rashid's App's Wallpaper ", width=None, use_column_width=None, clamp=False,
             channels="RGB", output_format="auto")
    # filteredImages = [wallpaper]

    # with st.container():
    #     for col in st.columns(1):
    #         col.image(filteredImages, width=300)

    st.title(" MOVIE RECOMMENDER SYSTEM - \n  \t\t\t\t\t By Rashid Siddiqui ")
    st.text("IT Branch, Netaji Subhash University of Technology, N.D.")

    st.image(image, caption=None, width=850, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    label = "Enter your age"

    st.number_input(label, value=15)

    title = '<p style="font-family:sans-serif; color: {}; font-size: 25px;".format(color) > Select the Movie you watched recently</p>'

    st.markdown(title, unsafe_allow_html=True)

    watchedMovie = st.selectbox("", options=titles[0:6000])

    if st.button('Click to get Movie Recommendations :-'):
        output(watchedMovie)