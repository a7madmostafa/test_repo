import streamlit as st
import pandas as pd
import pickle

st.title('Car Price Prediction App')


# Inputs
floors = st.number_input('Floors', 1, 10, 1)
waterfront = st.checkbox('Waterfront')
latitude = st.number_input('Latitude', -90, 90, 0)
bedrooms = st.slider('Bedrooms', 2, 10, 0)
sqft_basement = st.number_input('Sqft_Basement', 0, 10000, 0)
view = st.selectbox('View', [0, 1, 2, 3, 4])
bathrooms  = st.slider('Bathrooms', 0, 10, 0)
sqft_living15 = st.number_input('Sqft_Living15', 1000, 10000, 5000)
sqft_above = st.number_input('Sqft_Above', 1000, 10000, 5000)
grade = st.slider('Grade', 1, 13, 1)
sqft_living = st.number_input('Sqft_Living', 1000, 10000, 5000)


# Data
data = {'floors': floors,
    'waterfront': 1 if waterfront else 0,
    'lat': latitude,
    'bedrooms': bedrooms,
    'sqft_basement': sqft_basement,
    'view': view,
    'bathrooms': bathrooms,
    'sqft_living15': sqft_living15,
    'sqft_above': sqft_above,
    'grade': grade,
    'sqft_living': sqft_living
    }

data = pd.DataFrame(data, index=[0])

# Prediction
model = pickle.load(open('Car_Price_Model.pkl', 'rb'))
prediction = model.predict(data)

# Output
st.header(f'Predicted Price: ${prediction[0]:.2f}')