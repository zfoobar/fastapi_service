from fastapi import FastAPI
from routes import health, quotes, characters

app = FastAPI()

app.include_router(quotes.router)
app.include_router(characters.router)
app.include_router(health.router)

