FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD flask run -h 0.0.0.0 -p 80

# FROM python:3.10-slim - устанавливает в образ указанную версию питона
# slim - упрощенная версия

# WORKDIR /code - В образе будет создана папка, куда будут сохраняться все дальнейшие действия
# COPY requirements.txt . - Копируется файл с зависимостями в текущую созданную директорию - code
# RUN pip install -r requirements.txt - Устанавливаются все зависимости в образ
# COPY . . - Копирует весь проект в текущую директорию
# CMD flask run -h 0.0.0.0 -p 80 - После создания образа выполняется команда запуска приложения
