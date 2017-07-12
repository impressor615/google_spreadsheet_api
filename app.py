"""
    Flask web application app
"""
import os
import re

from flask import Flask, redirect, render_template, request, url_for
from spreadsheet import add_to_spreadsheet
from wtforms import Form, StringField, validators


app = Flask(__name__)


class LinkForm(Form):
    link = StringField('link', [validators.DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def save():
    form = LinkForm(request.form)
    if request.method == 'POST' and form.validate():
        link = form.link.data
        if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link):
            add_to_spreadsheet(link)
        else:
            return render_template('error.html')
        return render_template('thanks.html')
    return render_template('save.html', form=form)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port
    
