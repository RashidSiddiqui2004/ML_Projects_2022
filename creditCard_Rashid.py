
import streamlit as st
import pickle
import numpy as np
import sklearn as sns

df = pickle.load(open("dataset.pkl",'rb'))
pipe = pickle.load(open("modelCreditCard.pkl",'rb'))

df1 = pickle.load(open("datasetIntCC.pkl",'rb'))

def funcCall():
    st.title("Credit Card Issuer - API")

    checking_status = st.selectbox(" Checking Status: ", df1['checking_status'].unique())

    duration = st.selectbox("Duration", df1['duration'].unique())

    credit_history = st.selectbox(" Credit History : ", df1['credit_history'].unique())

    purpose = st.selectbox("Purpose", df1['purpose'].unique())

    credit_amount = st.number_input("Enter credits(in Rs.)")

    savings_status = st.selectbox("Savings status:", df1['savings_status'].unique())

    employment = st.selectbox("Employment ", df1['employment'].unique())
    foreign_worker = st.selectbox("Is the customer a foreign worker ?", ["Yes", "No"])
    personal_status = st.selectbox("Personal Status of the customer", df1["personal_status"].unique())
    residence_since = st.selectbox("Residence_since", df1["residence_since"].unique())
    job = st.selectbox("Job of the customer ", df1['job'].unique())
    num_dependents = st.selectbox("Num of dependents in the family?", df1['num_dependents'].unique())
    age = st.number_input("Enter customer's age(in years) ")
    own_telephone = st.selectbox("Does the customer own a telephone ?", ["Yes", "No"])

    # ,installment_commitment,property_magnitude,,
    # ,,existing_credits,,,

    if st.button('Predict whether to give Credit Card or Not'):

        # st.title("Output: Yes, you should give the credit card to this user..")

        if repeat_retailer == "Yes":
            repeat_retailer = 1
        else:
            repeat_retailer = 0

        if used_chip == "Yes":
            used_chip = 1
        else:
            used_chip = 0

        if used_pin_number == "Yes":
            used_pin_number = 1
        else:
            used_pin_number = 0

        if online_order == "Yes":
            online_order = 1
        else:
            online_order = 0

        query = np.array([distance_from_home, distance_last_trn, ratio_to_median_purchase_price, repeat_retailer,
                          used_chip, used_pin_number, online_order])

        query1 = query.reshape(1, 7)

        if (pipe.predict(query1)[0]):
            st.title("Fraud: Yes")

            print("\n")
            st.title("Please click this link to file an FIR against the person/organisation involved!!")

            # st.title("https://cybercrime.gov.in/")

            st.write("Link:- [Cyber safety site](https://cybercrime.gov.in/)")
        else:
            st.title('Fraud: No')
            st.title("Feel safe to go ahead with the payment:)")