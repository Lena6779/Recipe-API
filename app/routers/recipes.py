from fastapi import APIRouter, HTTPException

from app.schemas.recipe import Recipe, RecipeCreate

router = APIRouter(prefix="/recipes", tags=["Recipes"])

recipes_db: list[Recipe] = []
next_id = 1

@router.get("/", response_model=list[Recipe])
def list_recipes():
    return recipes_db


@router.get("/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: int):
    for recipe in recipes_db:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")


@router.post("/", response_model=Recipe, status_code=201)
def create_recipe(recipe_in: RecipeCreate):
    global next_id
    recipe = Recipe(id=next_id, **recipe_in.model_dump())
    recipes_db.append(recipe)
    next_id += 1  # Means that a new recipe gets assigned the next continuing number!
    return recipe