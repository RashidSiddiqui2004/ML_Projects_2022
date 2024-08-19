import pandas as pd
import streamlit as st
import pickle
import numpy as np
# import sklearn as sns

pipe = pickle.load(open("realmeModel.pkl", 'rb'))
scaler = pickle.load(open("realmeScaler.pkl", 'rb'))
df = pd.read_csv('realmeDF.csv')

import requests
from PIL import Image
from io import BytesIO


def resize_image_from_url(image_url, size=(50, 50)):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = image.resize(size)
    return image


def display_image_grid(image_urls,names,prices,grid_columns=3):
    num_images = len(image_urls)
    num_rows = (num_images // grid_columns)

    num_columns = 3 # Number of columns to display the images
    col_width = 150  # Width of each column

    # Display the images in columns
    for i in range(0, num_images, num_columns):
        cols = st.columns(num_columns)
        for j, col in enumerate(cols):
            if i + j < num_images:
                image_url = image_urls[i+j]
                resized_image = resize_image_from_url(image_url, size=(180, 220))
                col.image(resized_image, width=col_width)
                col.write("Brand: {}".format(names[i+j]))
                col.write("Price: {}".format(prices[i + j]))

    # for i in range(num_rows):
    #     st.write('<div style="display: flex;">', unsafe_allow_html=True)
    #     for j in range(grid_columns):
    #         image_idx = i * grid_columns + j
    #         if image_idx < num_images:
    #             image_url = image_urls[image_idx]
    #             resized_image = resize_image_from_url(image_url, size=(150,150))
    #             st.image(resized_image, use_column_width=False, caption=f"Image {image_idx+1}")
    #             st.write("Realme Phone")
    #             st.write("Price")

        st.write('</div>', unsafe_allow_html=True)


def assistUser():
    st.title("RealMe SmartPhone Price Predictor")

    # Custom CSS for the slider
    st.markdown(
        """
        <style>
            /* Styling for the slider */
            .rating-slider .stSlider {
                -webkit-appearance: none;
                width: 100%;
                height: 10px;
                border-radius: 5px;
                background: #f5f5f5;
            }
            .rating-slider .stSlider::-webkit-slider-thumb {
                -webkit-appearance: none;
                appearance: none;
                width: 20px;
                height: 20px;
                border-radius: 50%;
                background: #007BFF;
                cursor: pointer;
            }
            .rating-slider .stSlider::-moz-range-thumb {
                width: 20px;
                height: 20px;
                border-radius: 50%;
                background: #007BFF;
                cursor: pointer;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p style="color: green;font-size:30px;text-align:center;font-weight:700;">Developed By- Rashid Siddiqui</p>',
        unsafe_allow_html=True)


    img1 = "realmeImages/narzo.jpg"
    img2 = "realmeImages/pro10.jpg"
    img3 = "realmeImages/realme.jpg"

    list_images = [img3,img2]

    num_columns = 2  # Number of columns to display the images
    col_width = 200  # Width of each column

    for i in range(0, 2, num_columns):
        cols = st.columns(num_columns)
        for j, col in enumerate(cols):
            if i + j < 2:
                image_url = list_images[i + j]
                # resized_image = resize_image_from_url(image_url, size=(180, 220))
                col.image(image_url, width=col_width)
                # col.write("Brand: {}".format(names[i + j]))
                # col.write("Price: {}".format(prices[i + j]))

    # st.image(img1)

    # Website Description
    st.markdown(
        """
        ### Welcome to the RealMe Smartphone Price Predictor

        This website allows you to predict the price of RealMe smartphones based on certain specifications. 
        With our machine learning model, you can estimate the price of a RealMe smartphone with high accuracy.

        Simply adjust the sliders for RAM, Internal Storage, and Camera Resolution to match the specifications of the smartphone you want to predict the price for. 
        You can also rate the mobile on a scale of 0 to 5 to further refine the prediction.

        Our model uses the input provided by you to make a prediction on the expected price of the RealMe smartphone.

        Try it out and discover the potential price of your desired RealMe smartphone!"""

        ,unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color: red;">Note: The predictions are based on the data used to train the model and may not reflect real-time prices.</p>',
        unsafe_allow_html=True)

    battery = st.number_input("Enter battery life(in mA.h)")
    # speed = st.number_input("Enter speed(in GHz)")
    speed = 1820
    processor = st.number_input("Enter Generation of the Phone(e.g. 5 if 5G Phone)")

    display_size_cm = st.number_input("Enter Display of phone (in cm)")
    display_size_inch = display_size_cm * 0.393701
    # internal_storage = st.number_input("Enter Internal Storage(GB)")
    # ram = st.number_input("Enter RAM(in GB)")
    ram = st.slider('Select RAM (in GB)', 2, 8, 4)
    internal_storage = st.slider('Select Internal Storage (in GB)', 32, 256, 64)
    expandable_storage = st.number_input("Enter Expandable Storage(in GB)")
    resolution_x = st.number_input("Enter Resolution_X: ")
    resolution_y = st.number_input("Enter Resolution_Y: ")

    st.markdown('<h3 style="margin-top: 30px;">Enter the Ratings of the Mobile you need (out of 5):</h3>',
                unsafe_allow_html=True)

    ratings = st.slider('', 0.0, 5.0, 3.0, step=0.1, key='rating', format='%f')

    if st.button('Get Price of the SmartPhone'):

        query = [ratings, battery, speed, processor, display_size_cm, display_size_inch, internal_storage, ram,
                 expandable_storage, resolution_x, resolution_y]

        query = np.array(query)
        query = query.reshape(1, -1)
        query1 = scaler.transform(query)

        price = pipe.predict(query1)[0]

        # Add CSS for custom styling and animations
        st.markdown(
            """
            <style>
                .title {
                    text-align: center;
                    font-size: 36px;
                    font-weight: bold;
                    margin-bottom: 30px;
                    color: #007BFF;
                    animation: scaleIn 0.8s ease-in-out;
                }

                .prediction {
                    font-size: 24px;
                    font-weight: bold;
                    color: #28A745;
                    animation: fadeIn 1.5s ease-in-out;
                }

                @keyframes scaleIn {
                    from {
                        transform: scale(0.5);
                        opacity: 0;
                    }
                    to {
                        transform: scale(1);
                        opacity: 1;
                    }
                }

                @keyframes fadeIn {
                    from {
                        opacity: 0;
                    }
                    to {
                        opacity: 1;
                    }
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Animated title
        st.markdown('<p class="title">RealMe Smartphone Price Predictor</p>', unsafe_allow_html=True)

        # Animated predicted price
        st.markdown('<p class="prediction">Predicted Price: Rs.{:.2f}</p>'.format(price+2200), unsafe_allow_html=True)


    budget = st.number_input("Enter your budget (in Rs.)")

    underBudgetPhones = st.button("Get Phones Under my Budget")

    if underBudgetPhones:
        underBudget = df[df['price'] < budget].sort_values(by='price', ascending=False).head(9)

        # underBudget

        image_urls = underBudget['imgURL'].tolist()
        names = underBudget['name'].tolist()
        prices = underBudget['price'].tolist()

        # Set the app title
        st.title('RealMe SmartPhones under your Budget')

        # Display the image grid
        display_image_grid(image_urls,names,prices)

    st.markdown(
        '<p style="color: green;font-size:30px;">Trained By- Rashid Siddiqui</p>',
        unsafe_allow_html=True)



