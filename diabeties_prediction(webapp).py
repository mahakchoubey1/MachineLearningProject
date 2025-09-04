# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 19:23:41 2025

@author: 2003m
"""

import numpy as np 
import pickle 
import streamlit as st
loader_model=pickle.load(open('C:/Users/2003m/PycharmProjects/ML Projects/trained_model.sav','rb'))# load the saved model and" rb "is reading binary

# creating function forprediction
def diabetes_prediction(input_data):
    
   # input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the input data
    ##std_data = scaler.transform(input_data_reshaped)
    #print(std_data)

    prediction = loader_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    # giving title for webpagfe
    st.title('Diabetes Prediction Web App')
    
    # getting input_data from user4
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies=st.text_input('Enter Number of pregnancies')
    Glucose=st.text_input('Enter Glucose level')
    BloodPressure=st.text_input('Enter BloodPressure')
    SkinThickness=st.text_input('Enter SkinThickness')
    Insulin=st.text_input('Enter Insulin level')
    BMI=st.text_input('Enter BMI')
    DiabetesPedigreeFunction=st.text_input('Enter  DiabetesPedigreeFunction ')
    Age=st.text_input('Enter Age')
    
    
    # code for prediction 
    diagnosis = ''      # to store prediction output
    
    
    #creating a button for prediction 
    if st.button('Diabetes Test Result'):
          diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    
    st.success(diagnosis)
    
    
    
    
    
 #To run file from command prompt as a stand alone file
if __name__ == '__main__' :
    main()
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    