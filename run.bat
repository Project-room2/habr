@echo loading modules for the project
pip install -r requirements.txt

@echo collect the project
python manage.py makemigrations

@echo building the project database
python manage.py migrate

@echo run web server
python manage.py runserver --settings=Habr.settings.local