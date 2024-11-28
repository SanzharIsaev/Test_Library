# Тестовое задание. 

## Внешние зависимости
Для работы проекта необходимы следующие зависимости:
- **Django**: Веб-фреймворк для разработки приложений на Python.
- **Django Rest framework**: библиотека, которая работает со стандартными моделями Django для создания гибкого и мощного API для проекта.


1. **Установка виртуального окружения**:
    ```bash
    python -m venv venv
    ```

2. **Активация виртуального окружения**:
    - На Windows:
        ```bash
        venv\Scripts\activate
        ```
    - На MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3. **Клонируйте репозиторий**:
   ```bash
   git clone {project_url}
   cd {repository_name}

4. **Установка зависимостей**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Применение миграций**:
    ```bash
    python manage.py migrate
    ```

6. **Создание суперпользователя** (по желанию):
    ```bash
    python manage.py createsuperuser
    ```

7. **Запуск сервера**:
    ```bash
    python manage.py runserver
    ```
