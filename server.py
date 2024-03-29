from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route for our application for "/"
@app.route('/')
def home():
    """
    This funcion just reponds to the browser URL
    http://localhost:5000/

    :return:    the rendered template 'home.html'
    """
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
