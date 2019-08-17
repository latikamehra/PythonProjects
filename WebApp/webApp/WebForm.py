'''
Created on Aug 2, 2019

@author: latikamehra
'''
from flask import Flask, render_template, flash, redirect, url_for, session
from webApp.Forms import LoginForm as lf
from genericpath import exists

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/home")
def home():
    return '''
    <title><h1> Hey There! </h1></title>
    <a href="/"> Login Page </a>
    '''

@app.route('/')
def default():
    return redirect(url_for('login'))

   
@app.route("/login", methods=['POST', 'GET'])
def login():
    frm = lf()
    if frm.validate_on_submit():
        
        ip = {}
        ip['usr'] = frm.usrnm.data
        ip['pwd'] = frm.pswrd.data
        ip['remember'] = frm.rmmbr_me.data
        msg = "Login requested for {} with Remember_Me flag set to {}"
        flash(msg.format(ip['usr'], ip['remember']))
        session[ip['usr']] = True
        
        return redirect(url_for('wlcm', name=ip['usr']))
    return render_template("login.html", title="Sign-In", form=frm)



@app.route('/welcome/<string:name>')
def wlcm(name):
    if name in session.keys() :
        logged_flag = session[name]
    else:
        logged_flag = False
    user = {'username': name}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    if logged_flag == True:
        return render_template('welcome.html',  user=user, posts=posts) 
    else :
        return redirect(url_for('login'))
 
    
if __name__ == "__main__":
    app.run()