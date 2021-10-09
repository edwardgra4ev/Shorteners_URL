# Тестовый проект по сервису сокращения ссылок
## Запуск
___
```bash
python3.9 -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```
Файл `sql_app.db` содержит в базу данных

## Пример работы
Для создания сокращенного `URL` используеться `POST` метод `/create_short_url` который примает:
````json
{
    "name": "my_git",
    "url": "https://github.com/edwardgra4ev"
}
````
Результат: 
```json
{
    "short_url": "http://localhost:8000/my_git"
}
```
Где:

`name` это короткая ссылка
</br>
`url` ссылка которая будет заменена на коротку

Для переадресации используется `GET` метод `/{short_url}` где `short_url` ссылка сгенерированная сервисом 