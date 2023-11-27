from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    user_name: str
    full_name: str | None = None


# Mix Path, Query and body parameters
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,  # optional
):
    result = {"item_id": item_id}
    if q:
        result |= {"q": q}
    if item:
        result |= {"item": item}
    return None


# Multiple body parameters
@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item, user: User):  # required item & user
    """
    Request Example
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "dave",
            "full_name": "Dave Grohl"
        }
    }
    """
    return {"item_id": item_id, "item": item, "user": user}