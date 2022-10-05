from typing import Union
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from monitoring.custom_logger import get_logger

load_dotenv()
logger = get_logger(__name__)
app = FastAPI()
# app.logger = get_logger(__name__)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/sum")
async def custom():
    a_value = 5
    b_value = 5
    logger.info(f"Sum is {a_value+b_value}")
    return f"Sum is {a_value+b_value}"


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)