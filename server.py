from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
import smtplib, os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('MY_FLASK_SECRET_KEY')

class SendMessage(FlaskForm):
    name = StringField("Title", validators=[DataRequired(), Length(min=3, max=200)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Content", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("SEND MESSAGE")


@app.route("/", methods=['GET', 'POST'])
def home():
    form = SendMessage()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        c = 5
        while c > 0:
            try:
                my_email = "romeoclimate@gmail.com"
                password = os.environ.get('GMAIL_APP_PASSWORD')
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs="michaelonaahegboja@gmail.com",
                                        msg=f'Subject:Message From Your Website.\n\nSENDER INFO:\nName: {name}\nEmail:'
                                            f' {email}\n\nMessage:\n"{message}"')
                    flash("Message sent successfully!", "success")
                break
            except:
                print("Repeated trial in sending Mail.")
            c -= 1

    return render_template("index.html", form=form)


if __name__== "__main__":
    app.run(debug=False)

