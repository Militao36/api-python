from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users

app = FastAPI(
    title="ApiTest"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    users.router,
    prefix='/users'
)


@app.get('/healthcheck', status_code=200)
async def health_check():
    return {'message': 'Asspi running'}
