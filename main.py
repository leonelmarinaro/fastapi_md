from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/app2")
async def app2():
    return {"message": "App dos"}


# Documentación
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

# POST GET PUT DELETE
