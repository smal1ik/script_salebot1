from fastapi import FastAPI, Header
from fastapi.responses import FileResponse
from image_generator import *
from pathlib import Path
import uvicorn

app = FastAPI()


@app.get('/api/get')
async def get(url_avatar: str, answers: str):
    arr = []
    for elem in answers:
        arr.append(int(elem))
    print(arr)
    uuid = generate(url_avatar, arr)
    image_path = Path(f"generated_images/{uuid}.jpg")

    return FileResponse(image_path)


if __name__ == '__main__':
    uvicorn.run(app)