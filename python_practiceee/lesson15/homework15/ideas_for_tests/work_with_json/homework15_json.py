import json
import os
import logging

from constants import BASE_PROJECT_PATH


logging.basicConfig(
    filename="error-json.log",
    level=logging.ERROR,
    format="%(levelname)s: %(message)s")

for current_path, folders, files in os.walk(BASE_PROJECT_PATH):
    for file in files:
        if file.endswith(".json"):
            full_path = os.path.join(current_path, file)

            try:
                with open(full_path, encoding="utf-8") as json_file:
                    json.load(json_file)
            except json.JSONDecodeError:
                logging.error(f"{file} is not valid")









