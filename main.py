from fastapi import FastAPI, Header
from fastapi.responses import FileResponse
from image_generator import *
from pathlib import Path
import uvicorn

app = FastAPI()


@app.get('/api/get')
async def get(url_avatar, answers):

    uuid = generate(url_avatar)
    image_path = Path(f"generated_images/{uuid}.jpg")

    return FileResponse(image_path)


if __name__ == '__main__':
    uvicorn.run(app)