from pydantic import BaseModel

class CreateBrandSchema(BaseModel):
    name: str
    description: str | None = None
    logo: str | None = None
    website: str | None = None
    is_active: bool = True
    sort_order: int | None = None

 