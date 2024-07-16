# paw_finder
PawFinder is a service that uses AI to find lost pets through photo recognition. The service includes a Telegram bot for users to search for their pets and a web-based CRM for shelters to manage found animals and related data.

# PawFinder

PawFinder - сервис по поиску потерянных животных по фото с помощью ИИ. Поиск осуществляется через Telegram-бота, а на сайте предоставляется упрощенная CRM для управления данными о найденных животных и приютах.

## Установка

### Требования

- Python 3.8+
- PostgreSQL
- Docker
- Docker Compose

### Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/yourusername/pawfinder.git
    cd pawfinder
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  # В Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` со следующим содержимым:

    ```env
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
    ```

5. Инициализируйте базу данных:

    ```bash
    alembic upgrade head
    ```

### Запуск приложения

1. Запустите приложение с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

2. Приложение будет доступно по адресу `http://localhost:8000`.


### Модели данных

#### User (Пользователь)

Пользователи системы, такие как обычные пользователи, сотрудники приютов и администраторы.

- `id` (Integer): Уникальный идентификатор пользователя
- `username` (String): Имя пользователя
- `email` (String): Электронная почта пользователя
- `hashed_password` (String): Хешированный пароль пользователя
- `is_active` (Boolean): Флаг активности пользователя
- `is_superuser` (Boolean): Флаг суперпользователя
- `is_verified` (Boolean): Флаг подтверждения пользователя
- `role` (String): Роль пользователя
- `shelter_id` (Integer, nullable): Идентификатор приюта, к которому привязан пользователь
- `is_blocked` (Boolean): Флаг блокировки пользователя
- `created_at` (DateTime): Дата и время создания пользователя
- `updated_at` (DateTime): Дата и время последнего обновления пользователя
- `deleted_at` (DateTime, nullable): Дата и время удаления пользователя

#### Role (Роль)

Роли пользователей для управления доступом к ресурсам.

- `id` (Integer): Уникальный идентификатор роли
- `name` (String): Название роли
- `user_id` (Integer): Идентификатор пользователя, которому принадлежит роль

#### Shelter (Приют)

Приюты для животных.

- `id` (Integer): Уникальный идентификатор приюта
- `name` (String): Название приюта
- `phone` (String): Телефон приюта
- `email` (String): Электронная почта приюта
- `website` (String): Веб-сайт приюта
- `approved` (Boolean): Флаг одобрения приюта
- `is_blocked` (Boolean): Флаг блокировки приюта
- `created_at` (DateTime): Дата и время создания приюта
- `updated_at` (DateTime): Дата и время последнего обновления приюта
- `deleted_at` (DateTime, nullable): Дата и время удаления приюта

#### ShelterAddress (Адрес приюта)

Адреса приютов.

- `id` (Integer): Уникальный идентификатор адреса
- `shelter_id` (Integer): Идентификатор приюта
- `address` (String): Адрес
- `city` (String): Город
- `state` (String): Штат/Регион
- `zip_code` (String): Почтовый индекс
- `country` (String): Страна
- `latitude` (Float, nullable): Широта
- `longitude` (Float, nullable): Долгота
- `created_at` (DateTime): Дата и время создания адреса
- `updated_at` (DateTime): Дата и время последнего обновления адреса

#### Animal (Животное)

Информация о животных.

- `id` (Integer): Уникальный идентификатор животного
- `name` (String): Имя животного
- `species` (String): Вид животного
- `breed` (String): Порода животного
- `color` (String): Окрас животного
- `age` (Integer): Возраст животного
- `description` (String): Описание животного
- `special_markings` (String): Особые отметки
- `status` (String): Статус животного (например, найдено, усыновлено)
- `shelter_id` (Integer, nullable): Идентификатор приюта
- `is_searching` (Boolean): Флаг поиска животного
- `search_user_id` (Integer, nullable): Идентификатор пользователя, который ищет животное
- `created_at` (DateTime): Дата и время создания записи о животном
- `updated_at` (DateTime): Дата и время последнего обновления записи о животном
- `deleted_at` (DateTime, nullable): Дата и время удаления записи о животном

#### AnimalHistory (История животного)

История перемещений и изменений статусов животных.

- `id` (Integer): Уникальный идентификатор истории
- `animal_id` (Integer): Идентификатор животного
- `status` (String): Статус животного
- `shelter_id` (Integer, nullable): Идентификатор приюта
- `new_shelter_id` (Integer, nullable): Идентификатор нового приюта
- `timestamp` (DateTime): Временная метка записи
- `details` (String, nullable): Дополнительные детали

#### Photo (Фото)

Фотографии животных.

- `id` (Integer): Уникальный идентификатор фото
- `animal_id` (Integer): Идентификатор животного
- `image` (String): URL или путь к изображению
- `uploaded_at` (DateTime): Дата и время загрузки фото

#### Report (Отчет)

Отчеты о найденных животных.

- `id` (Integer): Уникальный идентификатор отчета
- `user_id` (Integer): Идентификатор пользователя, создавшего отчет
- `animal_id` (Integer): Идентификатор животного
- `location` (String): Местоположение, где было найдено животное
- `date_found` (DateTime): Дата и время, когда было найдено животное
- `description` (String): Описание отчета
