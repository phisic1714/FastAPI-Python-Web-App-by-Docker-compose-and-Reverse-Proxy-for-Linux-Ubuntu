from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def hello_world():
    return {"ข้อความ(message)": "สวัสดีชาวโลก(Hello World)"}