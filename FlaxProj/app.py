from os import name
import flask as f
import datetime

from flask import sessions
from werkzeug.utils import redirect

app = f.Flask(__name__)
app.secret_key = '111'

@app.route('/')
def home():
    if "username" in  f.session:
        userName =  f.session["username"]
    else: 
        userName = "Stranger"
    return f"<h1>Wellcome to the home page {userName}!<h1>"


@app.route('/firstCV')
def cv1():
    return f.redirect('CVgrid.html')


@app.route('/ContactUs')
def cu():
    return f.render_template('forms.html')


@app.route('/cv')
def cv():
    return f.render_template('cv1.html')


@app.route('/cv2')
def cv2():
    return f.render_template('cv2.html')


@app.route('/assignment8')
def asg8():
    return f.render_template('assignment8.html', time=datetime.datetime.now().time().hour)


users = {'0': {'name': 'Yossi', 'email': 'yo@gmail.com', 'password': '1111'},
         '1': {'name': 'Kelly', 'email': 'Kel@gmail.com', 'password': '2222'},
         '2': {'name': 'Ron', 'email': 'Ron@gmail.com', 'password': '3333'},
         '3': {'name': 'Raz', 'email': 'Raz@gmail.com', 'password': '4444'},
         '4': {'name': 'Tal', 'email': 'Tal@gmail.com', 'password': '5555'}}


@app.route('/assignment9', methods=['GET', 'POST'])
def asg9():
    if f.request.method == 'GET':
        if 's-us' in f.request.args:
            us_name = f.request.args['s-us']
            us_email = f.request.args['s-em']
            if us_name and us_email:
                chosen = [users[user]
                          for user in users if us_name in users[user]['name'] and us_email in users[user]['email']]
            if us_name and not us_email:
                chosen = [users[user]
                          for user in users if us_name in users[user]['name']]
            if not us_name and us_email:
                chosen = [users[user]
                          for user in users if us_email in users[user]['email']]
            if not us_name and not us_email:
                chosen = [users[user] for user in users]
            return f.render_template('assignment9.html', usersList=chosen)
  
    if f.request.method == 'POST':
        username = f.request.form['r-us']
        emai = f.request.form['r-em']
        password = f.request.form['r-pass']
        f.session["username"] = username
        users[len(users)] = {
            'name': username,
            'email': emai,
            'password': password
        }
        return f.render_template('assignment9.html')

    return f.render_template('assignment9.html')


@app.route('/logout')
def logout():
    f.session.pop("username", None)
    return f.redirect('/assignment9')

if __name__ == '__main__':
    app.run(debug=True)
