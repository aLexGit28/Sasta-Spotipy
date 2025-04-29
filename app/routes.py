# Inside app/routes.py

from flask import Blueprint, render_template

# Create a Blueprint object named 'main'
# __name__ helps Flask locate the blueprint
main_bp = Blueprint('main', __name__) 

# Define the route for the homepage ('/') using the blueprint
@main_bp.route('/')
def home_page():
    # We still render templates the same way
    return render_template('home.html')

# Define the route for the about page ('/about') using the blueprint
@main_bp.route('/about')
def about_page():
    return render_template('about.html')

# Add more routes related to main pages here later!