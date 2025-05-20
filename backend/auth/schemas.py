from pydantic import BaseModel, Field

class SUserRegister(BaseModel):
    username: str = Field(..., description="Имя")
    login: str = Field(..., description="Логин")
    password: str = Field(..., description="Пароль")
    is_admin: bool = Field(..., description="Является ли пользователь администратором")

class SUserAuth(BaseModel):
    login: str = Field(..., description="Логин")
    password: str = Field(..., description="Пароль")

class SEdinUsername(BaseModel):
    username: str = Field(..., description="Новое имя")

class SEditPassword(BaseModel):
    last_password: str = Field(..., description="Старый пароль")
    new_password: str = Field(..., description="Новый пароль")