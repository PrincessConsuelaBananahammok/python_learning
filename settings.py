from dynaconf import Dynaconf
from os.path import join
from constants import BASE_PROJECT_PATH

settings = Dynaconf(
    settings_file=[join(BASE_PROJECT_PATH, "base_settings.ini")],
    environments=True,
    envvar_prefix="DYNACONF",
    load_dotenv=True
)