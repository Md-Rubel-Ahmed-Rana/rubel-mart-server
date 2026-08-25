from pydantic import BaseModel

class CreateCategorySchema(BaseModel):
    name: str
    slug: str | None = None
    description: str | None = None
    image: str | None = None
    is_active: bool = True
    sort_order: int | None = None


