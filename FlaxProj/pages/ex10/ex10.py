from distutils.log import error
import flask as f
from inter_db import inter_db
import requests

assignment10 = f.Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    template_folder='tamplates',
    static_url_path='/static/'
)


def insert(req):
    username = req.form['is_name']
    email = req.form['is_email']
    password = req.form['is_pass']

    query = "insert into users (username, email, password) values('%s', '%s', '%s')" % (
        username, email, password)
    if inter_db(query, 'commit'):
        alertMsg = "A new user was inserted!"
    else:
        alertMsg = "No new user was inserted!"
    query_text = 'select * from users'
    users = inter_db(query_text, 'fetch')
    return f.render_template('Ex10Base.html', usersList=users, msg=alertMsg)


def update(req):
    old_email = req.form['up_o_email']
    new_us = req.form['up_name']
    new_em = req.form['up_email']
    new_pss = req.form['up_pass']
    query = "UPDATE users SET username = '%s', email = '%s', password = '%s' WHERE email = '%s'" % (
        new_us, new_em, new_pss, old_email)
    if inter_db(query, 'commit'):
        alertMsg = "User was updated!"
    else:
        alertMsg = "User not found"
    query_text = 'select * from users'
    users = inter_db(query_text, 'fetch')
    return f.render_template('Ex10Base.html', usersList=users, msg=alertMsg)


def delete(req, users):

    email = req.form['up_o_email']
    query = 'delete from users where email = '+email
    if inter_db(query, 'commit'):
        alertMsg = "User was deleted!"
    else:
        alertMsg = "User not found"
    query_text = 'select * from users'
    users = inter_db(query_text, 'fetch')
    return f.render_template('ex10/Ex10Base.html', usersList=users, msg=alertMsg)


@assignment10.route('/assignment10', methods=['GET', 'POST'])
def e10():
    query_text = 'select * from users'
    users = inter_db(query_text, 'fetch')

    if f.request.method == 'POST':
        if f.request.form['is_name']:
            insert(f.request)

        if f.request.form['up_o_email']:
            update(f.request)

        if f.request.form['d-em']:
            delete(f.request)

    return f.render_template('Ex10Base.html', usersList=users)


@assignment10.route('/assignment11')
def ex11():
    return f.redirect('/assignment11/users')


@assignment10.route('/assignment11/users')
def ex11_f():
    query_text = 'select * from users'
    users = inter_db(query_text, 'fetch_json')
    return f.render_template('ex11.html', usersList=users)


@assignment10.route('/assignment11/outer_source')
def ex11_o():

    if f.request.method == 'GET':
        if 'backId' in f.request.args:
            id = f.request.args['backId']
            res = requests.get('https://reqres.in/api/users/'+ id)
            user = res.json()

            return f.render_template('ex11_o.html', selected = user['data'])

    return f.render_template('ex11_o.html')

@assignment10.route('/assignment12/restapi_users/')
def default_user():
    return f.redirect('/assignment12/restapi_users/1')
    
@assignment10.route('/assignment12/restapi_users/<int:UserId>/')
def ex12(UserId):
    res = requests.get('https://reqres.in/api/users/'+ str(UserId))
    user = res.json()
    if ('data' in user):
        return f.render_template('ex12.html', selected = user['data'])
    else:
        error = {
            'Success': False,
            'Error': {
                'Reason': 'UserId not found', 
                'Message': "Requested user with Id "+str(UserId)+" wasn't found in the DB"
            },
            'Code' : 404, 
            'Message': "Not found"
        }
        return f.render_template('ex12.html', selected = error)
