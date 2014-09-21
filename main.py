import os

import flask_app
from zair import __all__

app = flask_app.app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=app.config['DEBUG'])
