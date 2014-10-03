#Author: Morgan Keys
#Email: morgan.keys@gmail.com
#Adapted from Flask tutorials. See: http://flask.pocoo.org/

# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
# import templating
from jinja2 import Template
from jinja2 import Environment, PackageLoader

# create our little application :)
app = Flask(__name__)

#app.config.from_object(__name__)
app.config.from_envvar('portfolio_settings', silent=True)

#connect to database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#Create templating central object
env = Environment(loader=PackageLoader('myPortfolio', 'templates'))

#Home page
@app.route('/')
@app.route('/about')
def portfolio():
	return render_template('portfolio.html')

@app.route('/style')
def styleguide():
	return render_template('styleguide.html')

@app.route('/palantir')
def palantir():
	return render_template('portfolio_for_palantir.html')

if __name__ == '__main__':
    app.run()