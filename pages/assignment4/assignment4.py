#import os
#from dotenv import load_dotenv
#load_dotenv()
#'f'os.environ.get('DB_PASSWORD')'

from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector
assignment4 = Blueprint('assignment4', __name__,
                         static_folder='static',
                         template_folder='templates')

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


@assignment4.route('/assignment4')
def Assign4_page():
    return render_template('assignment_4.html')
@assignment4.route('/users')
def users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('users.html', users=users_list)

@assignment4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['inputname']
    username = request.form['inputUsername']
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    #print(f'{name} {email} {password}')
    query = "INSERT INTO users(username,name, email, password) VALUES ('%s','%s', '%s', '%s')" % (username,name, email, password)
    interact_db(query=query, query_type='commit')
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('users.html',message='user added successfully',users=users_list)

@assignment4.route('/updateuser', methods=['POST'])
def up_user():
    username = request.form['inputusername']
    name = request.form['inputname']
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    query = "UPDATE users SET name ='%s',email ='%s',password='%s'WHERE username='%s';" % (name, email, password,username)
    interact_db(query=query, query_type='commit')
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('users.html',message='user details update successfully',users=users_list)

@assignment4.route('/update_user', methods=['GET','POST'])
def update_user():
    user_id = request.form['user_id']
    userToUdate=user_id
    return render_template('updateusers.html',username=user_id)

@assignment4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE username='%s';" % user_id
    # print(query)
    interact_db(query, query_type='commit')
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('users.html',message='user deleted successfully',users=users_list)