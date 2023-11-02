from typing import Union
import fastapi
from fastapi import FastAPI
import datetime


# Constants
app = FastAPI()
INDEX_HTML = """<!DOCTYPE html>
<html>
<head>
  <title>My Simple HTML Page</title>
</head>
<body>
  <h1>This is a simple HTML page!</h1>
  <p><a href="./v1/now">Now endpoint as csv.</a></p>
  <p><a href="./v1/VIP/1">Coordinates of VIP in given time</a></p>
  <p>This form overwrites data in the current SQLite DB.</p>
  <form action="/load-data" method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
  </form>
  </body>
</html>"""


@app.get("/", response_class=fastapi.responses.HTMLResponse)
async def index_html():
    return INDEX_HTML


@app.get("/v1/now")
def index_html():
    """Returns {"now": "ISO8601 now format"}
    NOTE: DEPENDS ON system clock PROPER config + proper NTP config & runtime!"""
    return {"now": datetime.datetime.utcnow().replace(tzinfo=datetime.UTC).isoformat()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=8088, log_level="debug", reload=True, host="0.0.0.0", timeout_keep_alive=4)
