from flask import Flask # type: ignore
from views.user_view import user_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
