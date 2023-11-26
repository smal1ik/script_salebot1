import urllib.request as request
from fastapi import FastAPI, Header
from fastapi.responses import FileResponse

from pathlib import Path
import uvicorn

app = FastAPI()


@app.get('/api/get/{avatar}')
async def get(avatar: str):
    img = avatar
    resource = request.urlopen(img)
    out = open("img.jpg", 'wb')
    out.write(resource.read())
    out.close()
    image_path = Path("img.jpg")
    return FileResponse(image_path)


if __name__ == '__main__':
    uvicorn.run(app)