"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""


import logging
from pathlib import Path

from constants import BASE_PROJECT_PATH
import os

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    log_file = Path(__file__).parent / "login_system.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(message)s - %(levelname)s',
        force=True
    )

    # Логування події
    if status == "success":
        logging.info(log_message)
    elif status == "expired":
        logging.warning(log_message)
    else:
        logging.error(log_message)
