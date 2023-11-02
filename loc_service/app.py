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
async def index_html():
    """Returns {"now": "ISO8601 now format"}
    NOTE: DEPENDS ON system clock PROPER config + proper NTP config & runtime!
    Note for interview: Let's use what we do have yet. Standard Py libs are
    enough now. JEE way - use the standard. (Must be supported /w no cost!)"""
    return {"now": datetime.datetime.utcnow().replace(tzinfo=datetime.UTC).isoformat()}


@app.get("/VIP/{point_in_time}")
async def read_item(point_in_time: int):


    return {"item_id": point_in_time}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=8088, log_level="debug", reload=True, host="0.0.0.0", timeout_keep_alive=4)
