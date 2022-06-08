<img alt="Issues" src="https://img.shields.io/github/issues/Project-room2/github-readme-stats?color=0088ff" />  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/Project-room2/github-readme-stats?color=0088ff" />  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/w/Project-room2/habr?style=plastic" />                                             

   
# **ПРОЕКТ "XABR"**
___
## Сайт обмена полезной информацией и формирование базы знаний для образовательной экосистемы
Командная разработка по методологии Agile:Scrum 

март-июнь 2022

GeekBrains, факултет Python-разработки, группа GU_python_742 (09.11.2020)
____

### Команда

- Евгения
- Владимир
- Вячеслав
- Дмитрий - https://github.com/dr2moscow | https://t.me/dr2moscow

### :fire: Статистика (Statistic) :
![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=Project-room2)
<img src="https://github-readme-stats.vercel.app/api?username=Project-room2&show_icons=true&line_height=27&count_private=true" />



### Технический стек (Technologies) :
* Python
* Postres 
* Javascript
* GitHub
* Django
* Jenkins
* Yougile
* Bootstrap
* HTML5/CSS3

### Базовая документация к проекту :
Основные системные требования:

* Ubuntu 20.04 LTS
* Python 3.10
* PostgreSQL 12
* Django 4.4
* Gunicorn 20.1.0
* Nginx 1.18.0
* Зависимости (Python) из requirements.txt

### Установка необходимого ПО (Setup) :
#### Рекомендуемая подготовка системы
обновляем информацию о репозиториях
```
sudo apt-get update && sudo apt-get upgrade -y
```
Установка окружения
```
sudo apt-get install git-core
sudo apt-get install python-setuptools 
sudo apt-get install python-dev
sudo apt-get install python3-pip
```

#### Копируем проект на сервер
```
mkdir habr
cd habr
sudo git clone [git@github.com:Project-room2/habr.git](https://github.com/Project-room2/habr.git)
```

#### Создаем виртуальное окружение (из папки /home/kbook/knackbook)
```
sudo apt-get install python3-venv
python -m venv env
```  

#### Активируем виртуальное окружение
```
source env/bin/activate
```

#### Настраиваем виртуальное окружение
Ставим зависимости
```
pip install -r requirements.txt
```

#### Устанавливаем базу данных postgresql
```
sudo apt-get install postgresql postgresql-contrib 
sudo apt-get install libpq-dev
```
(psycopg2-binary уже установлен из requirements.txt)


После установки проверяем статус СУБД, командой:
```
sudo service postgresql status
```

#### Настраиваем базу данных postgresql

запуск режима работы с базой (интерпретатор команд сервера)
```
sudo -u postgres psql
```

создаем БД
```
CREATE DATABASE habr;
```

Создаем пользователя
```
CREATE USER "habr_user" with NOSUPERUSER PASSWORD 'PASSWORD';
```

Привилегии
```
GRANT ALL PRIVILEGES ON DATABASE habr_user TO "habr";
```

Кодировка 'UTF8'
```    
ALTER ROLE "habr" SET CLIENT_ENCODING TO 'UTF8';
```

Устанавливается уровень изоляции
```
ALTER ROLE "habr" SET default_transaction_isolation TO 'READ COMMITTED';      
```
Выставляем TIME ZONE
```
ALTER ROLE "habr" SET TIME ZONE 'Europe/Moscow';
```
Для выхода пишем «\q».

проверка статуса
```
sudo systemctl status postgresql
```
перезапуск сервера
```
sudo systemctl restart postgresql
```

#### заполняем файл настройки проекта

```
nano ./install/env.json
```
```
"DOMAIN_NAME" : "http://(IP-адрес):8000",
"POSTGRE_DB" : "habr",
"POSTGRE_USER" : "habr_user",
"POSTGRE_PASSWORD" : "PASSWORD"
"EMAIL_PASSWORD": "(пароль для почты сервиса)"
```

#### Выполнение миграций и сбор статических файлов проекта
Выполняем миграции:
```
python manage.py makemigrations
```
Собираем статику:
```
python manage.py migrate
```

#### Создаем Суперпользователь (администратора проекта)
```
python manage.py createsuperuser
```

#### Заполнить базу данных тестовыми данными
```
python manage.py loaddata ./install/tests_db.json 
```

#### Тест запуска   проекта
```
python manage.py runserver
```

#### Устанавливаем nginx
```
sudo apt-get install nginx
```
проверяем: в браузере вводим IP-адрес
получаем сообщение: Welcome to nginx!

#### Устанавливаем модуль gunicorn (веб-сервер)
```
pip install gunicorn
```

Активирование и запуск сервиса
```
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```
Настройки параметров для nginx
```
sudo nano /etc/nginx/sites-available/habr
```

#### Активировируем сайт
```
sudo ln -s /etc/nginx/sites-available/habr /etc/nginx/sites-enabled
```

#### Устанавливаем права для чтения 755
```
sudo chmod -R 755 /home/habr/project/habr/
```

Перезапускаем nginx и gunicorn
```
sudo systemctl restart nginx
sudo systemctl restart gunicorn
```

### После этого в браузере можно ввести ip-адрес сервера и откроется проект
```
https://(IP-адрес)
```

для просмотра технической документации к проекту введите:
```
https://(IP-адрес)/html/
```
