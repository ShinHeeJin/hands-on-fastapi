from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    # In Pydantic version 2, you would use the attribute model_config
    # that takes a dict as described in Pydantic's docs: Model Config.
    # https://docs.pydantic.dev/latest/api/config/
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Foo", "description": "A very nice Item", "price": 35.4, "tax": 3.2},
            ]
        }
    }


# Extra JSON Schema data in Pydantic models
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}
