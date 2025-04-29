# Inside app/routes.py

# Keep the existing imports and blueprint definition
from flask import Blueprint, render_template
main_bp = Blueprint('main', __name__) 

# Keep the existing home and about routes...
@main_bp.route('/')
def home_page():
    return render_template('home.html')

@main_bp.route('/about')
def about_page():
    return render_template('about.html')


# --- NEW ROUTE FOR LOGIN PAGE ---
@main_bp.route('/login')
def login():
    # This just displays the login form template
    return render_template('login.html')
# --- END OF LOGIN ROUTE ---


# --- NEW ROUTE FOR REGISTER PAGE ---
@main_bp.route('/register')
def register():
    # This just displays the register form template
    return render_template('register.html')
# --- END OF REGISTER ROUTE ---