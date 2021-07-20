создание локальной сети local-apps
```bash
docker network create local-apps
```

загрузка образа docker
```bash
docker pull postgres:13.2-alpine
```

создание папки хранения БД
```bash
mkdir -p ~/Documents/storedata/pg-data
```

создание контейнера БД 
```bash
docker run --name local-pg13 \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_INITDB_ARGS="--locale=C.UTF-8" \
    -v ~/Documents/storedata/pg-data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network="local-apps" \
    --restart always \
    -d postgres:13.2-alpine
```

вход в докер
```bash
docker exec -it local-pg13 psql -U postgres
```

создание пользователя surveys для БД 
создание БД surveys
```sql
CREATE USER surveys CREATEDB LOGIN PASSWORD 'surveys_password';
CREATE DATABASE surveys WITH OWNER = surveys CONNECTION LIMIT = -1;
GRANT ALL PRIVILEGES ON DATABASE surveys to surveys;
```


создание папки хранения backend на сервере и клонирование в нее проекта из репозитория
```bash
mkdir surveys
```

запуск контейнера АПИ и миграций
```bash
docker run -d --name surveys_image --network="local-apps" -p 8000:8000 -v ~/surveys:/surveys surveys_docker
```

```bash
docker run --rm --network="local-apps" -v ~/surveys:/surveys \
  surveys_docker python3 ./manage.py migrate
```
