from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.app_context().push()

class News(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False)
  article = db.Column(db.String(1000), nullable=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<News %r>' % self.id

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

@app.route('/admin/news',methods=['POST','GET'])
def newsAdd():
    if request.method == "POST":
      news_title = request.form['title']
      news_article = request.form['article']
      new_news = News(title=news_title, article=news_article)

      try:
        db.session.add(new_news)
        db.session.commit()
        return redirect('/admin/news')
      except: 
        return 'An error occurred'
    else: 
      all_news = News.query.order_by(News.created_at).all()
      return render_template("news-add.html", all_news = all_news)

@app.route('/admin/news/delete/<int:id>')
def newsDelete(id):
  news_to_delete = News.query.get_or_404(id)
  try:
    db.session.delete(news_to_delete)
    db.session.commit()
    return redirect('/admin/news')
  except: 
    return 'An error occurred'

@app.route('/admin/news/update/<int:id>',methods=['POST','GET'])
def newsUpdate(id):
  news_to_update = News.query.get_or_404(id)
  if request.method == "POST":
      news_to_update.title = request.form['title']
      news_to_update.article = request.form['article']
      try:
        db.session.commit()
        return redirect('/admin/news')
      except: 
        return 'An error occurred'
  else: 
    return render_template("news-update.html", news = news_to_update)

@app.route('/news')
def allNews():
    all_news = News.query.order_by(News.created_at).all()
    return render_template("news.html", all_news = all_news)

@app.route('/news/<int:id>')
def newsOne(id):
    news = News.query.get_or_404(id)
    return render_template("news-one.html", news = news)

@app.route('/players')
def players():
    return render_template("players.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()