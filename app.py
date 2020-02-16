from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.route('/')
def home():
    #The Cube
    return render_template('home.html')

app.route('/portfolio')
def index():
    #Portfolio
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))