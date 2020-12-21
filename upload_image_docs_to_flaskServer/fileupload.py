import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
import minecart
UPLOAD_FOLDER = 'documets/'
PEOPLE_FOLDER = os.path.join('static', 'documetns')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
from PIL import Image
app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <h1>Upload course pdf</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>

<h1> Add Course</h1>
<style>
        
        table, th, td,tr {
          border: 1px solid black;
        }
</style>
<table>
    <tr><th>course Status</th>
         <th>course Domain</th>
         <th>course provider</th>
         <th>Course certificate</th>
        </tr>
        <tr> 
            <td>
                <select name="cars" id="cars">
                    <option value="Completed">Registerd </option>
                    <option value="Registerd">Completed</option>

                  </select>
        <td><input placeholder="EX: Courseera,Udemy"></td>
         <td><input placeholder="EX: Python,Kubernets"></td>
         <td><input type="file">
         <td><Button>save</Button></td>
     </tr>
     </table>
    '''
@app.route('/uploaded_file')
def uploaded_file():
    file =open('pathofdocumet','rb')
    doc = minecart.Document(file)
    page=doc.iter_pages()
    pageref=[]
    for j,i in enumerate( page):
        im = i.images[0].as_pil()
        im.save(app.config['docsfolder']+f"/{j}.jpg")
    for i in range(6):
        print(os.path.join(app.config['docsfolder']))
        print(app.config['docsfolder'])
        pageref.append(os.path.join(app.config['docsfolder'], f'{i}.jpg'))
    print(pageref)
    
    return render_template("x.html", user_image = pageref)

@app.route('/studentdata')
def studentdata():
    return'''
    <style>
        
        table, th, td,tr {
          border: 1px solid black;
        }
</style>
     <select name="cars" id="cars">
                                <option value="Completed">Third Year </option>
                                <option value="Completed">Second Year </option>
                                <option value="Registerd">Final Year</option>
            
                              </select>
         <select name="cars" id="cars">
                                <option value="Completed">Div c </option>
                                <option value="Registerd">Div A </option>
                                <option value="Registerd">Div B </option>
            
                              </select>
        <button>Generate Report</button>
    <h2> Students with No registration or less then 5 course completion</h2>
        <table>
    <tr><th>Student ID</th>
    <th>Student Name</th>
         <th>No ofcourse's Completed</th>
         <th>No of Course's Registerd Currently </th>
        </tr>
        <tr> 
            <td>
               <h6>-</h6>
                
                  <td><h6>-</h6></td>
                <td>-</td>
                  <td>-</td>
     </tr>
     </table>
    <h2> Student Course completion and registration detail</h2>
    <table>
    <tr><th>Student ID</th>
    <th>Student Name</th>
         <th>No ofcourse's Completed</th>
         <th>No of Course's Registerd Currently </th>
        </tr>
        <tr> 
            <td>
               Tus3s181912</td>
                
                  <td>Nikhil Chauhan</td>
                <td>6</td>
                  <td>0</td>
     </tr>
     </table>
     <br>
     <br>
     <h1> Make Announcement</h1>
     Title: <br>
     <input></input><br>
     Description:<br>
     <textarea></textarea><br>
    <input type="checkbox">Mandatory<br>

     <Button onclick="myFunction()">Make Announcement</Button>
     <script>
     function myFunction(){
     window.alert('Anouncemt created')}
     </script>
    '''
@app.route('/announcemet')
def announcemet():
    return'''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bootstrap Horizontal Card Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <style>
        .bcontent {
            margin-top: 10px;
        }
    </style>
</head>
<body>
<h1 class="card-title"> Announcemet
    <div class="container bcontent">
        <hr />
        <div class="card" style="width: 900px;">
                <div class="col-sm-7">
                    <div class="card-body">
                        <h2 class="card-title">Register for Codevita 2020</h5>
                        <h5 class="card-text">Click below link to register for codevita 2020</p>
                        <a href="https://forms.gle/9AbY11M2v8nkRuDs9" class="btn btn-primary">Click here to register</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
    '''

@app.route('/dashboard')
def dashboard():
    return render_template('dash.html')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['docsfolder'] = PEOPLE_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
if __name__ == "__main__":
    app.run(debug=True)

