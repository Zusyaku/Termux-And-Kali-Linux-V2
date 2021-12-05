from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Change these
app.secret_key = 'really secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SMTP_EMAIL'] = 'EMAIL'
app.config['SMTP_PASSWORD'] = 'Password'
app.config['SMTP_HOST'] = 'smtp.gmail.com'
app.config['SMTP_PORT'] = 587
app.config['ADMIN_EMAIL'] = 'ADMIN-EMAIL'
