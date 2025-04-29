# Inside run.py (at the top level)

from app import create_app

# Call the factory function to create the app instance
app = create_app()

# Run the Flask development server 
# (only if this script is executed directly)
if __name__ == '__main__':
    app.run(debug=True)