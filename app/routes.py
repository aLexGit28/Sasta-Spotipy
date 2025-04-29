# Inside app/routes.py

# Keep the existing imports and blueprint definition
# Near the top of app/routes.py
from flask import Blueprint, render_template, flash, redirect, url_for 
from .forms import LoginForm # Import our new form class
main_bp = Blueprint('main', __name__) 


# Keep the existing home and about routes...
@main_bp.route('/')
def home_page():
    return render_template('home.html')

@main_bp.route('/about')
def about_page():
    return render_template('about.html')


# --- NEW ROUTE FOR LOGIN PAGE ---
# Inside app/routes.py - REPLACE the old login() function with this

@main_bp.route('/login', methods=['GET', 'POST']) # Allow both GET and POST requests
def login():
    form = LoginForm() # Create an instance of our Login Form
    
    # validate_on_submit() checks if it's a POST request and if data is valid
    if form.validate_on_submit(): 
        # --- TEMPORARY --- 
        # We'll add actual login logic (checking username/password) later!
        # For now, just pretend it worked:
        flash(f'Login requested for user {form.username.data}', 'success') 
        return redirect(url_for('main.home_page')) # Redirect to homepage
        # --- END TEMPORARY ---
        
    # If it's a GET request or validation failed, show the login page
    # Pass the form instance to the template
    return render_template('login.html', title='Login', form=form)


# --- NEW ROUTE FOR REGISTER PAGE ---
@main_bp.route('/register')
def register():
    # This just displays the register form template
    return render_template('register.html')
# --- END OF REGISTER ROUTE ---