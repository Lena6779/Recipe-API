from fastapi import APIRouter

from app.schemas.ingredient import Ingredient, IngredientCreate

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])

ingredients_db: list[Ingredient] = []
next_id = 1


@router.get("/", response_model=list[Ingredient])
def list_ingredients():
    return ingredients_db


@router.post("/", response_model=Ingredient, status_code=201)
def create_ingredient(ingredient_in: IngredientCreate):
    global next_id
    ingredient = Ingredient(id=next_id, **ingredient_in.model_dump())
    ingredients_db.append(ingredient)
    next_id += 1
    return ingredient