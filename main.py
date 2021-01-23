from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "your-secret-key-should-not-be-here"


class SimpleForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return f"<p>It works!</p>" \
           f"<p><a href={ url_for('parks') }>View Parks</a></p>"


@app.route("/parks", methods=["GET", "POST"])
def parks():
    simple_form = SimpleForm()

    if simple_form.validate_on_submit():
        name = simple_form.name.data
        print(name)
        # Do something with name
        return redirect(url_for('home'))
    else:
        print("Name is required")
        # OR send some error message to front-end

    return render_template("parks.html", form=simple_form)


if __name__ == "__main__":
    app.run(debug=True)
