from import_xyz import import_xyz
import os
import subprocess
import_xyz('llm')
import llm
from datetime import *
import math
from weather import *
from chat import *

hello_list = ['hello', 'hi',' good morning', 'good afternoon', 'greetings']
time_list = ['what time','which day', "o' clock", 'time', 'day','what time is it']
wiki_list = ['search wiki', 'wikipedia', 'wiki']
weather_list = ['weather','is it going to rain', ' rain or not', 'how hot', 'how cold', 'what temperature', 'wind speed', ' is it cold', 'is it hot']
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
        if any(map(user_input.__contains__,hello_list)):
            response = greeting()
            print (f'{response}, i am chatbot with few capabilities. \n you can  use me to \n 1. ask me day / time \n 2. limited search wikipedia as "search wiki"/ "wiki" \n 3. ask weather \n 4. get summary of news from bbc \n 5 or use llm " llm model("orca-mini-3b") 1.8 Gb size" \n but i am bit slow at thinking in \n my capabilities being limited by theis box\n')
        elif any(map(user_input.__contains__, time_list)):
            day()
            time_now()

        elif any(map(user_input.__contains__, wiki_list)):
            wiki()

        elif any(map(user_input.__contains__, weather_list)):
           weather()

        elif user_input in news_list:
            news()

        else:
            response = get_chat_response(prompt)
            print(response.text())

if __name__ == "__main__":
    chat_shell()
