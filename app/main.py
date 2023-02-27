from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def hello_world():
    return {"message": "สวัสดีชาวโลก(Hello World)"}