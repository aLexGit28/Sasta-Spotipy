# Inside app/__init__.py

from flask import Flask

def create_app():
    # Create the Flask app instance
    # __name__ here refers to the 'app' package, 
    # so Flask knows to look for templates and static folders inside 'app/'
    app = Flask(__name__) 
    
    # Add configuration (e.g., secret key)
    # IMPORTANT: Change this to something random and keep it secret later!
    app.config['SECRET_KEY'] = 'a_different_secret_key_for_factory' 

    # Import the blueprint from our routes file (using relative import)
    from .routes import main_bp
    # Register the blueprint with the app
    app.register_blueprint(main_bp)

    # You could add database connections or other extensions here later

    # Return the configured app instance
    return app