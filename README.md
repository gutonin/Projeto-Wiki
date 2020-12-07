Instalação

Clone o projeto:
git clone https://github.com/gutonin/projeto-wiki
cd projeto-wiki

virtualenv:
virtualenv venv -p python3

Linux:
source env/bin/activate

Windows:
env\Scripts\activate.bat

Instale as dependencias:
pip install -r requirements.txt
python manage.py runserver