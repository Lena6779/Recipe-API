from pydantic import BaseModel


class RecipeCreate(BaseModel):
    title: str
    cuisine: str
    prep_time_minutes: int
    servings: int


class Recipe(RecipeCreate):
    id: int