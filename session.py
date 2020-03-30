from flask import Flask
from flask import request
from flask import render_template
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = "suman@123"
#CREATE SESSION
@app.route('/')
def index():
    if 'hits' in session:
        session['hits'] = session.get('hits')+1
    else:
        session['hits'] = 1
    return("Total Hit Count = {}".format(session.get('hits')))

#DELETE SESSION
@app.route('/delete')
def delete():
    session.pop('hits', None)
    return("Session Deleted Successfully")

if __name__ == '__main__':
    app.run(debug=True, port=8080)