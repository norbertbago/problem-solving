from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    return "Main Page"

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return "You've used a POST request!"
    else:
        return "You've used a GET request!"



app.run()

