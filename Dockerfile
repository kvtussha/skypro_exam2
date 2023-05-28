FROM python:3.10-slim
# устанавливает в образ указанную версию питона
# slim - упрощенная версия

WORKDIR /code
# в образе будет создана папка, куда будут сохраняться все дальнейшие действия
COPY requirements.txt .
# копируется файл с зависимостями в текущую созданную директорию - code
RUN pip install -r requirements.txt
# устанавливаются все зависимости в образ
COPY . .
# копирует весь проект в директорию code
COPY configs/docker_config.py configs/default_config.py
# default_config заменяется на docker_config
# default_config нужен в процессе разработки, чтобы docker работал нужен docker_config


# config -> default_config, переименовали
# default_config копируем в только что созданный файл docker_config
# в docker_config меняем SQLALCHEMY_DATABASE_URI = 'sqlite:///notes.db' на SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:flask_app_password@pg/flask_app"
# создаем docker_ci_config, копируем туда docker_config, но меняем SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:flask_app_password@pg/flask_app"
# на SQLALCHEMY_DATABASE_URI = "postgresql://$DB_USER:$DB_PASSWORD@pg/$DB_NAME"

# docker hub: create repository
# создать docker-compose.yaml


CMD flask run -h 0.0.0.0 -p 80
