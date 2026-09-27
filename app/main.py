from fastapi import FastAPI

from app.config import APP_DESCRIPTION, APP_TITLE, APP_VERSION
from app.routers import ingredients, recipes

app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
)

app.include_router(recipes.router)
app.include_router(ingredients.router)


@app.get("/")
def root():
    return {"message": "Recipe API is running"}