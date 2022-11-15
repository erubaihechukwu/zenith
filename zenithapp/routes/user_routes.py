from collections import ChainMap
from heapq import merge
from multiprocessing import Value
import os
import random
from ssl import AlertDescription
from zenithapp import app
from flask import render_template,make_response,request,abort,redirect,flash,session,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from zenithapp import db,app,csrf
from zenithapp.models import *
from zenithapp.forms import *
@app.route('/')
def launch():
    return render_template('user/home.html')
@app.route('/home')
def homelaunch():
    return render_template('user/home.html')