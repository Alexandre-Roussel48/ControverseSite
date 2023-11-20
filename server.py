from flask import Flask, request, redirect, url_for, g, render_template
from itsdangerous import (
        TimedSerializer,
        SignatureExpired,
        BadSignature)

import config

app = Flask('__name__')

app.config.from_pyfile('config.py')

from views import (
    base
)

app.register_blueprint(base.views)

if __name__ == '__main__':
    app.run('0.0.0.0')