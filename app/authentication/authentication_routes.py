#
# Blueprint: Authentication
#
# >> Make sure to import bp as the correct blueprint <<
#
from app.authentication import bp

from flask import jsonify, g
from app import auth
from app.authentication import authentication_service as auth_service


#
# Generate a new API token
#
@bp.route('/auth/token')
@auth.login_required
def get_auth_token():
    token = auth_service.generate_auth_token(60 * 60 * 24 * 7)
    return jsonify({'token': token.decode('ascii'), 'duration': 60 * 60 * 24 * 7})


@bp.route('/')
def index():
    return 'Hello, World!'
