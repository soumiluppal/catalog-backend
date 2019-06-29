from app.models.user import UserModel
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

def authenticate(username, password):
    user = UserModel.query.filter_by(username=username).first()
    print(user.full_name)
    if not user:
        return
    if check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.query.get_or_404(user_id)