from flask import Flask, render_template

#app is the name used in Procfile
app = Flask(__name__)

@app.route('/')
def home():
    # renders html page
    return render_template('home.html')

@app.route('/about')
def about():
    # renders html page
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
