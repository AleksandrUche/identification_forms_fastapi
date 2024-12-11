from app.database import database
from app.find_form.validators import is_date, is_phone, is_email


def detect_field_type(value: str):
    """Определяет тип поля"""
    if is_date(value):
        return "date"

    if is_phone(value):
        return "phone"

    if is_email(value):
        return "email"

    return "text"


def find_form(data: dict):
    available_templates = database.all()

    field_types = {key: detect_field_type(value) for key, value in data.items()}

    for template in available_templates:
        template_fields = template["fields"]

        is_match = all(
            key in field_types and template_fields[key] == field_types[key]
            for key in template_fields
        )
        if is_match:
            return {"template_name": template["name"]}

    return field_types
