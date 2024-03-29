from fastapi import FastAPI, Header
from fastapi.responses import FileResponse
from image_generator import *
from pathlib import Path
import uvicorn

app = FastAPI()

@app.get('/api/get')
async def post(url_avatar: str, answers: str, telegram_id: str):
    try:
        arr = []
        for elem in answers:
            arr.append(int(elem))
        print(arr)
        generate(url_avatar, arr, telegram_id)
        return {"status": "ok"}
    except:
        return {"status": "ne ok"}


@app.get('/api/get_save/{telegram_id}')
async def get_save(telegram_id):
    image_path = Path(f"generated_images/{telegram_id}.jpg")
    return FileResponse(image_path)

if __name__ == '__main__':
    uvicorn.run(app)