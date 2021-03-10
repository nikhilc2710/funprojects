from flask import Flask, request, render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/submit', methods=['POST'])
def submit():
    code=request.form['text']
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True)