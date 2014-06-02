# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/tmp/hello.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'



# create our little application :)
app = Flask(__name__)

#app.config.from_object(__name__)
app.config.from_envvar('hello_settings', silent=True)

#connect to database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#Home page
@app.route('/')
def home():
	return render_template('home.html')

#Name page
@app.route('/@<name>')
def hello_world(name=None):
    return render_template('template_page.html', name=name.title())

@app.route('/resume/')
@app.route('/resume')
def resume_page():
	return 'It&#39;s r&#233;sum&#233;, dummy.' 

@app.route('/@<name2>')
def user_page(name2=None):
	return render_template('user_page.html', name=name2.title())

@app.route('/list_users')
def list_users():
	return render_template('list_users.html')

@app.route('/about')
def portfolio():
	return render_template('portfolio.html')

@app.route('/style')
def styleguide():
	return render_template('styleguide.html')


if __name__ == '__main__':
    app.run()