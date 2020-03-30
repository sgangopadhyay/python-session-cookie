from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = "suman@123"

#CREATE COOKIE
@app.route('/')
def index():
    cookie = make_response("Creating a Cookie")
    cookie.set_cookie('name', 'suman gangopadhyay', max_age = 60*60)
    return(cookie)

# COOKIE READ
@app.route('/read')
def read():
    if request.cookies.get('name'):
        cookie = make_response("Display Cookie : {}".format(request.cookies.get('name')))
    else:
       cookie = make_response("Creating a Cookie")
       cookie.set_cookie('name', 'suman gangopadhyay', max_age = 60*60)
    return(cookie)

# DELETE COOKIE
@app.route('/delete')
def delete():
    cookie = make_response("Deleting a Cookie")
    cookie.set_cookie('name', 'suman gangopadhyay', max_age = 0)
    return(cookie)


if __name__ == '__main__':
    app.run(debug=True, port=9000)