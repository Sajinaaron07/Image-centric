from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

app = FastAPI()
load_dotenv()


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

   