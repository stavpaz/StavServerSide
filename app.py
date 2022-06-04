from flask import  Flask,redirect,url_for
from flask import render_template
app = Flask(__name__)

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

    return render_template('assignment3_1.html', user_info=user_info, user_degrees=degrees, hobbies=hobbies, user_name='stav', user_second='cohen')

@app.route('/blocks')
def blocks_page():
    return redirect('/assignment3_1.html')


@app.route('/openyourmind.html')
def OpenYourMind_page():
    return render_template('openyourmind.html', user_name='stav', user_second='cohen')


if __name__ == '__main__':
    app.run(debug=True)



