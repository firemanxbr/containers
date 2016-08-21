from flask import Flask

app = Flask(__name__)

@app.route('/')
def default_route():
    return 'Flask running on Containers!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

