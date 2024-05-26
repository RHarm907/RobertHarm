from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/schoolprojects')
def schoolprojects():
    return render_template('schoolprojects.html')

@app.route('/personalprojects')
def personalprojects():
    return render_template('personalprojects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here, you can handle the form data (e.g., save it to a database or send an email)
        print(f"Received message from {name} ({email}): {message}")
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route('/thank_you')
def thank_you():
    return '<h1>Thank you for your message!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
