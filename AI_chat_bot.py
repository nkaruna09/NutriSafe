import streamlit as st
import cohere

# Initialize Cohere API client with your API key
co = cohere.Client('rFtQp6u9Dj0QIfwyKRAGGEZwbuZWOutMSoi4wMZ0')  # Replace with your actual API key

# Function to call Cohere for generating responses
def get_cohere_response(user_input):
    response = co.generate(
        model='command-r-08-2024',  # Cohere's model for generating text
        prompt=f"User is asking for health advice. Answer based on the user's health goals and preferences. If the user asks a non-health//food related question, say that you cannot respond. \nUser: {user_input}\nAI:",
        max_tokens=150,
        temperature=0.7,
    )
    return response.generations[0].text.strip()

# Streamlit App Layout
st.markdown("### Ask me anything about health, diet, and nutrition! 💬")

# Set up a session state to store chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to display messages in chat-like format
def display_chat():
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.markdown(f"**YOU**: {message['text']}")
        elif message['role'] == 'ai':
            st.markdown(f"**AI HEALTH COACH**: {message['text']}")

# Disclaimer 
st.write("""DISCLAIMER: Any information provided by this AI chatbot is for informational purposes only and 
         should not be considered as professional medical advice. Always consult a qualified healthcare 
         professional before making any important decisions related to your health, treatment, or well-being. 
         The chatbot does not diagnose conditions, provide prescriptions, or offer personalized medical 
         recommendations. By using this service, you acknowledge that any actions you take based on the 
         information provided are at your own risk.""")

# Handle user input
user_input = st.text_input("Type your question here:")

# When the user submits input
if user_input:
    # Append user message to the chat history
    st.session_state['messages'].append({'role': 'user', 'text': user_input})
    
    # Get AI response
    ai_response = get_cohere_response(user_input)
    
    # Append AI response to the chat history
    st.session_state['messages'].append({'role': 'ai', 'text': ai_response})

# Display chat history
display_chat()

