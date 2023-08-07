from import_xyz import import_xyz
import os
import subprocess
import_xyz('llm')
import llm
from datetime import *
import math
from weather import *
from chat import *


time_list = ['what time','which day', "o' clock", 'time', 'day']
wiki_list = ['search wiki', 'wikipedia', 'wiki']
weather_list = ['weather','is it going to rain', ' rain or not', 'how hot', 'how cold', 'temperature', 'wind speed', ' is it cold', 'is it hot']
exit_list = ['Goodbye, I hope to assist you again soon.','bye','close','exit']
news_list = ['what in news','news','news summary', 'bbc']



def get_chat_response(query):
        model = llm.get_model("orca-mini-3b")
        conversation = model.conversation()
        response = model.prompt(query)
        return response


def chat_shell():
    greeting()
    print("Welcome to LLN Chatbot. Type 'exit' to end the conversation.")

    user_input = ""
    while 1:
        user_input = input("<<: ").lower()
        #print( user_input)
        if user_input in exit_list:
            print(user_input)
            exit(0)
        prompt = f"Thinking about h: {user_input}\nLLN: "
        print (prompt)
        if user_input in time_list:
            day()
            time_now()

        elif user_input in wiki_list:
            wiki()

        elif user_input in weather_list:
            weather()

        elif user_input in news_list:
            news()

        else:
            response = get_chat_response(prompt)
            print(response.text())

if __name__ == "__main__":
    chat_shell()
