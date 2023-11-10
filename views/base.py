from flask import (
        Blueprint,
        render_template,
        send_from_directory,
        redirect,
        request,
        g)

views = Blueprint('main', __name__)

#Cette fonction est le point de depart de l'application.
@views.route('/')
def index():
	return render_template('index.html')