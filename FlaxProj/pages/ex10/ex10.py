import flask as f
from db_inter import inter_db

assignment10 = f.Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    template_folder='tamplates'
)


def insert(req):
    username = req.form['is_name']
    email = req.form['is_email']
    password = req.form['is_pass']

    query = "insert into users (username, email, password) values('%s', '%s', '%s')" % (
        username, email, password)
    inter_db(query, 'commit')
    alertMsg = "A new user was inserted!"
    query_text = 'select * from users'
    users = inter_db(query_text, 'fetch')
    return f.render_template('Ex10Base.html', usersList=users, msg=alertMsg)


def update(req):
    old_email = req.form['up_o_email']
    new_us = req.form['up_name']
    new_em = req.form['up_email']
    new_pss = req.form['up_pass']
    query ="UPDATE users SET username = '%s', email = '%s', password = '%s' WHERE email = '%s'" % (new_us, new_em, new_pss, old_email)
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
