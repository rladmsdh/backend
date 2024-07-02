from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi~"}

@app.get("/test")
async def test():
    return {"message": "TEST"}

# uvicorn 파일명:app --reload