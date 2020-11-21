from flask import Flask

app = Flask(__name__) # Flask takes the name of the current module as argument

@app.route("/")
def welcome():
	return "Hello"
	
if __name__ == "__main__":
	app.run(use_reloader = True, port = 80)