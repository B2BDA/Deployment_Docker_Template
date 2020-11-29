# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:48:36 2020

@author: bishw
"""

import streamlit as st
import pickle
import os
from sklearn.preprocessing import MinMaxScaler
mmx = MinMaxScaler()
model = pickle.load(open("cluster.pkl","rb"))
st.title("Customer Segmentation")
st.header("Enter Recency, Frequency & Revenue values")

recency = st.text_input("Enter Recency value")
frequency = st.text_input("Enter Frequency value")
revenue = st.text_input("Enter Revenue value")
# scaled = mmx.fit_transform([[float(recency), float(frequency), float(revenue)]])
# print(scaled)

if st.button("Sumbit") == True:
    cluster_class = model.predict([[float(recency), float(frequency), float(revenue)]])
    cluster_details = {3:'High Revenue/Frequency, Less Recency', 0:'High Revenue/Frequency, Less Recency',2:'Low Revenue/Frequency, High Recency', 1:'Medium Revenue/Frequency, Medium Recency'}
    st.write(cluster_details.get(cluster_class[0]))