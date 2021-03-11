from app import app # The first `app`, is the `app`-directory. The second `app` is the `app` created in the `__init__.py`-file: `app = Flask(__name__)`.

@app.route('/') # P.6 - These are 'decorators'.
@app.route('/index') # P.6 - You can chain decorators.
def index():
    user = {                # P12. Dummy-data.
        "username":"Dion", 
    }
    return """
<html>
    <head>
        <title>Homepage</title>
    </head>
    <body>
        <h1>Hello, """ + user['username'] + """!        
        </h1>
    </body>
</html>
"""

