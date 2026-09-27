from pydantic import BaseModel


class IngredientCreate(BaseModel):
    name: str
    category: str


class Ingredient(IngredientCreate):
    id: int