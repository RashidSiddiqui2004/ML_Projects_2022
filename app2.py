
import streamlit as st 
import numpy as np
import sklearn as sns

# import CustomerChurnPred
import app
import creditCard_Rashid
import appDiabetes
import fattyLiverPred
import moodPred
import newsClassifier
import MovieRecommender
import RealmePhonePrice
import pwdStrengthPredictor

usermenu2 = st.sidebar.selectbox("Which model do you want to utilise??",['ML MODELS','DL MODELS','NLP MODELS',"MEDICAL AI Assistants"])

if usermenu2== 'ML MODELS':

    usermenu = st.sidebar.radio("CHOOSE THE ML MODEL TO UTILISE",["CREDIT CARD FRAUD PREDICTOR",
                        "HR INTERVIEW PREDICTOR","CUSTOMER CHURN PREDICTION","REALME PRICE PREDICTOR",
                                                                  "Password Strength Predictor"])

elif usermenu2 == 'NLP MODELS':

    usermenu = st.sidebar.radio("CHOOSE THE NLP MODEL TO UTILISE", ["MOOD PREDICTOR","NEWS CLASSIFIER"])

elif usermenu2 == "MEDICAL AI Assistants":

    usermenu = st.sidebar.radio("CHOOSE THE Medical AI Model To Assist You",["DIABETES PREDICTOR - MEDICAL ASSISTANT","FATTY LIVER DISEASE PREDICTOR"])

else:
    st.sidebar.title("SORRY SIR/MAM, I have only 1 Deep Learning Model")

    st.sidebar.title("You will definitely find more models in your next visit :)")

    usermenu = st.sidebar.radio("CHOOSE THE DL MODEL TO UTILISE", ['MOVIE RECOMMENDER SYSTEM'])

if usermenu== "HR INTERVIEW PREDICTOR":
    app.funcCall()

elif usermenu== "DIABETES PREDICTOR - MEDICAL ASSISTANT":
    appDiabetes.funcCall()

# elif usermenu == "CUSTOMER CHURN PREDICTION":
#     CustomerChurnPred.funcCall()

elif usermenu== "MOOD PREDICTOR":
    moodPred.funcCall()

elif usermenu== "NEWS CLASSIFIER":
    newsClassifier.funccall()

elif usermenu=='MOVIE RECOMMENDER SYSTEM':
    MovieRecommender.funcCall()

elif usermenu == "FATTY LIVER DISEASE PREDICTOR":
    fattyLiverPred.assistUser()

elif usermenu=="REALME PRICE PREDICTOR":
    RealmePhonePrice.assistUser()


elif usermenu == "Password Strength Predictor":
    pwdStrengthPredictor.assistUser()

else:
    creditCard_Rashid.funcCall()

