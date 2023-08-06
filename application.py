## run terminal first
## check only visible file in cmd : dir
## change folder : cd
## python package install : pip install package_name 
## if packages name in text file : pip install -r filename.txt
## run python application : python application_name.py
## host 0.0.0.0 is localhost, cannot use this host in web, for personal use only
## clear teminal codes : clear

    ## check all files (+ hidden) : ls -a
##when ever there is flask app, .git (gir repository)will be there by-default, so to remove it
## check git url present in repository : git remote -v
## putting all this code in our personal github repository to do deployment
## removing present origin/github repository link : git remote rm origin
## checking again link: git remote -v

## create new repository on github account then link it
    ###initailize : git init
    ### add all files : git add .
        #- see/check all the files : git status
    ### first commit : git commit -m "first commit"
        #-  it'll return some error, without email-id and user.name how can you commit
        #-  now have to set git email-id and user.name
    ### putting email-id : git config --global user.email "you@email.com"
    ### configuring user-name: git config --global user.name "Your Name"
        #(after setting it up, again have to first commit)
    ### first commit again : git commit -m :first commit"
        #(now all files are ready for commit)
    ### setting Up main branch to main : git branch -M main
    ### giving link of repository to commit : git remote add origin https://github.com/--.git
    ## final push to upload : git push -u origin main

import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__) 
## changed app.py to application.py, so this step is required
app = application #this app variable will be used to start our application

## web should interact with ridge.pkl and scaler.pickle

##import ridge regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb')) ##open in read-byte mode
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))
##we'll use these loaded files to do prediction


## creating home page
@app.route("/") 
def index():
    return render_template('index.html') 
    ## it'll search this file in templates folder


@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scaled) ## we'll get result as list()
        ## in return using result[0] to get predicted datapoint

        return render_template('home.html',results=result[0])

    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0") ##localhost, and can change port no to any like 8080 etc



# GITHUB process


    ## check all files (+ hidden) : ls -a
##when ever there is flask app, .git (gir repository)will be there by-default, so to remove it
## check git url present in repository : git remote -v
## putting all this code in our personal github repository to do deployment
## removing present origin/github repository link : git remote rm origin
## checking again link: git remote -v

## create new repository on github account then link it
    ###initailize : git init
    ### add all files : git add .
        #- see/check all the files : git status
    ### first commit : git commit -m "first commit"
        #-  it'll return some error, without email-id and user.name how can you commit
        #-  now have to set git email-id and user.name
    ### putting email-id : git config --global user.email "you@email.com"
    ### configuring user-name: git config --global user.name "Your Name"
        #(after setting it up, again have to first commit)
    ### first commit again : git commit -m :first commit"
        #(now all files are ready for commit)
    ### setting Up main branch to main : git branch -M main
    ### giving link of repository to commit : git remote add origin https://github.com/--.git
    ## final push to upload : git push -u origin main
