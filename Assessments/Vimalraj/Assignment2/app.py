from flask import Flask,render_templates

app=Flask(__name__)

@app.route('/home')
def home():
    return render_templates("homepage.html")
@app.route('/about')
def about():
    return render_templates("about.html")
@app.route('/signin')
def signin():
    return render_templates("signin.html")
app.run(debug=True)