import streamlit as st
from services.openai_client import get_model_answer

def show():
    st.title("Model Evaluation")
    # if 'selected_case' not in st.session_state:
    #     st.warning("Please select a test case first.")
    #     return

    # test_case = st.session_state['selected_case']
    # model_answer = get_model_answer(test_case['question'])
    
    # st.write("Model Answer:", model_answer)
    # st.write("Correct Answer:", test_case['final_answer'])

    # is_correct = st.radio("Is the model answer correct?", ["Yes", "No"])
    # feedback = st.text_area("Feedback")

    # if st.button("Submit Evaluation"):
    #     session = Session()
    #     evaluation = Evaluation(
    #         test_case_id=test_case['id'],
    #         model_answer=model_answer,
    #         is_correct=(is_correct == "Yes"),
    #         feedback=feedback
    #     )
    #     session.add(evaluation)
    #     session.commit()
    #     st.success("Evaluation submitted successfully!")