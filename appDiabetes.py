import streamlit as st
import pickle
import numpy as np
import sklearn as sns
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    # engine.runAndWait()

df = pickle.load(open("datasetDiabetes.pkl",'rb'))
pipe = pickle.load(open("DiabetesPrediModel.pkl",'rb'))
scaler = pickle.load(open("scalerDiab.pkl",'rb'))
lbl = pickle.load(open("labelTrf.pkl",'rb'))


def getBMI(heig, weight):
    feet = int(heig.split('\'')[0])

    try:
        inches = int(heig.split('\'')[1])
    except:
        inches = 0

    h_m = (feet * 0.3048 + inches * 0.0254)

    bmi = weight / (h_m * h_m)

    return bmi

def funcCall():
    st.title("DIABETES PREDICTOR")
    st.title("Here's your personal health check-up, get assured of Diabetes-free life.")

    gender = st.selectbox("Select your Gender", ['M', 'F'])

    age = st.number_input("Please Enter your age (in years)")

    hypertension = st.selectbox("Are you suffering from Hypertension ?", ["Yes,I am.", 'No, I am not.'])

    heart_disease = st.selectbox("Do you have any heart disease?", ["Yes,I am.", 'No, I am not.'])

    smoking_history = st.selectbox("Do you have any smoking history ?",
                                   ['never', 'No Info', 'current', 'former', 'ever', 'not current'])

    weight = st.number_input("What's your weight(in kgs)")

    height = st.text_input("What's your height(in feets and inches)")
    # height2 = st.number_input("What's your height(in inches)")

    HbA1c_level = st.number_input("Enter your HbA1c Level")

    blood_glucose_level = st.number_input("Enter Blood Glucose Level (Range 70-340)")

    if st.button('Click to get Reports'):

        if gender == 'F':
            gender = 0
        else:
            gender = 1

        if hypertension == "Yes,I am.":
            hypertension = 1
        else:
            hypertension = 0

        if heart_disease == "Yes,I am.":
            heart_disease = 1
        else:
            heart_disease = 0

        bmi = getBMI(height,weight)

        smoking_history = lbl.transform([smoking_history])[0]

        query = [gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]

        query = np.array(query)
        query = query.reshape(1, -1)
        query1 = scaler.transform(query)

        if (pipe.predict(query1)[0]):
            txt1 = "You are having Diabetes."
            st.title(txt1)
            speak(txt1)
            print("\n")
            st.title("Please follow this link to get info about doctors having expertise in Diabetes!!")

            st.write(
                "Link:- [JustDial Diabetes Specialist Doctors Near Me site](https://www.justdial.com/Delhi/Diabetologist-Doctors/nct-10892682)")
        else:

            txt2 = 'Congratulations, you are detected free from Diabetes :)'
            st.title(txt2)
            speak(txt2)
            cong = "STAY HAPPY, STAY HEALTHY"
            st.title(cong)
            speak(cong)