#import pandas as pd
##from agents.import *

#a=2
#b=4
#c=a+b
#print(c)


####code to read the APIs from env file
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPEN_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

print(openai_api_key)
print(openai_api_key)
