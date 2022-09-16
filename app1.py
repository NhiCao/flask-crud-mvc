# from flask import Flask, render_template
# from flask_migrate import Migrate

# from app.models.user import db
# from app.routes.user_bp import user_bp

# db = SQLAlchemy()

# app = Flask(__name__)
# app.config.from_object('config')

# db.init_app(app)
# migrate = Migrate(app, db)

# app.register_blueprint(user_bp, url_prefix='/users')

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=5000)







# from flask import render_template
# from flask_migrate import Migrate

# from app.routes.user_bp import user_bp
# from app import create_app

# app = create_app()

# app.register_blueprint(user_bp, url_prefix='/users')

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=5000)








# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>So bad to have to say goodbye.</p>"






import os
import config

from flask import render_template

from app.routes.user_bp import user_bp
from app import create_app

environ = os.environ.get('FLASK_ENV')

config_app = config.LocalConfig
if environ == 'PRODUCTION':
    config_app = config.ProductionConfig
elif environ == 'TESTING':
    config_app = config.TestingConfig
elif environ == 'LOCAL':
    config_app = config.LocalConfig

app = create_app(config_app)
print(environ)
print("------------------")

app.register_blueprint(user_bp, url_prefix='/users')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)







