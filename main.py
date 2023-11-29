from fastapi import FastAPI, Header
from fastapi.responses import FileResponse
from image_generator import *
from pathlib import Path
import uvicorn
import os
app = FastAPI()


@app.get('/api/get')
async def get(url_avatar, answers):
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    uuid = generate(url_avatar)
    image_path = Path(f"{dir}/generated_images/{uuid}.jpg")

    return FileResponse(image_path)


if __name__ == '__main__':
    uvicorn.run(app)