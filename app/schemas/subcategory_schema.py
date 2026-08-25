from pydantic import BaseModel

class CreateSubcategorySchema(BaseModel):
    name: str
    slug: str | None = None
    category_id: str | None = None
    description: str | None = None
    image: str | None = None
    is_active: bool = True
    sort_order: int | None = None


