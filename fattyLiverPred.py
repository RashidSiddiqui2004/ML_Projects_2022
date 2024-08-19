
import streamlit as st
import pickle
import numpy as np
import sklearn as sns
import appDiabetes

pipe = pickle.load(open("fattyLiver.pkl", 'rb'))
scaler = pickle.load(open("scalerFattyLiver.pkl", 'rb'))

def getHeight(heig):
    feet = int(heig.split('\'')[0])

    try:
        inches = int(heig.split('\'')[1])
    except:
        inches = 0

    h_m = (feet * 0.3048 + inches * 0.0254)

    return h_m*100

def assistUser():
    st.title("FATTY LIVER PREDICTOR")

    st.title("Here's your personal health check-up, get assured of Fatty-Liver-free life.")

    gender = st.selectbox("Select your Gender", ['M', 'F'])
    age = st.number_input("Please Enter your age (in years)")
    weight = st.number_input("Enter your weight(in kgs)")
    height = st.text_input("What's your height(in feets and inches)")
    futime = st.number_input("Enter your FUTime")
    hdl = st.number_input("What's your HDL(in kgs)")
    cholesterol = st.number_input("What's your Cholesterol level(in )")
    sbp = st.number_input("Enter your SBP Level")
    dbp = st.number_input("Enter DBP")
    fib4 = st.number_input("Enter fib4 SCORE")

    if st.button('Click to get Reports'):

        if gender == 'F':
            gender = 0
        else:
            gender = 1

        bmi = appDiabetes.getBMI(height, weight)

        height = getHeight(height)

        query = [age, gender, height, bmi, futime, hdl, cholesterol, sbp, dbp, fib4]

        query = np.array(query)
        query = query.reshape(1, -1)

        query1 = scaler.transform(query)

        if pipe.predict(query1)[0]:
            txt1 = "You are having Fatty Liver."
            st.title(txt1)
            print("\n")
            st.title("Please follow this link to get info about doctors having expertise in Fatty Liver!!")
            # st.write(
            #     "Link:- [JustDial Fatty Liver Specialist Doctors Near Me site](https://www.justdial.com/Delhi/Diabetologist-Doctors/nct-10892682)")
        else:

            txt2 = 'Congratulations, you are detected free from Fatty Liver :)'
            st.title(txt2)
            # speak(txt2)
            cong = "STAY HAPPY, STAY HEALTHY!"
            st.title(cong)
            # speak(cong)
