# Магазин одежды

Задание 2, вариант 9. В каталоге можно выбрать любимый стиль и размер. Сохранённые предпочтения действуют в том же браузере 30 дней.

## Запуск

В PowerShell из этой папки:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py runserver
```

Откройте http://127.0.0.1:8000/. База данных не нужна.

## Проверка

```powershell
.\.venv\Scripts\python.exe manage.py test
```

На странице выберите «Спортивный» и размер M, нажмите «Сохранить» и обновите страницу: останется спортивная футболка. Кнопка «Сбросить» вернёт весь каталог.
