from fastapi import APIRouter, UploadFile, status
import json

from utils import speech_to_translate

router = APIRouter()


@router.post("/transcribe", status_code=status.HTTP_202_ACCEPTED)
async def transcribe(file: UploadFile):
    
    file = await file.read()
    
    # use celery to async it
    speech_to_translate(file)

    with open("translated_data.json", "w", encoding='utf-8') as f:
            empty_data = {'status':"In progress"}
            json.dump(empty_data, f, ensure_ascii=False, indent=4)

    return {'status':"Accepted"}


@router.get('/translate')
def translate():
    with open("translated_data.json", "r") as f:
        data = f.read()
        if data:
            data = json.loads(data)
        else:
            data = {}

    if data.get('status') == 'done':

        with open("translated_data.json", "w", encoding='utf-8') as f:
            empty_data = {'status':"No file uploaded"}
            json.dump(empty_data, f, ensure_ascii=False, indent=4)

        return data.get('ftext')
    else:
        return data.get('status')
    
    







    
