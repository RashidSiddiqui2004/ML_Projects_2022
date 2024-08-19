import streamlit as st
import pickle
import numpy as np
import sklearn as sns
import pandas as pd
import re
from PIL import Image

image = Image.open('logoNews.jpg')

# st.image(image, caption='News Classifier API')

image2 = Image.open('nlp.jpg')

# st.image(image2)
imageBtm = Image.open('nlpLast.jpg')
img3= Image.open('nlp2.jpg')
#
filteredImages = [image, image2]

filteredImages2 = [imageBtm,img3]

def remove_htmlTags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)


import string, time

exclude = string.punctuation


def remove_punc(txt):
    return txt.translate(str.maketrans('', '', exclude))



def remove_urls(text):
    pattern = re.compile(r'https?://s+/www\.www\.\s+')
    return pattern.sub(r'', text)

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stemmed(text):

    return " ".join([ps.stem(word) for word in text.split()])

predictor = pickle.load(open("disasterPredictor.pkl", 'rb'))
cv = pickle.load(open('cvNews.pkl', 'rb'))

def convToModelSecure(news):
    news = remove_punc(remove_urls(remove_htmlTags(stemmed(news)))).lower()

    testData = pd.DataFrame({'text': [news]})

    testData = cv.transform(testData['text']).toarray()
    prediction = predictor.predict(testData)

    if (prediction[0] == 1):
        return  1
        # return "This news is related to a disaster!! :("
    else:
        return 0
        # return "This news is not related to a disaster :)"


def funccall():

    with st.container():
        for col in st.columns(1):
            col.image(filteredImages, width=270)

    st.title(" NEWS CLASSIFIER (NLP Project)- \n  \t\t\t\t\t\t\t By Rashid Siddiqui ")
    st.text("IT Branch, Netaji Subhash University of Technology, N.D.")

    # st.camera_input("click pic")
    # st.image(image, channels="BGR") -> to insert images in Web-app

    new_title = '<p style="font-family:sans-serif; color:orange; font-size: 30px;">This website helps you to know whether the inputted news feed is a disaster or not.</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    st.text("What is Disaster according to me ?")

    new_title1 = '<p style="font-family:sans-serif; color:black; font-size: 20px;">Any news related to natural disasters(earthquakes, tsunamis, floods, etc.), crimes, harassment, violence, etc.</p>'
    st.markdown(new_title1, unsafe_allow_html=True)
    # st.text("Any news related to natural disasters(earthquakes, tsunamis, floods, etc.), crimes, harassment, violence, etc.")

    name = st.text_input("Enter your name: ")

    news = st.text_area(label="PLease enter the news below:-", placeholder="Please feed the news here..", height=400)

    # st.text_area("News input form", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

    if st.button('Submit to know about the news'):

        pred = convToModelSecure(news)
        titleForRed = '<p style="font-family:sans-serif; color:red; font-size: 30px;">OMG! This news is related to a disaster!! :(</p>'

        titleForBlue = '<p style="font-family:sans-serif; color:blue; font-size: 30px;">Relax, This news is not  related to a disaster!! :) </p>'

        if (pred == 1):
            st.markdown(titleForRed, unsafe_allow_html=True)
        else:
            st.markdown(titleForBlue, unsafe_allow_html=True)
        # st.title(convToModelSecure(news))

    # st.image(imageBtm)
    with st.container():
        for col in st.columns(1):
            col.image(filteredImages2, width=270)


