from flask import Flask
app = Flask(__name__)

# Pass the required route to decorator
@app.route('/user/<username>') 
def show_user(username): 
# Greet the user 
    return f'Hello {username} !'
@app.route("/hello")
def hello():
	return "Hello World, first Flask app"
@app.route("/")
def index():
	return "Home page"
if __name__ == '__main__':
	app.run(host='192.168.1.54', debug=True)
