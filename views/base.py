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

#Cette fonction est le point de depart de l'application.
@views.route('/resume')
def resume():
        return render_template('resume.html')

#Cette fonction est la page traitant de l'aspect medical
@views.route('/medical')
def medical():
        return render_template('medical.html')

#Cette fonction est la page traitant de l'aspect militaire
@views.route('/militaire')
def militaire():
        return render_template('militaire.html')

#Cette fonction est la page de presentation du groupe
@views.route('/groupe')
def groupe():
        return render_template('groupe.html')

#Cette fonction est la page de contact
@views.route('/contact')
def contact():
        return render_template('contact.html')

#Cette fonction est la page traitant des mentions legales
@views.route('/mentions_legales')
def mentions_legales():
        return render_template('mentions_legales.html')