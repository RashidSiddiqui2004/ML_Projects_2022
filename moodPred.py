
import streamlit as st
import pickle
import numpy as np
import sklearn as sns
import  pandas as pd
from PIL import Image

pipe = pickle.load(open("moodPred.pkl",'rb'))
cv = pickle.load(open("cvMood.pkl",'rb'))
import re
def remove_htmlTags(text):

    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)


import string, time
exclude = string.punctuation

def remove_punc(txt):

    return txt.translate(str.maketrans('','',exclude))

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stemmed(text):

    return " ".join([ps.stem(word) for word in text.split()])

def convToModelSecure(text):
    text = remove_punc(remove_htmlTags(stemmed(text))).lower()

    testData = pd.DataFrame({'text': [text]})

    testData = cv.transform(testData['text']).toarray()
    prediction = pipe.predict(testData)

    return prediction[0]

moods= ['anger', 'fear', 'happy', 'joy', 'love', 'sadness', 'surprise']

moodsImg = ['angryjpg.jpg','fearjpg.jpg','happyjpg.jpg','joy.png','love.jpg','sadnessjpg.jpg','surprise.jpg']
def answer(index):

    return  moods[index]

def funcCall():
    st.title("SentimentSense")

    st.text("Introducing SentimentSense: Unlocking Emotions with Precision and Ease")

    st.text("Discover the power of SentimentSense, a cutting-edge sentiment analysis model designed to decipher the true emotions behind every text message. With our advanced machine learning techniques and state-of-the-art algorithms, SentimentSense empowers you to understand user sentiment effortlessly.")

    st.text('''Unleash the Potential:

Harness the insights hidden within text data with unrivaled accuracy and precision.
Gain a deep understanding of user emotions, opinions, and attitudes in real-time.
Seamlessly integrate SentimentSense into your applications, platforms, or customer 
engagement systems.

Unparalleled Performance:

Benefit from meticulously trained models on vast and diverse datasets, including
 Kaggle's sentiment-rich collection.

Leverage advanced natural language processing techniques for
 comprehensive sentiment analysis.
Trust in our model's ability to adapt to various domains, languages, 
and communication styles.''')

    original_title = '<p style="font-family:Fjalla One; color:Blue; font-size: 29px;">I will help you to know the mood/sentiment of the user who has entered/spoke some text/speech.</p>'
    st.markdown(original_title, unsafe_allow_html=True)

    # st.title("I will help you to know the mood/sentiment of the user who has entered/spoke some text/speech.")

    gender = st.selectbox("Select your Gender", ['M', 'F'])

    text = st.text_area("Enter your statement")

    if st.button('Click to get Prediction'):

        pred = convToModelSecure(text)

        st.title("Your mood is {}".format(answer(pred)))

        image = Image.open(moodsImg[pred])

        st.title("Most relatable emoji in your case is")
        st.image(image)
        print("\n")

    st.text('Join the SentimentSense revolution and tap into the emotional pulse of your \naudience. '
        'Unlock the power of sentiment analysis and revolutionize the way \nyou understand and connect with users.')