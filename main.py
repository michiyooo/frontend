from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management and flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']
        
        # Example authentication logic (replace with actual database authentication)
        if username == "admin" and password == "password":  # Replace with real user validation
            return redirect(url_for('order_form'))  # Redirect to order form on successful login
        else:
            # Display an error message if login fails
            flash("Invalid username or password. Please try again.")
            return redirect(url_for('login'))

    # For GET requests, just render the login page
    return render_template('login.html')

@app.route('/order_form')
def order_form():
    return render_template('order_form.html')

@app.route('/order_history')
def order_history():
    return render_template('order_history.html')

@app.route('/order_management')
def order_management():
    return render_template('order_management.html')

@app.route('/order_tracking')
def order_tracking():
    return render_template('order_tracking.html')

if __name__ == '__main__':
    app.run(debug=True)
