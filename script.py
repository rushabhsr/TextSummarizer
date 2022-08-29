# coding=utf-8
from flask import *  
from flask import render_template
app = Flask(__name__)  
from gensim.summarization.summarizer import summarize  
@app.route('/login',methods = ['GET','POST'])  
def login():
    content = ["",""]
    if request.method == 'POST':
    	content[0]=request.form[u'uname']
    	content[0] = content[0].encode('ascii', 'ignore').decode('ascii')

      #passwrd=request.form['pass']  
      #if uname=="ayush" and passwrd=="google":
        content[1]=str((summarize(content[0])))

    return render_template('login.html',content=content)
   
if __name__ == '__main__':  
   app.run(debug = True)