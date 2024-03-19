from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from typing import Set, Tuple

app = FastAPI()

class Item(BaseModel):
    name: str
    is_offer: Union[bool, None] = None
    price: float
@app.get("/")
async def read_root():
    return "This is root path from MyAPI"

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,  None] = None):
    return {"g": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"p": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}

def process_items(items: List[str], items_t:Tuple[int,int,str], items_s:Set[bytes]):
    for item in items:
        print(item)
    return items_s,items_t