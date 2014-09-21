from flask import Flask

def make_app(app_name):
    app = Flask(app_name)

    # Load configuration.
    # conf_file = os.environ.get("CONFIG", None)
    # if not conf_file:
    #     raise Exception("Missing CONFIG environment variable with the configuration")
    # app.config.from_pyfile(conf_file)
    app.config.from_object('config')

    if app.config['DEBUG']:
        app.testing = True

    return app

# Flask application.
app = make_app("Zair")

# Debugging.
#toolbar = DebugToolbarExtension(app)

config = app.config
