import streamlit as st
import pickle
import numpy as np
import sklearn as sns

pipe = pickle.load(open("HRhelper.pkl",'rb'))
scaler = pickle.load(open("scaler.pkl",'rb'))

# st.title("HR Interview Call Prediction -   AI Helper")
# st.title("Here's your personal health check-up, get assured of Diabetes-free life.")
#
# name = st.text_input("Enter Candidate's name")
# comp = st.selectbox("Select Company you have appplied for",['Amazon','Flipkart','Zoho','Paytm','Flipkart','Uber',
#                                                             'Google','Microsoft','Paypal'])
# gender = st.selectbox("Select your Gender",['Male','Female'])
#
# age = st.number_input("Please Enter your age (in years)")
#
# years_of_experience = st.selectbox("Enter your Industry experience",['<= 1 year','>1 and <2 years','>2 and <3 years',
#                                                                      '>3 and <5 years','>= 5 years'])
#
# st.title("Enter all the scores out of 1")
#
# functional_competency_score = st.number_input("Enter your functional_competency_score ")
#
# top1_skills_score = st.number_input("Enter your top1_skills_score ")
# top2_skills_score = st.number_input("Enter your top2_skills_score ")
# top3_skills_score = st.number_input("Enter your top3_skills_score ")
#
# behavior_competency_score =  st.number_input("Enter your behavior_competency_score ")
# top1_behavior_skill_score = st.number_input("Enter your top1_behavior_skill_score ")
# top2_behavior_skill_score = st.number_input("Enter your top2_behavior_skill_score ")
# top3_behavior_skill_score = st.number_input("Enter your top3_behavior_skill_score ")
#
# if st.button('Click to Know whether u would be called or not'):
#
#     if years_of_experience == '<= 1 year':
#         years_of_experience = 1
#     elif years_of_experience== '>1 and <2 years':
#         years_of_experience = 1.5
#     elif years_of_experience== '>2 and <3 years':
#         years_of_experience = 2.5
#     elif years_of_experience == '>3 and <5 years':
#         years_of_experience = 3.9
#     else:
#         years_of_experience = 5.2
#
#     query = [years_of_experience,functional_competency_score,top1_skills_score,top2_skills_score,top3_skills_score,
#              behavior_competency_score, top1_behavior_skill_score,top2_behavior_skill_score,top3_behavior_skill_score]
#
#     query = np.array(query)
#     query = query.reshape(1, -1)
#     query1 = scaler.transform(query)
#
#     if(pipe.predict(query1)[0]==1):
#         st.title("Congratulations, You are selected for the  HR Interview 😊 ")
#
#     else:
#         st.title('Sorry,You are not selected for HR Interview 😔')
#
#         st.title("WORK HARD FOR THE NEXT COMPANY")
#
#         st.title("Practice all SDE Sheet Problems on this site!")
#
#         st.write( "Link:- [SDE SHEET- 250 DSA QUESTIONS](https://practice.geeksforgeeks.org/explore?page=1&curated[]=1&sortBy=submissions&curated_names[]=SDE%20Sheet)")

def funcCall():

    st.title("HR Interview Call Prediction -   AI Helper")
    # st.title("Here's your personal health check-up, get assured of Diabetes-free life.")

    name = st.text_input("Enter Candidate's name")
    comp = st.selectbox("Select Company you have appplied for",
                        ['Amazon', 'Flipkart', 'Zoho', 'Paytm', 'Flipkart', 'Uber',
                         'Google', 'Microsoft', 'Paypal'])
    gender = st.selectbox("Select your Gender", ['Male', 'Female'])

    age = st.number_input("Please Enter your age (in years)")

    years_of_experience = st.selectbox("Enter your Industry experience",
                                       ['<= 1 year', '>1 and <2 years', '>2 and <3 years',
                                        '>3 and <5 years', '>= 5 years'])

    st.title("Enter all the scores out of 1")

    functional_competency_score = st.number_input("Enter your functional_competency_score ")

    top1_skills_score = st.number_input("Enter your top1_skills_score ")
    top2_skills_score = st.number_input("Enter your top2_skills_score ")
    top3_skills_score = st.number_input("Enter your top3_skills_score ")

    behavior_competency_score = st.number_input("Enter your behavior_competency_score ")
    top1_behavior_skill_score = st.number_input("Enter your top1_behavior_skill_score ")
    top2_behavior_skill_score = st.number_input("Enter your top2_behavior_skill_score ")
    top3_behavior_skill_score = st.number_input("Enter your top3_behavior_skill_score ")

    if st.button('Click to Know whether u would be called or not'):

        if years_of_experience == '<= 1 year':
            years_of_experience = 1
        elif years_of_experience == '>1 and <2 years':
            years_of_experience = 1.5
        elif years_of_experience == '>2 and <3 years':
            years_of_experience = 2.5
        elif years_of_experience == '>3 and <5 years':
            years_of_experience = 3.9
        else:
            years_of_experience = 5.2

        query = [years_of_experience, functional_competency_score, top1_skills_score, top2_skills_score,
                 top3_skills_score,
                 behavior_competency_score, top1_behavior_skill_score, top2_behavior_skill_score,
                 top3_behavior_skill_score]

        query = np.array(query)
        query = query.reshape(1, -1)
        query1 = scaler.transform(query)

        if (pipe.predict(query1)[0] == 1):
            st.title("Congratulations, You are selected for the  HR Interview 😊 ")

        else:
            st.title('Sorry,You are not selected for HR Interview 😔')

            st.title("WORK HARD FOR THE NEXT COMPANY")

            st.title("Practice all SDE Sheet Problems on this site!")

            st.write(
                "Link:- [SDE SHEET- 250 DSA QUESTIONS](https://practice.geeksforgeeks.org/explore?page=1&curated[]=1&sortBy=submissions&curated_names[]=SDE%20Sheet)")
