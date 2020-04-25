import textcleaning as tc
import pickle
import logging
import gensim
import praw
from praw.models import MoreComments
from zipfile import ZipFile 
import json
from werkzeug.utils import secure_filename

model = pickle.load(open('model/model.pkl','rb'))


reddit = praw.Reddit(client_id='U2Ag2amSBBT2yA', client_secret='dBkSqsN5cTkLXLnaJwmfe0M4cbo', user_agent='flare', username='pranay-ar',password='Elisha2835!')



def prediction(url):
	submission = reddit.submission(url = url)
	data = {}
	data["title"] = str(submission.title)
	data["url"] = str(submission.url)
	data["body"] = str(submission.selftext)

	submission.comments.replace_more(limit=None)
	comment = ''
	count = 0
	for top_level_comment in submission.comments:
		comment = comment + ' ' + top_level_comment.body
		count+=1
		if(count > 10):
		 	break
		
	data["comment"] = str(comment)

	data['title'] = tc.clean_text(str(data['title']))
	data['body'] = tc.clean_text(str(data['body']))
	data['comment'] = tc.clean_text(str(data['comment']))
    
	combined_features = data["title"] + data["comment"] + data["body"] + data["url"]

	return model.predict([combined_features])


import flask
import pickle
import pandas as pd
from flask import Flask, render_template, request
#from gevent.pywsgi import WSGIServer


# Initialise the Flask app
#app = flask.Flask(__name__, template_folder='templates')
app = Flask(__name__)

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        text = flask.request.form['url']
        
        # Get the model's prediction
        flair = prediction(str(text))
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html', original_input={'url':str(text)}, result=flair,)


@app.route("/automated_testing")
def index2():                                                                                         
    return (render_template("test.html"))

@app.route("/automated_testing", methods = ['POST', 'GET'])
def automated_testing():
    #print("Hello")
    #print(request.method)
    if request.method == 'POST':
        #print("Hello 2")
        myfile = request.files['upload_file']
        print("Hello")
        myfile.save(secure_filename(myfile.filename))
        lst = []
        with open(myfile.filename, 'r') as filein:
            for url in filein:
                lst.append(url)

        dic = {}
        for i in lst:
            i = i[:-1]
            pred = prediction(i)
            key = i
            value = pred[0]
            dic.update({key : value})

    d = json.dumps(dic)
    return json.dumps(d)
if __name__ == '__main__':
    app.run(debug=True)
 #http_server = WSGIServer(('', 5000), app)
 #http_server.serve_forever()