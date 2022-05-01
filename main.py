# from typing import Optional

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# @app.get("/")
# def index():
#     return {"Hello": "World"}

# @app.get("/about")
# def index():
#     return {"About": "World"}


# 1
# @app.get("/blog")
# def index(limit):
#     # /blog?limit=10 =>{"Blogs":"10 blogs from db"}
#     return {"Blogs": f"{limit} blogs from db"}

# 2
@app.get("/blog")
def index(limit,published:bool , sort : Optional[str] = None):
    # /blog?limit=10&published=true =>{"Blogs":"10 blogs from db"}
    if published:
        return {"Blogs": f"{limit} published blogs from db"}
    else :
        return {"Blogs": f"{limit} unpublished blogs from db"}

@app.get("/blog/unpublished")
def show():
    return {"Blog": "unpublished"}

@app.get("/blog/{id}")
def show(id: int):
# def show(id: str):
    return {"Blog": id}

@app.get("/blog/{id}/comments")
def comment(id):
    return {"About": {id : "comments"}}





# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}