from flask import Flask, render_template_string

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    color: #333;
                    margin: 0;
                    padding: 20px;
                }
                h1 {
                    color: #0056b3;
                }
                p {
                    font-size: 18px;
                }
                .container {
                    background-color: white;
                    border-radius: 8px;
                    padding: 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                    margin: auto;
                }
                .greeting {
                    font-size: 20px;
                    color: #28a745;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to My Flask App</h1>
                <p>This is a simple example of a Flask app with embedded HTML and CSS.</p>
                <p class="greeting">Hello, World!</p>
            </div>
        </body>
        </html>
    """)

# Define a route to show a custom message
@app.route('/greet/<name>')
def greet(name):
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Greeting Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    color: #333;
                    margin: 0;
                    padding: 20px;
                }
                h1 {
                    color: #0056b3;
                }
                p {
                    font-size: 18px;
                }
                .container {
                    background-color: white;
                    border-radius: 8px;
                    padding: 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                    margin: auto;
                }
                .greeting {
                    font-size: 20px;
                    color: #28a745;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello, {{ name }}!</h1>
                <p class="greeting">Welcome to your personalized page.</p>
                <p>We hope you're enjoying this simple Flask app!</p>
            </div>
        </body>
        </html>
    """, name=name)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

