import streamlit as st
import pickle
import numpy as np
import sklearn as sns

cols = pickle.load(open("columnsCustomerchurn.pkl",'rb'))
pipe = pickle.load(open("CustomerChurnModel.pkl",'rb'))
scaler = pickle.load(open("CCPscaler.pkl",'rb'))


def funcCall():
    st.title("Customer Churn Predictor")

    for i in cols:
        st.title(i)
    # st.title("Here's your personal health check-up, get assured of Diabetes-free life.")

    gender = st.selectbox("Select your Gender", ['M', 'F'])

    age = st.number_input("Please Enter your age (in years)")

    CreditScore = st.number_input("CreditScore")

    geography = st.number_input("Enter Customer's country")

    tenure = st.number_input("Tenure ")
    balance = st.number_input("Balance")
    HasCrCard = st.number_input("HasCrCard ?")
    isActMem = st.number_input("Is he/she an active member?")

    EstimatedSalary = st.number_input("Estimated Salary ?")
    Complain = st.selectbox("Has ever Complained?",["Yes","No"])
    Satis_score  =st.number_input(" Satisfaction Score")
    Card_Type = st.selectbox("Card type")
    PointEarned= st.number_input(" Satisfaction Score")

    if st.button('Click to get Result'):

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

        smoking_history = lbl.transform([smoking_history])[0]

        query = [gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]

        query = np.array(query)
        query = query.reshape(1, -1)
        query1 = scaler.transform(query)

        if (pipe.predict(query1)[0]):
            st.title("You are having Diabetes.")
            print("\n")
            st.title("PLease follow this link to get info about doctors having expertise in Diabetes!!")

            st.write(
                "Link:- [JustDial Diabetes Specialist Doctors Near Me site](https://www.justdial.com/Delhi/Diabetologist-Doctors/nct-10892682)")
        else:
            st.title('Congratulations, you are detected free from Diabetes :)')

            st.title("STAY HAPPY, STAY HEALTHY")

funcCall()