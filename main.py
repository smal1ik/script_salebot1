import urllib.request as request
from fastapi import FastAPI, Header
from fastapi.responses import FileResponse
from typing import Annotated
from pathlib import Path
import uvicorn

app = FastAPI()
server = app.server

@app.get('/api/get')
async def get(avatar: Annotated[str | None, Header()] = None, answers: Annotated[list[int] | None, Header()] = None):
    img = "https://files.salebot.pro/uploads/avatars/332056/1-288193541-365276269.jpg"
    resource = request.urlopen(img)
    out = open("img.jpg", 'wb')
    out.write(resource.read())
    out.close()
    image_path = Path("img.jpg")
    return FileResponse(image_path)


# if __name__ == '__main__':
#     uvicorn.run(app)