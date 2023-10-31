from flask import Blueprint, render_template, request, flash, redirect, url_for
from . models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    if(request.method=='POST'):
        email = request.form.get('email')
        password=request.form.get('password1')
        print(f'{email}, {password}')
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                if(user.role=="resident"):
                    return redirect(url_for('views.residentHome'))
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exists.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/signup', methods= ['GET', 'POST'])
def signup():
    if request.method == "POST":
        # id=request.form.get('id')
        email=request.form.get('email')
        name=request.form.get('name')
        pass1=request.form.get('password1')
        pass2=request.form.get('password2')
        contactNo=request.form.get('contactNo')
        role=request.form.get('role')

        user=User.query.filter_by(email=email).first()
        
        if(user):
            flash('User already exists!', category='error')
        elif(pass1!=pass2):
            flash("Passwords must match!", category='error')
        elif (len(contactNo)!=10):
            flash("Incorrect number entered!", category='error')
        else:
            new_user=User(email=email, name=name, password=generate_password_hash(pass1,method='sha256'), contactNo=contactNo, role=role)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category='success')
            print(f"Name:{name}\nEmail:{email}\nPassword: {pass1}\nContact Number:{contactNo}\nRole:{role}\n")
            return redirect(url_for('views.home'))
         
    return render_template("signup.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))