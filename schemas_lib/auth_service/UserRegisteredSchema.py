from pydantic import BaseModel, EmailStr


class UserRegisteredSchema(BaseModel):
    user_id: int
    email: EmailStr