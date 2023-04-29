from blog.app import create_app
from flask import redirect, url_for

app = create_app()

if __name__ == '__main__':
    app.run()
    
    
@app.route('/')
def index():
    return redirect(url_for('auth.login'))