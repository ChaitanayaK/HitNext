# waitress-serve --port=5000 app:app

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instructions')
def quiz():
    return render_template('instructions.html')

@app.route('/question1')
def question1():
    send_from_directory('static/files', 'dataset.csv', as_attachment=True)
    return render_template('question1.html') 

@app.route('/download-dataset')
def download_dataset():
    return send_from_directory('static/files', 'dataset.csv', as_attachment=True)

@app.route('/hufflepuff44')
def question2():
    return render_template('question2.html') 

@app.route('/tgmoto')
def question3():
    return render_template('question3.html') 

@app.route('/dementor')
def question4():
    return render_template('question4.html') 

@app.route('/triwizard')
def question5():
    return render_template('question5.html') 

@app.route('/earth')
def question6():
    return render_template('question6.html') 

@app.route('/FBDAGCE')
def question7():
    return render_template('question7.html') 

@app.route('/sirmokshagundamvisvesvaraya')
def ending():
    return render_template('ending.html') 

if __name__ == '__main__':
    app.run(debug=True)
