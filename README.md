# Site Groupe controverse

Site pour controverse du numerique Polytech IG

## install

precond :

```
apt-get install python3-venv
```

then :

```
git clone https://github.com/Alexandre-Roussel48/ControverseSite.git
cd ControverseSite
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## run (development mode)

```
	rundev.sh

source venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=server.py
flask run
```

## run (server mode)

```
	run.sh

kill $(cat ControverseSite.pid)
source venv/bin/activate
gunicorn --daemon -b '0.0.0.0:80' --pid=ControverseSite.pid --error-log=./errors.log server:app
```
