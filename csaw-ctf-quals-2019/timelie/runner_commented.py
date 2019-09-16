#!/usr/bin/sage
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from sagesham import SS, rederive
from secrets import REQUIRED, FLAG, APP_SECRET
from music import  *
import uuid
import os
import random
import pickle

app = Flask(__name__)
app.config["RAW_FILES"] = "./tmp/"
shares = []

# A hint about how SSS was implemented, seems like sage was used

def prepare_lawsuit():
    # total_pieces = 4000
    # required_pieces = REQUIRED
    # prime = 101109149181191199401409419449461491499601619641661691809811881911
    # secret = int(FLAG.encode('hex'),16)
    # sham = SS(secret, total_pieces, required_pieces, prime)
    # return sham.create_shares()
    return pickle.load(open('pshares','rb'))


# The first thing that'll run once you open webpage
@app.route('/')
def index():
    return render_template('index.html')            # index.html has been loaded

# POST on /musicin
@app.route('/musicin', methods=['POST'])
def invoke_artificial_intelligence_factorization():
    global shares                                   # Global shares
    if 'file' not in request.files:                                 # Don't be sly, else
        return redirect(url_for("index", _anchor="features"))       # Redirect to /#features
    file = request.files['file']                                    # Get Attributes
    if file.filename =='':                                          # No empty file name allowed
        return redirect(url_for("index", _anchor="features"))       # If so, then redirect to /#features

    # For example
    # test.txt uploaded will be saved as
    # ./tmp/cc567660-6c84-44cc-a156-86f29c5c5529test.txt
    name = os.path.join(app.config['RAW_FILES'], str(uuid.uuid4()) + secure_filename(file.filename))
    file.save(name)                                                 # Now we can save as it's not guessable
    share = random.choice(shares)

    # try block
    try:
        # Something like musicals/5d7bdb7d-e925-486f-a6bf-277fa69fa3ca , can't guess
        magic_name = os.path.join('musicals',str(uuid.uuid4()))
        #create score is called with
        # name
        # hex of 2nd element of share
        # string of integer represent of 1st element of share
        # magic name
        create_score(name, hex(int(share[1])).replace('0x','').replace('L',''), str(int(share[0])), magic_name)
        # Reutrn to /sheetmusic/musicals/5d7bdb7d-e925-486f-a6bf-277fa69fa3ca
        # Hence, magic name will be known after the create_score is called
        return redirect('/sheetmusic/{}'.format(magic_name))
    except Exception as e:
        print e
        return redirect(url_for("index", _anchor="features"))
    return redirect(url_for("index", _anchor="features"))

n

@app.route('/musicals/<path:path>')
def transmit_super_quantum_secrets(path):
    return send_from_directory('musicals', path)

@app.route('/sheetmusic/musicals/<filename>', methods=['GET'])
def entangle_quasi_primes(filename):
    return render_template("musical.html", filename="/musicals/"+filename)

if __name__ == '__main__':
    app.secret_key = APP_SECRET                         # Set APP_SECRET
    environment.UserSettings()['warnings']=0            # No warnings, No Haxx
    shares = prepare_lawsuit()                          # Prepare SS
    app.run(host='0.0.0.0')                             # Run Flask everywhere
