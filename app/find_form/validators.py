from datetime import datetime
from app.find_form.schemas import ValidateEmail


def is_date(value: str) -> bool:
    """Проверяет, является ли значение датой"""
    date_formats = ["%Y-%m-%d", "%d.%m.%Y"]
    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            continue
    return False


def is_phone(value: str) -> bool:
    """Проверяет, является ли значение номером телефона в формате +7 xxx xxx xx xx"""
    parts = value.split()
    if len(parts) == 5 and parts[0] == "+7" and all(p.isdigit() for p in parts[1:]):
        return all(
            (
                len(parts[1]) == 3,
                len(parts[2]) == 3,
                len(parts[3]) == 2,
                len(parts[4]) == 2,
            )
        )
    return False


def is_email(value: str) -> bool:
    """Проверяет, является ли значение валидным email"""
    try:
        ValidateEmail(email=value)
        return True
    except Exception:
        return False
