from fastapi import Response
from backend.auth.auth import authenticate_user, create_access_token, get_password_hash, verify_password
from backend.auth.dao import UsersDAO
from backend.auth.models import Users
from backend.exceptions import IncorrectPasswordException, UserAlreadyExistsException
from backend.profile.dao import ProfileDAO
from backend.skills.dao import SkillsDAO
from backend.statistics.dao import StatisticsDAO


async def register_user(
    username: str,
    login: str,
    password: str,
    is_admin: bool
):
    user = await UsersDAO.find_one_or_none(login=login)
    if user:
        raise UserAlreadyExistsException
    hash_password = get_password_hash(password)
    user_id = await UsersDAO.add(
        username=username,
        login=login,
        hash_password=hash_password,
        is_admin=is_admin
    )
    statistics_data = await StatisticsDAO.add(0, 1, 0, 0, 45)
    skills_data = await SkillsDAO.add(1, 1, 1, 1, 0, 1)
    await ProfileDAO.add(user_id, statistics_data.id, skills_data.id)
    return {'detail': 'Вы успешно зарегистрированы!'}

async def login_user(login: str, password: str):
    user = await authenticate_user(login=login, password=password)
    access_token = create_access_token({"sub": str(user.id)})
    return {'access_token': access_token, 'detail': 'Вы успешно вошли!'}

async def edit_password(last_password: str, new_password: str, user_id: int):
    user: Users = await UsersDAO.find_one_or_none(id=user_id)
    if not verify_password(last_password, user.hash_password):
        raise IncorrectPasswordException
    hash_password = get_password_hash(new_password)
    await UsersDAO.update(user_id=user_id, hash_password=hash_password)
    return {"detail": "Пароль испешно изменен"}