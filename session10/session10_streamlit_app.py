import streamlit as st
from PIL import Image
import pandas as pd
import joblib
#st.title('my first app py  " Mohamed Faisal"')
#st.write(' this is my first app in NTI')
#x = st.file_uploader("upload image" , type=['jpg','png','jpeg'])
#if x is not None:
#    image = Image.open(x)
#    st.image(image, caption='Machine Learning Image')
#name = st.text_input("Enter your name")
#password = st.text_input("Enter your Password", type="password")
#age = st.number_input("Enter Age", min_value=1, max_value=100)
#gender = st.selectbox("Choose Gender", ["Male", "Female"])
#if name:
#    st.write("Welcome", name)
#if st.button("Predict"):
#    st.write("Done")   
#file = st.file_uploader("")
#st.success("Prediction Done")
#st.error("Wrong Input")
#st.warning("Check Data")



model = joblib.load('svm_model.pkl')
st.title('Virus Prediction')

med1 = st.number_input('Medicine 1', min_value=0.0)
med2 = st.number_input('Medicine 2', min_value=0.0)

if st.button('Predict'):

    sample = pd.DataFrame({
        'Med_1_mL': [med1],
        'Med_2_mL': [med2]
    })

    prediction = model.predict(sample)
    if prediction[0]==1:
        st.error("virus is present")
    else:
        st.success("no virus")
            

