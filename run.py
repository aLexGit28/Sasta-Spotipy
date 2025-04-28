# Inside run.py

from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home_page():
    return render_template('home.html')

# --- NEW ROUTE FOR ABOUT PAGE ---
@app.route('/about')
def about_page():
    return render_template('about.html')
# --- END OF NEW ROUTE ---

# The part that runs the app
if __name__ == '__main__':
    app.run(debug=True)