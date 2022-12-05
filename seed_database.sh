rm db.sqlite 3 
rm -rf ./WhatsYourFixApi/migrations
python3 manage.py migrate
python3 manage.py makemigrations WhatsYourFixApi
python3 manage.py migrate WhatsYourFixApi
python3 manage.py loaddata comments 
python3 manage.py loaddata hobbies 
python3 manage.py loaddata NeuroUser 
python3 manage.py loaddata posts 