from flask import Flask, jsonify, render_template
import os
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Gather system information
    name = "R Mokshgna Krishna Koushik"  # Replace with your actual name
    username = os.environ.get('USER') or os.environ.get('USERNAME')  # Get the current user's login name
    server_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime("%Y-%m-%d %H:%M:%S")
    
    # Getting the top output using a shell command
    top_output = os.popen('top -b -n1').read()
    
    # Render the data in HTML
    return f"""
    <html>
    <body>
        <h1>Name: {name}</h1>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {server_time}</h2>
        <h2>TOP output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)