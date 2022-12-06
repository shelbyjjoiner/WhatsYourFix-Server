rm db.sqlite3 
rm -rf ./WhatsYourFixApi/migrations
python3 manage.py migrate
python3 manage.py makemigrations WhatsYourFixApi
python3 manage.py migrate WhatsYourFixApi
python3 manage.py loaddata users
python3 manage.py loaddata NeuroUser 
python3 manage.py loaddata tokens
python3 manage.py loaddata hobbies 
python3 manage.py loaddata posts 
python3 manage.py loaddata comments 