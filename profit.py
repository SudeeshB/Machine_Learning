import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("PROFIT_ML_MODEL.sav" , "rb"))

st.set_page_config()
st.title("PROFIT PREDICTION")
st.write("prediction of PROFIT based on the amount spent")
st.divider()
prof_amount =st.number_input(
    "Enter the R&D amount",min_value= 0.0,) 
prof2 =st.number_input(    
    "Enter the Administration amount",min_value= 0.0)
prof3= st.number_input("Enter the Marketing Amount:",
    min_value= 0.0
)
if st.button("Predict profit"):
    input_data = np.array([[prof_amount,prof2,prof3]])
    prediction = model.predict(input_data)
    predict_profit = prediction[0][0]
    st.success(f"Predicted profit: ₹{predict_profit:,.2f}")