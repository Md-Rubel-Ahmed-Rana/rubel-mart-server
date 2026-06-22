from pydantic import BaseModel, EmailStr, Field

class RegisterSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str = Field(
        min_length=6,
        max_length=72
    )


class UpdateUserSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str | None = None
    image: str | None = None