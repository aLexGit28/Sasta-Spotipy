# Inside run.py (corrected version)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    # CORRECTED: Just give the filename. Flask looks in 'templates' automatically.
    return render_template('home.html')

if __name__ == '__main__':
    # REMOVED port=5500 to use the default Flask port (5000)
    # debug=True is great for development!
    app.run(debug=True)