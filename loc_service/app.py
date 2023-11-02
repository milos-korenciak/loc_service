from typing import Union
import fastapi
from fastapi import FastAPI
import datetime
import random as ra
import asyncio
import aiohttp


# Constants
app = FastAPI()
PORT = 8888
MAX_DELAY_SEC = 4
URL_HTTP_DB = "http://localhost:%s/v1/coords/{point_in_time}" % PORT
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



async def wait_max_time():
    """Wait max allowed time"""
    await asyncio.sleep(MAX_DELAY_SEC)
    return "500"  # here return 500 HTTP error

async def download_coordinates_db():
    """asynchronously download the coordinates"""
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())

    return {"type": "coords",
            "latitude": ra.randrange(-180., +180.),
            "longitude":ra.randrange(-180., +180.)}


async def wait_first():
    done, pending = await asyncio.wait(
        [wait_max_time(), download_coordinates_db()],
        return_when=asyncio.FIRST_COMPLETED)
    print("done", done)
    print("pending", pending)


@app.get("/v1/VIP/{point_in_time}")
async def read_vip(point_in_time: int):
    """ Serve coordinates
    NOTE: We can fail here, if we are not in given time.
    Let's use Error 500, as this IS Server internal troubles here."""
    concrete_url = URL_HTTP_DB.format(point_in_time=point_in_time)
    latitude = 0.
    longitude = 0.
    await asyncio.sleep(ra.choice((0, 6)))
    return {"source": "vip-db", "gpsCoords": {"lat": latitude, "long": longitude}}


@app.get("/v1/coords/{point_in_time}")
async def quazi_unreliable_db(point_in_time: int):
    """ HELPER METHOD!
    Serve coordinates of VIP. Sometimes /w >5s delay, sometimes immediately!"""
    await asyncio.sleep(ra.choice((0,6)))
    return


if __name__ == "__main__":
    import uvicorn
    # temporary override to 8888 - browser
    uvicorn.run("app:app", port=PORT, log_level="debug", reload=True, host="0.0.0.0", timeout_keep_alive=4)
