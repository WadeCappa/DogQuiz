from flask import render_template, request, redirect, url_for, session
from mysite import app
app.secret_key = "!I*VJzYRV2&RQtJ?j#O6IJL0#A4sxdq^&@Xfc9&!2zXe!"

@app.route('/')
@app.route('/home')
def home():
    return "Test Sentence, and let me tell you, if this does not work I will be angry"