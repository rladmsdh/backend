from fastapi import FastAPI, Form
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

items = {"1": {"name": "Pen"}, "2": {"name": "Pencil"}}


@app.get("/items")
async def read_items():
    logger.info("Fetching all item")
    return items


@app.post("/items/{item_id}")
async def create_item(item_id: str, name: str = Form(...)):
    items[item_id] = {"name": name}
    logger.info(f"Item created : {item_id} - {name}")
    return items[item_id]


@app.put("/items/{item_id}")
async def update_item(item_id: str, name: str = Form(...)):
    items[item_id] = {"name": name}
    logger.info(f"Item update : {item_id} - {name}")
    return items[item_id]


@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    if item_id in items:
        del items[item_id]
        logger.info(f"Item deleted : {item_id}")
        return {"message": "Item deleted"}
    else:
        logger.info(f"Item not found: {item_id}")
        return {"message": "Item not found"}


@app.patch("/items/{item_id}")
async def patch_item(item_id: str, name: str = Form(...)):
    if item_id in items:
        items[item_id]["name"] = name
        logger.info(f"Item patched : {item_id} - {name}")
        return items[item_id]
    else:
        logger.info(f"Item not found: {item_id}")
        return {"message": "Item not found"}



#테스트
import requests

# FastAPI 서버 URL
base_url = "http://127.0.0.1:8000"


# 아이템 목록을 조회하는 함수
def get_items():
    response = requests.get(f"{base_url}/items")
    return response.json


# 아이템 목록 출력
def print_items(title, items):
    print(f"\n{title}: \n", items)


# GET 요청 테스트
def test_get_items():
    items_before = get_items()
    print_items("Before GET Request", items_before)
    response = requests.get(f"{base_url}/items")
    print("GET Response:", response.status_code, response.json())
    items_after = get_items()
    print_items("After GET Request", items_after)


# POST 요청 테스트
def test_create_item():
    items_before = get_items()
    print_items("Before POST Request", items_before)
    response = requests.post(f"{base_url}/items/3", data={"name": "Notebook"})
    print("POST Response:", response.status_code, response.json())
    items_after = get_items()
    print_items("After POST Request", items_after)
