from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST': 
    f = request.files['file'] 
    print(f)
    f.save(secure_filename(f.filename))
    return 'file uploaded successfully'
        
if __name__ == '__main__':
   app.run()