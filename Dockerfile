FROM python:3.10-slim
# Устанавливает в образ указанную версию питона
# slim - упрощенная версия

WORKDIR /code
# В образе будет создана папка, куда будут сохраняться все дальнейшие действия
COPY requirements.txt .
# Копируется файл с зависимостями в текущую созданную директорию - code
RUN pip install -r requirements.txt
# Устанавливаются все зависимости в образ
COPY . .
# Копирует весь проект в текущую директорию

# default_config нужен в процессе разработки, чтобы docker работал нужен docker_config
# config -> default_config, переименовали
# default_config копируем в только что созданный файл docker_config
# в docker_config меняем SQLALCHEMY_DATABASE_URI = 'sqlite:///notes.db' на SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:flask_app_password@pg/flask_app"
# создаем docker_ci_config, копируем туда docker_config, но меняем SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:flask_app_password@pg/flask_app"
# на SQLALCHEMY_DATABASE_URI = "postgresql://$DB_USER:$DB_PASSWORD@pg/$DB_NAME"

# docker hub: create repository
# создать docker-compose.yaml


CMD flask run -h 0.0.0.0 -p 80
# После создания образа выполняется команда запуска приложения
