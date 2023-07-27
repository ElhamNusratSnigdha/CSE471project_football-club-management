from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def hello_world():
    return render_template("login.html")
database={'nachi':'123','james':'aac','karthik':'asdsf'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
                return render_template('index.html',name=name1)

@app.route('/matches')
def matches():
    return render_template("matches.html")

@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/players')
def players():
    return render_template("players.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(debug=True)