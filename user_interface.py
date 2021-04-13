from flask import Flask, redirect, url_for, render_template
from flask import request
import subprocess


from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home(result=None):

    ##Hangle Get Request

    if request.method == 'GET':
        if 'question' in request.args:
            question = request.args['question']


            url = 'http://0.0.0.0:4861/api/1.0/quizbowl/act'

            result = subprocess.check_output(['http', 'POST', 'http://0.0.0.0:4861/api/1.0/quizbowl/act', 'text='+question,'--ignore-stdin'])

            ## Only for debugging
            ## print(result)
            return render_template("index.html", result=result)

        return render_template("index.html", result=result)

##If user_interface.py is run then the server will start automatically.
if __name__ == "__main__":
    app.run(host="127.0.0.1")