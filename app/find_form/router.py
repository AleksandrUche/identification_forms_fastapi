from fastapi import APIRouter, Request

from app.find_form.service import find_form

router = APIRouter()


@router.post("/get_form", summary='Определить форму')
async def get_form(request: Request):
    """Определяет подходящий шаблон формы или типизирует поля"""
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}

    return find_form(data)
