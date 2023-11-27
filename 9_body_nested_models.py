from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    # The string will be checked to be a valid URL, and documented in JSON Schema / OpenAPI as such.
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    # if you receive a request with duplicate data, it will be converted to a set of unique items.
    tags: set[str] = set()
    images: list[Image] | None = None


# Set types &  Nested Models
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    This would mean that FastAPI would expect a body similar to:
    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": ["rock", "metal", "bar"],
        "image": {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }
    }
    """
    return {"item_id": item_id, "item": item}
