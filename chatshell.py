from import_xyz import import_xyz
import os
import subprocess
import_xyz('llm')
import llm
from datetime import *
import math
from weather import *
from chat import *


time_list = ['what time','which day', "o' clock"]
wiki_list = ['search wiki', 'wikipedia', 'wiki']
weather_list = ['weather','is it going to rain', ' rain or not', 'how hot', 'how cold', 'temperature', 'wind speed', ' is it cold', 'is it hot']



def get_chat_response(query):
        model = llm.get_model("orca-mini-3b")
        conversation = model.conversation()
        response = model.prompt(query)
        return response


def chat_shell():
    greeting()
    print("Welcome to LLN Chatbot. Type 'exit' to end the conversation.")
    
    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("<<: ")
        if user_input.lower() != "exit":
            prompt = f"You: {user_input}\nLLN: "
            print (prompt)
            if user_input in time_list:
                day()
                time_now()

            elif user_input in wiki_list:
                wiki()

            elif user_input in weather_list:
                weather()

            else:
                response = get_chat_response(prompt)
                print(response.text())
                pass
            

if __name__ == "__main__":
    chat_shell()
