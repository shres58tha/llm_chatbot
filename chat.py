from datetime import *
import random
import chat as chat
from import_xyz import import_xyz
import_xyz('wikipedia')
import wikipedia
from weather import *
from news_bbc import *
import requests

now = datetime.now()

def greeting():
    hour = int(now.hour)
    if hour>=0 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
    else:
        print("Good evening!")

def day():
    days = now.strftime("%A, %B %d")
    print(f"Today is {days}.")

def time_now():
    times = now.strftime("%H:%M:%S")
    print(f"The time is {times}.")

def weather():
    find_weather(query = 'kathmandu')

def wiki():
    data= input("what to find summary of in wikipedia <<: ")
    result = wikipedia.summary(data)
    # printing the result
    print(result)

def news():
    display_news()
