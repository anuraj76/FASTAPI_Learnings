from fastapi import FastAPI
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()  #Create FAST API Object

# Use the API key from environment variable
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  #Insert your OpenAI API key here

@app.get("/") #Use @app.get decorator to create endpoints and chat path
def root_controller():
    return {"message": "Welcome to the AI-powered text generation API!"}

@app.get("/chat")
def chat_controller(prompt:str = "Inspire me"):
    #make an API call to OpenAI to generate a response to the prompt
    response = openai_client.Completion.create(
        model="gpt-4o",
        message=[
            {"role":"system", "content":"You are an AI assistant. You will be given a task. You must generate a detailed and long answer."},
            {"role":"user", "content":prompt},
        ],
    )
    statement = response.choices[0].message.content
    #any data returned by decorated functions will be returned by it
    return {"statement": statement}

