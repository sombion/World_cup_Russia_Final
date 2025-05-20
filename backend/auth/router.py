from fastapi import APIRouter, Depends, Response
from backend.auth.dao import UsersDAO
from backend.auth.dependencies import get_current_user
from backend.auth.models import Users
from backend.auth.schemas import SEdinUsername, SEditPassword, SUserAuth, SUserRegister
from backend.auth.service import edit_password, login_user, register_user

router = APIRouter(
    prefix='/api/auth',
    tags=['Авторизация']
)


@router.get("/me", description="Просмотр данных о текущем пользователе")
async def api_get_me(current_user: Users = Depends(get_current_user)) -> dict:
    return await UsersDAO.find_by_id(current_user.id)

@router.post("/register", description="Регистрация")
async def api_register_user(user_data: SUserRegister) -> dict:
    return await register_user(
        username=user_data.username,
        login=user_data.login,
        password=user_data.password,
        is_admin=user_data.is_admin
    )

@router.post("/login", description="Авторизация")
async def api_auth_user(response: Response, user_data: SUserAuth) -> dict:
    login_data = await login_user(login=user_data.login, password=user_data.password)
    access_token = login_data["access_token"]
    response.set_cookie(key="pc_access_token", value=access_token, httponly=True)
    del login_data["access_token"]
    return login_data

@router.post("/logout", description="Выход из записи")
async def api_logout_user(response: Response) -> dict:
    response.delete_cookie(key="pc_access_token")
    return {'detail': 'Пользователь успешно вышел из системы'}

@router.patch("/edit-username", description="Изменение имени")
async def api_edit_username(user_new_data: SEdinUsername, current_user: Users = Depends(get_current_user)):
    await UsersDAO.update(user_id=current_user.id, username=user_new_data.username)
    return {"detail": "Имя пользователя испешно изменено"}

@router.patch("/edit-password", description="Изменение пароля")
async def api_edit_username(user_data: SEditPassword, current_user: Users = Depends(get_current_user)):
    return await edit_password(
        last_password=user_data.last_password,
        new_password=user_data.new_password,
        user_id=current_user.id
    )