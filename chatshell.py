from import_xyz import import_xyz
import os
import subprocess
import llm

def get_chat_response(query):
        model = llm.get_model("orca-mini-3b")
        conversation = model.conversation()
        response = model.prompt(query)
        return response


def chat_shell():
    print("Welcome to LLN Chatbot. Type 'exit' to end the conversation.")
    
    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("You: ")
        if user_input.lower() != "exit":
            prompt = f"You: {user_input}\nLLN: "
            response = get_chat_response(prompt)
            print(type(response.text()))
            print(response.text())

if __name__ == "__main__":
    chat_shell()
