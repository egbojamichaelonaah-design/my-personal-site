from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
import os
import resend

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('MY_FLASK_SECRET_KEY')

class SendMessage(FlaskForm):
    name = StringField("Title", validators=[DataRequired(), Length(min=3, max=200)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Content", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("SEND MESSAGE")

def send_email(name, email, message):
    try:
        resend.api_key = os.environ.get('RESEND_API_KEY')
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "egbojamichaelonaah@gmail.com",
            "subject": "Message From Your Website.",
            "text": f'SENDER INFO\nName: {name}\nEmail: {email}\n\nMessage:\n"{message}"'
        })
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Email failed: {e}")
        return False

@app.route("/", methods=['GET', 'POST'])
def home():
    form = SendMessage()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        report = send_email(name, email, message)
        if report:
            flash("Message sent successfully!", "success")
        else:
            flash("Failed to send message. Please try again.", "error")
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=False)
