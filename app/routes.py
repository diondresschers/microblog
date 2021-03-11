from app import app

@app.route('/') # P6 - These are 'decorators'.
@app.route('/index')
def index():
    return "Hello, World"
