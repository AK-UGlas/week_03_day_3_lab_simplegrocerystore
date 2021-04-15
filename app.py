from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=timedelta(seconds=1)

from controllers import controller

if __name__ == "__main__":
    app.run(debug=True)