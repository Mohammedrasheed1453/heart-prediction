import pickle
import streamlit as st
from streamlit_option_menu import option_menu
disease = pickle.load(open("heartprediction.sav", "rb"))
#default index if it is 1 then first disease will be index one disease
with st.sidebar:
    selected=option_menu("multiple  disease prediction",["heart disease","diabetis prediction"],
                         icons=["heart","activity"],
                         default_index=0)
if selected=="diabetis prediction":
    st.title("Diabetes prediction using ml")

if selected=="heart disease":
    st.title("heart disease prediction using ml")
    col1,col2,col3=st.columns(3)
    with col1:
        age = st.text_input("Enter your age")
    with col2:
        sex = st.selectbox("Select your sex", options=[1, 0])
    with col3:
        cp = st.selectbox("Select chest pain type", options=[0,1,2,3])
    with col1:
        trestbps = st.text_input("Enter resting blood pressure")
    with col2:
        chol = st.text_input("Enter serum cholesterol in mg/dl")
    with col3:
        fbs = st.selectbox("Is fasting blood sugar > 120 mg/dl?", options=[0,1])
    with col1:
        restecg = st.selectbox("Resting electrocardiographic results", options=[ 0,1,2])
    with col2:
        thalach = st.text_input("Enter maximum heart rate achieved")
    with col3:
        exang = st.selectbox("Exercise induced angina", options=[0,1])
    with col1:
        oldpeak = st.text_input("Enter ST depression induced by exercise relative to rest")
    with col2:
        slope = st.selectbox("The slope of the peak exercise ST segment", options=[0,1,2])
    with col3:
        ca = st.text_input("Enter number of major vessels (0-3) colored by flourosopy")
    with col1:
        thal = st.selectbox("Thalassemia", options=[0,1,2,3])
    diagnosis=""
    #creating a button for prediction
    if st.button("heart=disease test result"):
        heart_pred=disease.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,
                                     exang,oldpeak,
                                     slope,ca,thal]])
        if heart_pred[0]==1:
            diagnosis="the person has heart disease"
        else:
            diagnosis="the person dosen thave heart disease"
    st.success(diagnosis)




