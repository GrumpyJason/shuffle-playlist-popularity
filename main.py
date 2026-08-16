#TODO: implement the spotify album reorganization part of the project starting with if user_album already exists and making new one if not

from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from youtube import sort_yt_playlist

class playlist_ids(BaseModel):
    youtube_playlist_id: str
    album_name: str

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.post("/submit-form")
async def handle_form(form_data: playlist_ids = Form()):
    data = {
        "yt_id": form_data.youtube_playlist_id, 
        "album": form_data.album_name
    }

    yt_sorted = sort_yt_playlist(data["yt_id"])
    return yt_sorted