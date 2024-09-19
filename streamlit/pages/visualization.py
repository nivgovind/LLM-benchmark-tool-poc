import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from data.database import Session, Evaluation

def show():
    st.title("Evaluation Results Visualization")
    # session = Session()
    # evaluations = session.query(Evaluation).all()
    # df = pd.DataFrame([(e.test_case_id, e.is_correct) for e in evaluations], 
    #                   columns=['test_case_id', 'is_correct'])
    
    # st.bar_chart(df['is_correct'].value_counts())
    st.write("Correct vs Incorrect Answers")