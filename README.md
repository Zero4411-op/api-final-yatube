# API для Yatube
## Описание

API для учебного проекта Yatube.

С его помощью можно:

получать список публикаций;

создавать, редактировать и удалять посты;

добавлять комментарии к публикациям;

просматривать сообщества;

подписываться на других пользователей;

получать JWT-токены для авторизации.


## Установка

Перейдите в папку проекта:

cd api-final-yatube

Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/Scripts/activate

Установите зависимости:

pip install -r requirements.txt

Перейдите в папку с файлом manage.py:

cd yatube_api

Выполните миграции:

python manage.py migrate

Запустите проект:

python manage.py runserver

После запуска проект будет доступен по адресу:

http://127.0.0.1:8000/

Документация API:

http://127.0.0.1:8000/redoc/

## Примеры

Получение списка постов:

GET /api/v1/posts/

Создание нового поста:

POST /api/v1/posts/

Пример запроса:

{
"text": "Новый пост",
"group": 1
}

Получение JWT-токена:

POST /api/v1/jwt/create/

Пример запроса:

{
"username": "your_username",
"password": "your_password"
}