from flask import Flask, request, redirect, url_for, g, render_template
from itsdangerous import (
        TimedSerializer,
        SignatureExpired,
        BadSignature)

app = Flask('__name__')

from views import (
    base
)

app.register_blueprint(base.views)

if __name__ == '__main__':
    app.run('0.0.0.0')
