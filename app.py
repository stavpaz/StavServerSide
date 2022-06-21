from flask import Flask, redirect, url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
userToUdate=''

@app.route('/')
def main():
    return redirect(url_for('Home_page'))


@app.route('/home.html')
def Home_page():
    return render_template('home.html', user_name='stav', user_second='cohen')


@app.route('/aboutus.html')
def AboutUs_page():
    return render_template('aboutus.html', user_name='stav', user_second='cohen')


@app.route('/contactus.html')
def ContactUs_page():
    return render_template('contactus.html', user_name='stav', user_second='cohen')


@app.route('/design.html')
def Design_page():
    return render_template('design.html')


@app.route('/assignment3_1.html')
def Assign_page():
    user_info = {'FirstName': 'Stav', 'SecondName': 'Paz', 'LastName': 'Cohen'}
    degrees = ['Industrial Engineering', 'Mechanical engineering', 'management']
    hobbies = ('Dance', 'TV', 'Sleep')

    return render_template('assignment3_1.html', user_info=user_info, user_degrees=degrees, hobbies=hobbies,
                           user_name='stav', user_second='cohen')


@app.route('/blocks')
def blocks_page():
    return redirect('/assignment3_1.html')


@app.route('/openyourmind.html')
def OpenYourMind_page():
    return render_template('openyourmind.html', user_name='stav', user_second='cohen')


@app.route('/assignment3_2.html')
def Assign2_page():
    return render_template('assignment3_2.html')


user_dict = {
    'stavCO': {'name': 'stav', 'email': 'stav@gmail.com'},
    'talGU': {'name': 'tal', 'email': 'tal@gmail.com'},
    'einavML': {'name': 'einav', 'email': 'einav@gmail.com'},
    'noamAV': {'name': 'noam', 'email': 'noam@gmail.com'},
    'zivIN': {'name': 'ziv', 'email': 'ziv@gmail.com'}
}

def Indict_func(inputs):

    for k, v in user_dict.items():
        if(v['email']).__eq__(inputs):
            print(v['email'])
            return(v['name'])
    return('')
def IndictName_func(inputs):

    for k, v in user_dict.items():
        if(v['name']).__eq__(inputs):
            print(v['name'])
            return(v['email'])
    return('')
@app.route('/Search')
def search_func():
    if 'name' in request.args:
        name = request.args['name']
        email = request.args['email']
        if IndictName_func(name)!='' and email=='':
            email=IndictName_func(name)
            return render_template('SearchUsers.html',
                                   name=name,
                                   email=email)
        else:
            if name=='' and email=='':
                return render_template('SearchUsers.html', user_dict=user_dict)
            else:
                if 'email' in request.args:
                    email = request.args['email']
                    name = request.args['name']
                    if Indict_func(email)!='' and name=='':
                        name = Indict_func(email)
                        return render_template('SearchUsers.html',
                                               name=name,
                                               email=email)
                    else:
                           if name!='' and email!='':
                               if Indict_func(email)==name:
                                  return render_template('SearchUsers.html',
                                                      name=name,email=email)
                               else:
                                    return render_template('SearchUsers.html', message='User not found.')
                           else:
                                if IndictName_func(name)!='':
                                   email=IndictName_func(name)
                                   return render_template('SearchUsers.html',
                                                       name=name, email=email)
                                else:
                                    if IndictName_func(name) == '':
                                        return render_template('SearchUsers.html', message='User not found.')
                                    else:
                                      return render_template('SearchUsers.html', user_dict=user_dict)
                return render_template('SearchUsers.html', user_dict=user_dict)
            return render_template('SearchUsers.html', user_dict=user_dict)
    return render_template('SearchUsers.html', user_dict=user_dict)


sign_dict={
    'stavCO':'123123',
    'talGU':'111111',
    'einavML':'000000',
    'noamAV':'123456',
    'zivIN':'999999'
}
@app.route('/log_in', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in sign_dict:
            pas_in_dict = sign_dict[username]
            if pas_in_dict == password:
                session['username'] = username
                session['logedin'] = True
                return render_template('log_in.html',
                                       message='Success',
                                       username=username)
            else:
                return render_template('log_in.html',
                                       message='Wrong password!')
        else:
            return render_template('log_in.html',
                                   message='Username doesnt exist')
    return render_template('log_in.html')

def Register_func(inputs):
    for k, v in user_dict.items():
        if(k).__eq__(inputs):
            return(False)
    return(True)

@app.route('/registration', methods=['GET', 'POST'])
def register_func():
    if request.method == 'POST':
        name=request.form.get('inputname')
        username = request.form.get('inputUsername')
        email=request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        Repassword = request.form.get('inputConfirmPassword')
        if Repassword == password and Register_func(username):
            session['username'] = username
            session['logedin'] = True
            user_dict[username]={'name':name,'email':email}
            sign_dict[username]= password
            print(user_dict)
            print(sign_dict)
            return render_template('assignment3_2.html',
                                   message='Success',
                                   username=username)
        else:
            return render_template('registration.html',
                                   message='Passwords dont match or user name already exists,please register again')
    return render_template('registration.html')

@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('Assign2_page'))


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))
@app.route('/assignment4.html')
def Assign4_page():
    return render_template('assignment4.html')
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

@app.route('/users')
def users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('users.html', users=users_list)

@app.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['inputname']
    username = request.form['inputUsername']
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    #print(f'{name} {email} {password}')
    query = "INSERT INTO users(username,name, email, password) VALUES ('%s','%s', '%s', '%s')" % (username,name, email, password)
    interact_db(query=query, query_type='commit')
    return redirect('/users')

@app.route('/updateuser', methods=['POST'])
def up_user():
    username = request.form['inputusername']
    name = request.form['inputname']
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    query = "UPDATE users SET name ='%s',email ='%s',password='%s'WHERE username='%s';" % (name, email, password,username)
    interact_db(query=query, query_type='commit')
    return redirect('/users')

@app.route('/update_user', methods=['GET','POST'])
def update_user():
    user_id = request.form['user_id']
    userToUdate=user_id
    return render_template('updateusers.html',username=user_id)

@app.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE username='%s';" % user_id
    # print(query)
    interact_db(query, query_type='commit')
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)
