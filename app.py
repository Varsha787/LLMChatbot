# !pip install google-generativeai

import google.generativeai as genai
import os
import grpc

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"


def remove_star(text):
  return text.replace("*", "")

genai.configure(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

def get_response(message : str):
  response = model.generate_content(message)
  return remove_star(response.text)


