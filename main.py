from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from fastapi import Body
import cloudinary
import cloudinary.uploader
import cloudinary.api
import openai

app = FastAPI()
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

cloudinary.config( 
  cloud_name = os.getenv("CLOUD_NAME"), 
  api_key = os.getenv("API_KEY"), 
  api_secret = os.getenv("API_SCERET"),
)
  


@app.post("/")
def upload(file:UploadFile = File(...)):
    result = cloudinary.uploader.upload(file.file)
    url = result.get('url')
    return {'url':url}

@app.post("/chat")
def chat(prompt:str= Body()):

  response = openai.Completion.create(
      prompt = prompt,
      model = os.getenv('MODEL'),
      max_tokens = 1000,
      temperature = 0.9,

  )
  
  
  return response.choices[0]


   