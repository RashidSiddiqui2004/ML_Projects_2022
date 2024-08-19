import pandas as pd
import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open("pwdStrengthPredictor.pkl", 'rb'))


def getDiffFeatures(password):
    # frequency of chars, digits, symbols, mixture, pattern

    num_smallchars, num_bigchars, num_digits, num_specl = 0, 0, 0, 0

    symbols = ['@', '#', '$', '%', '^', '&', '*', ':', ';', '>', '<', '~', '!', '(', ')']

    for i in password:
        if 'a' <= i <= 'z':
            num_smallchars += 1
        elif 'A' <= i <= 'Z':
            num_bigchars += 1
        elif '0' <= i <= '9':
            num_digits += 1
        elif i in symbols:
            num_specl += 1

    return num_smallchars, num_bigchars, num_digits, num_specl


import re


def is_easy_to_crack(password):
    # Criteria 1: Password consists of a single letter or digit
    if len(password) == 1 and password.isalnum():
        return 0

    # Criteria 2: Password consists of consecutive numbers or alphabets
    consecutive_patterns = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba']
    for pattern in consecutive_patterns:
        if password.lower() in pattern:
            return 1

    for i in range(len(password) - 1):
        if password[i] != password[i + 1]:
            return 2

    return 0


def getStrength(password):
    features = getDiffFeatures(password)
    is_easy = is_easy_to_crack(password)

    df_test = pd.DataFrame({
        'num_smallchars': features[0], 'num_bigchars': features[1],
        'num_digits': features[2], 'num_specl': features[3], 'is_easy_to_crack': is_easy
    }, index=[0])

    predStrength = pipe.predict(df_test)

    return predStrength


def assistUser():

    st.title('SecurePassMeter -Password Strength Checker')

    st.markdown(
        '<p style="color: green;font-size:30px;text-align:center;font-weight:700;">Developed By- Rashid Siddiqui</p>',
        unsafe_allow_html=True)


    st.markdown(
        "Are your passwords strong enough to keep your accounts secure? Our Password Strength Checker can help you assess the strength of your passwords.")

    st.write(
        "Use our tool to quickly evaluate the strength of your passwords and make informed decisions about your online security.")

    # st.markdown(
    #     '<p style="color: red;">Note: The predictions are based on the data used to train the model and may not reflect real-time prices.</p>',
    #     unsafe_allow_html=True)

    st.warning(
        "⚠️ For security reasons, do not enter your actual password. Instead, use a similar password to check its strength.")

    pwd = st.text_input("Enter your password")

    if st.button('Check Password Strength'):

        str_pred = getStrength(pwd)
        str_pred = np.round(str_pred,2)

        st.title("Your Password Strength is :  {}".format(str_pred[0]))

        if str_pred <= 8:
            st.warning("⚠️ This password is easy to crack. Consider making it stronger.")
        elif 8 < str_pred < 15:
            st.info("ℹ️ This password falls between being too weak and too strong. Consider improving its complexity.")
        else:
            st.success("✅ This password seems strong and secure.")

        st.markdown(
            "Please remember that sharing your actual passwords or using them on untrusted websites can compromise your security and privacy. Always use unique and strong passwords for your accounts."
        )

    getTipsPwd = st.button('How to set secure Passwords??')
    if getTipsPwd:
        st.header("Tips for Creating Strong Passwords")
        st.markdown(
            "1. **Length Matters:** Longer passwords are generally more secure. Aim for at least 12 characters.")
        st.markdown(
            "2. **Mix It Up:** Use a combination of uppercase and lowercase letters, numbers, and special characters.")
        st.markdown(
            "3. **Avoid Common Patterns:** Steer clear of easily guessable patterns like '123456' or 'password'.")
        st.markdown(
            "4. **Unique for Each Account:** Don't use the same password across multiple accounts. This limits the impact of a security breach.")
        st.markdown(
            "5. **Phrases and Acronyms:** Create passwords using memorable phrases or acronyms only you would understand.")
