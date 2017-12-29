'''
Created on Oct 11, 2017

@author: peperk
'''
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "TEST FLASK"
    


if __name__ == '__main__':
    if 'OPENSHIFT_APP_NAME' in os.environ:              #are we on OPENSHIFT?
        ip = os.environ['OPENSHIFT_PYTHON_IP']
        port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    else:
        ip = '0.0.0.0'                            #localhost
        port = 8080 
   
    app.run(host=ip, port=port)