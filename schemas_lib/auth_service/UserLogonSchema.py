from pydantic import BaseModel, EmailStr


class UserLogonSchema(BaseModel):
    user_id: int
    email: EmailStr