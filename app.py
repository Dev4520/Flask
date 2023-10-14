# https://www.youtube.com/watch?v=nZRygaTH2MA&t=45s
# https://github.com/kritimyantra/flask-authentication-system/blob/main/templates/register.html


from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import bcrypt

# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100))

    def __init__(self,email,passpword,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(passpword.encode('utf-8'), bcrypt.gensalt()).dencode('utf-8')

    def check_password(self, passpword):
        return bcrypt.checkpw(passpword.encode('utf-8'),self.passpword.encoe('utf-8'))


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'hi'


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        pass
    
    return render_template('register.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # handle rquest
        pass
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
