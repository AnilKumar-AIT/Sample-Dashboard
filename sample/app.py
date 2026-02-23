from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    view = request.args.get('view', 'home')
    return render_template('dashboard.html', view=view)

if __name__ == '__main__':
    app.run(debug=True)
