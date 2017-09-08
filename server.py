# import Flask

from flask import Flask, render_template, redirect,request, session
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      session['upload']=True
      print "Success"
      
   else:
      session['upload']=False
      print "fail"
   return redirect('/result')

@app.route('/result')
def result():
    if session['upload']:
        print 'result success'
        return render_template('show.html')
    else:
        print 'result fail'
        return render_template('fail.html')
        
if __name__ == '__main__':
   app.run(debug = True)

