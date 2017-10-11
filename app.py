'''
Created on Oct 11, 2017

@author: peperk
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "TEST FLASK"
    

if __name__ == '__main__':
    app.run()