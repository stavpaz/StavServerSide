from flask import Flask, redirect, url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

app = Flask(__name__)
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)


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
    'stav': {'name': 'stav', 'email': 'stav@gmail.com'},
    'tal': {'name': 'tal', 'email': 'tal@gmail.com'},
    'einav': {'name': 'einav', 'email': 'einav@gmail.com'},
    'noam': {'name': 'noam', 'email': 'noam@gmail.com'},
    'ziv': {'name': 'ziv', 'email': 'ziv@gmail.com'}
}


@app.route('/Search')
def search_func():
    if 'name' in request.args:
        name = request.args['name']
        email = request.args['email']
        if name in user_dict:
            return render_template('SearchUsers.html',
                                   name=name,
                                   email=user_dict[name]['email'])
        else:
            if name=='' and email=='':
                return render_template('SearchUsers.html', user_dict=user_dict)
            else:
                if 'email' in request.args:
                    name = request.args['name']
                    email = request.args['email']
                    if email in user_dict['name'][email]:
                        return render_template('SearchUsers.html',
                                               name=user_dict['name']['email'],
                                               email=email)
                    else:

                            return render_template('SearchUsers.html', message='User not found.')
                return render_template('SearchUsers.html', user_dict=user_dict)
            return render_template('SearchUsers.html', user_dict=user_dict)
    return render_template('SearchUsers.html', user_dict=user_dict)


sign_dict={
    'stav':'123123',
    'tal':'111111',
    'eden':'0000'
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
                                   message='Please sign in!')
    return render_template('log_in.html')

@app.route('/registration', methods=['GET', 'POST'])
def register_func():
    if request.method == 'POST':
        username = request.form.get('inputUsername')
        password = request.form.get('inputPassword')
        Repassword = request.form.get('inputConfirmPassword')
        if Repassword == password:
            session['username'] = username
            session['logedin'] = True
            return render_template('assignment3_2.html',
                                   message='Success',
                                   username=username)
        else:
            return render_template('registration.html',
                                   message='Passwords dont match,please register again')
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


if __name__ == '__main__':
    app.run(debug=True)
