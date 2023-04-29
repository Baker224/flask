from gunicorn.app.base import BaseApplication
from blog.app import create_app

class FlaskGunicornApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

app = create_app()
gunicorn_app = FlaskGunicornApplication(app, {'bind': '0.0.0.0:8000'})