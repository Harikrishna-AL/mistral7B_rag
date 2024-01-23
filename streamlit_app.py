import streamlit as st
import requests
from streamlit_chat import message
import black

def chat_ui(prompt,response):
    
    message(response)

class Mistral7BChat:
    def __init__(self):
        self.api_endpoint = "https://a8qo11ogw37imm-5000.proxy.runpod.net/generate/"
        self.headers = {"Content-Type": "application/json"}
        # self.chat_history = []

    def query_mistral_7b(self, input_text, context="You were developed by mistral jsut to write taglines for products"):
        form_data = {
            "prompt": input_text,
            }
    
        response = requests.post(self.api_endpoint, json=form_data, headers=self.headers)

        if response.status_code == 200:
            output_text = response.json().__str__()
            # output_text = output_text.strip('"')
            # output_text = output_text.replace("\\n", "\n")
            # output_text = black.format_str(output_text, mode=black.FileMode())
            # self.chat_history.append({"user": input_text, "mistral_7b": output_text})
            return output_text
        else:
            return f"Error: {response.status_code} - {response.text}"

def main():
    st.title("Mistral 7B Chat Interface")

    chatbot = Mistral7BChat()

    user_input = st.chat_input("Enter your message:")
    if user_input is not None:
        message(user_input, is_user=True)

    if user_input:
        response_text = chatbot.query_mistral_7b(user_input)
        message(response_text)


if __name__ == "__main__":
    main()