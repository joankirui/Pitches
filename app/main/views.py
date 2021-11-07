from flask import render_template,redirect,url_for
from .import main
from flask_login import login_required
from ..models import User,Pitch,Comment,Upvote,Downvote

@main.route('/')
def index():
    pitches = Pitch.query.all()
    job = Pitch.query.filter_by(category = 'Job').all()
    event = Pitch.query.filter_by(category = 'Events').all()
    advertisement = Pitch.query.filter_by(category = 'Advertisement').all()
    return render_template('index.html',event = event,job = job,advertisement = advertisement, pitches = pitches)

# @main.route('/create_new', methods = ['POST','GET'])
# @login_required
# def new_pitch():



