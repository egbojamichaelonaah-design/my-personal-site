from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
import os
import resend

# cloud = "0R&V3%51GW$NMOF!Or"
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

# from flask import Flask, render_template, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, TextAreaField
# from wtforms.validators import DataRequired, Email, Length
# import smtplib, os
#
# app = Flask(__name__)
# app.config["SECRET_KEY"] = os.environ.get('MY_FLASK_SECRET_KEY')
#
#
# class SendMessage(FlaskForm):
#     name = StringField("Title", validators=[DataRequired(), Length(min=3, max=200)])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     message = TextAreaField("Content", validators=[DataRequired(), Length(min=10)])
#     submit = SubmitField("SEND MESSAGE")
#
#
# @app.route("/", methods=['GET', 'POST'])
# def home():
#     form = SendMessage()
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         message = form.message.data
#         try:
#             my_email = "romeoclimate@gmail.com"
#             password = os.environ.get('GMAIL_APP_PASSWORD')
#             with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection:
#                 connection.starttls()
#                 connection.login(user=my_email, password=password)
#                 connection.sendmail(from_addr=my_email,
#                                     to_addrs="michaelonaahegboja@gmail.com",
#                                     msg=f'Subject:Message From Your Website.\n\nSENDER INFO:\nName: {name}\nEmail:'
#                                         f' {email}\n\nMessage:\n"{message}"')
#             flash("Message sent successfully!", "success")
#         except Exception as e:
#             print(f"Email failed: {e}")
#             flash("Failed to send message. Please try again.", "error")
#
#     return render_template("index.html", form=form)
#
#
# if __name__ == "__main__":
#     app.run(debug=False)





# from flask import Flask, render_template, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, TextAreaField
# from wtforms.validators import DataRequired, Email, Length
# import os, threading
# import sendgrid
# from sendgrid.helpers.mail import Mail
#
# app = Flask(__name__)
# app.config["SECRET_KEY"] = os.environ.get('MY_FLASK_SECRET_KEY')
#
# class SendMessage(FlaskForm):
#     name = StringField("Title", validators=[DataRequired(), Length(min=3, max=200)])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     message = TextAreaField("Content", validators=[DataRequired(), Length(min=10)])
#     submit = SubmitField("SEND MESSAGE")
#
# def send_email(name, email, message):
#     try:
#         sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
#         email_message = Mail(
#             from_email='romeoclimate@gmail.com',
#             to_emails='michaelonaahegboja@gmail.com',
#             subject='Message From Your Website',
#             plain_text_content=f'SENDER INFO:\nName: {name}\nEmail: {email}\n\nMessage:\n"{message}"'
#         )
#         sg.send(email_message)
#         print("Email sent successfully!")
#         # return True
#     except Exception as e:
#         print(f"Email failed: {e}")
#         # flash("Failed to send message. Please try again.", "error")
#         # return False
#
# @app.route("/", methods=['GET', 'POST'])
# def home():
#     form = SendMessage()
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         message = form.message.data
#         thread = threading.Thread(target=send_email, args=(name, email, message))
#         thread.start()
#         flash("Message sent successfully!", "success")
#     return render_template("index.html", form=form)
#
# if __name__ == "__main__":
#     app.run(debug=True)
