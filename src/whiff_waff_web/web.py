from flask import Flask
from flask import request, render_template, redirect, url_for

app = Flask(__name__.split('.')[0])
app.config['SECRET_KEY'] = 'XXX secret!'

@app.route('/')
def index():
  return redirect(url_for('ww_control'))

@app.route('/ww_control')
def ww_control():
  return render_template("ww_control.html")

@app.route('/learn')
def learn():
  return render_template("learn.html")

@app.route('/credits')
def credits():
  return render_template("credits.html")

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')
