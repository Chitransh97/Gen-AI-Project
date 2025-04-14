import streamlit as st
from groq import Groq

st.set_page_config(page_title="CK97")

# Load the api key
api_key = st.secrets["API_KEY"]

# Initialize groq api
client = Groq(api_key = api_key)

# Write a function to generate response from model
def model_response(text: str, model_name="llama-3.3-70b-versatile"):
    stream = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assitant"
            },
            {
                "role": "user",
                "content": text
            }
        ],
        model = model_name,
        stream=True
    )

    for chunk in stream:
        response = chunk.choices[0].delta.content
        if response is not None:
            yield response

# Add title to streamlit app
st.title("Gen AI Model")
st.subheader("by Chitransh Khatri")

# Provide text area input for user
user_input = st.text_area("Ask any question:")

# Create a submit button
submit = st.button("Submit", type="primary")

# If button is clicked
if submit:
    st.subheader("Response")
    st.write_stream(model_response(user_input))