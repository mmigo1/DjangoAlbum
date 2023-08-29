# Album API
Приложения представляет из себя каталог исполнителей и их альбомов, собранных при помощи DRF.
## Установка
По умолчанию докер будет использовать порт 8000.
1)Используйте docker-compose что бы построить образ
```sh
docker-compose build
```
2)Выполните миграции
```sh
docker compose run --rm web-app sh -c "python manage.py migrate"
```
3)Создайте суперпользователя
```sh
docker compose run --rm web-app sh -c "python manage.py createsuperuser"
```
4)Запустите образ
```sh
docker-compose up
```
## Примеры запросов к API

Приложение работает по адресу http://localhost:8000/ и использует Swagger по адресу http://localhost:8000/swagger/

1)admin/ - служит для входа в панель администратора и взаимодействия с БД
2)/api/album - служит для взаимодействия с моделью "Альбом"
3)/api/song  - служит для взаимодействия с моделью "Песня"
4)/api/performer  -служит для взаимодействия с моделью "Исполнитель"
