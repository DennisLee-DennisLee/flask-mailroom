import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)
    
@app.route('/create/', methods=['GET', 'POST'])
# @app.route('/create/')
def donate():
    if request.method == 'GET':
        return render_template('create.jinja2')

    if request.method == 'POST':
        amount, donor = int(request.form['amount']), request.form['donor']
        Donation.create(
            value=request.form['amount'],
            donor=Donor.get(name=request.form['donor'])
        )
        return redirect(url_for('home'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

