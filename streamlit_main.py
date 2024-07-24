import streamlit as st
from src.generate_answers import generate_answer

# Set the title of the Streamlit app
st.title("Ask Lawyers")

# Provide example questions for the user to select or refer to
example_questions =  ["what is indian penal code?",
                "what is ipc 420?",
                "what are sections in ipc?"]

# Display the example questions as a dropdown menu
selected_question = st.selectbox("Select an example question:", example_questions)

# Allow the user to enter their own question or modify the selected example
input_text = st.text_input("Or enter your own question:", selected_question)

# If the user submits the form, process the input
if st.button("Submit"):
    if input_text:
        # Generate a response based on the input
        response = generate_answer(query=input_text)
        # Display the response
        st.write(f"Response: {response}")
    else:
        st.write("Please enter or select a question.")
