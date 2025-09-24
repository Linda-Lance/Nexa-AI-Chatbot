import streamlit as st
import ollama
from gtts import gTTS

# Your chatbot name
CHATBOT_NAME = "Nexa AI"

def generate_llm_response(prompt, model="llama3.2"):
    # Check if user is asking the chatbot's name
    if any(word in prompt.lower() for word in ["your name", "who are you", "what is your name"]):
        return (f"Hello! I'm {CHATBOT_NAME}. "
                "I'm here to assist you, answer your questions, and provide helpful information. "
                "You can ask me anything, and I'll do my best to help!")
    
    messages = [{'role': 'user', 'content': prompt}]
    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']

st.title("Nexa AI")
st.write("Interact with a Large Language Model (LLM) and listen to responses")

user_prompt = st.text_area('Enter your Prompt...')

if st.button('Generate Response'):
    if user_prompt.strip() != "":
        with st.spinner('Generating response...'):
            try:
                response = generate_llm_response(user_prompt)
                st.success("Response generated!")
                st.text_area("LLM Response:", value=response, height=200)

                # Convert to Speech
                tts = gTTS(response)
                tts.save("response.mp3")
                audio_file = open("response.mp3", "rb")
                st.audio(audio_file.read(), format="audio/mp3")

            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a prompt.")
