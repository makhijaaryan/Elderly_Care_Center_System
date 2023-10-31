from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . models import Note, Requests
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if (request.method=='POST'):
        note=request.form.get('note')
        if (len(note)<1):
            flash('Note is too short!', category='error')
        else:
            new_note=Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note=json.loads(request.data)
    noteId=note['noteId']
    note=Note.query.get(noteId)
    if (note):
        if(note.user_id==current_user.id):
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


@views.route('/resident-home', methods=['GET','POST'])
@login_required
def residentHome():
    return render_template('/residentHome.html', user=current_user)

@views.route('/resident-request', methods=['GET','POST'])
@login_required
def residentRequest():
    if (request.method=='POST'):
        userRequest=request.form.get('userRequest')
        if (len(userRequest)<1):
            flash('Request is too short!', category='error')
        else:
            new_userRequest=Requests(userRequest=userRequest, user_id=current_user.id)
            db.session.add(new_userRequest)
            db.session.commit()
            flash('Request Registed!', category='success')
    return render_template("resident.html", user=current_user)


@views.route('/delete-request', methods=['POST'])
def delete_request():
    delRequest=json.loads(request.data)
    requestId=delRequest['requestId']
    delRequest=Requests.query.get(requestId)
    if (delRequest):
        if(delRequest.user_id==current_user.id):
            delRequest.status="past"
            db.session.commit()
    return jsonify({})
