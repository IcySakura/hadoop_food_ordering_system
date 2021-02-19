from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import os
import subprocess

app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'OAdregJF9823Rofjwoef3209489H4T'

# Flask-Bootstrap requires this line
Bootstrap(app)

class WordCountForm(FlaskForm):
    input_text = TextAreaField('Type in your text below:', validators=[DataRequired()])
    submit = SubmitField('Submit')

def run_mapred(input_string):
    input_string = input_string.lower()
    filepath_in = 'input/input.txt'
    filepath_out = 'output'

    with open(filepath_in, 'w+') as f:
        f.write(input_string)
    
    subprocess.run(['mapred', 'streaming', '-input', 'input/*', '-output', 'output', '-mapper', 'mapper.py', '-reducer', 'reducer.py'])
    with open(f'{filepath_out}/part-00000') as f:
        lines = [line.rstrip('\n') for line in f]
    
    subprocess.run(['rm', '-rf', filepath_out])
    return lines


@app.route('/', methods=['GET', 'POST'])
def index():
    form = WordCountForm()
    if form.validate_on_submit():
        input_string = form.input_text.data
        form.input_text.data = ""

        hadoop_output = run_mapred(input_string)
        for line in hadoop_output:
            flash(line)
        # redirect the browser to another route and template
        return redirect( url_for('results') )

    return render_template('index.html', form=form)

@app.route('/results')
def results():
    return render_template('results.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
