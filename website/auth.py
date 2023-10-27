from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    # return render_template("login.html", text="testing", testing=True)
    data=request.form
    print(data)
    return render_template("login.html")

@auth.route('/signup', methods= ['GET', 'POST'])
def signup():
    if request.method == "POST":
        id=request.form.get('id')
        email=request.form.get('email')
        name=request.form.get('name')
        pass1=request.form.get('password1')
        pass2=request.form.get('password2')
        contactNo=request.form.get('contactNo')
        if(pass1!=pass2):
            flash("Passwords must match!", category='error')
        elif (len(contactNo)!=10):
            flash("Incorrect number entered!", category='error')
        else:
            flash("Account created!", category='success')
            print(f"Id: {id}\nName:{name}\nEmail:{email}\nPassword: {pass1}\nContact Number:{contactNo}\n")
    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return "<p>logout here<p>"