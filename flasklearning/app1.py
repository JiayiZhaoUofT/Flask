from flask import Flask, app, url_for, request

app = Flask(__name__)

# use the route decorator to bind a function to aURL
@app.route('/')
def welcome_page():
    return 'welcome!'

@app.route('/helloworld')
def hello_world():
    return 'Hello World!'

#variable rules
# add the variable section to a URL by making sections with<user_name>
# the function receives the <user_name>as a keyword
# available types: string(default) int float path uuid
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' %username
# use a converter to specify the type of the argument like <converter:variable_name>
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' %subpath

# URL building
# the url_for accepts the names of the function as the first argument
# and any number of keyword arguments, each corresponding to a variable part of the URL rule

# HTTP abstractmethod

def do_the_login():
    return 0
def show_the_login_form():
    return 0

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html',error = error)




