from typing import Union
from fastapi import FastAPI

# Constants
app = FastAPI()
INDEX_HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>My Simple HTML Page</title>
</head>
<body>
  <h1>This is a simple HTML page!</h1>
  <a href="./v1/now">This exports the current SQLite DB as csv.</a>
  <a href="./v1/VIP/">This exports the current SQLite DB as csv.</a>
  <a href="./v1/coords/2">This exports the current SQLite DB as csv.</a>
  <p>This form overwrites data in the current SQLite DB.</p>
  <form action="/load-data" method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
  </form>
  </body>
</html>
"""

@app.get("/")
def index_html():
    return INDEX_HTML


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=8088, log_level="debug", reload=True, host="0.0.0.0", timeout_keep_alive=4)
