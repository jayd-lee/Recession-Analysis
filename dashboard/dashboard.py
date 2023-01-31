from flask import Flask, render_template
import api

app = Flask(__name__)

@app.route('/')
def index():

    data = api.convert_watchlist()
    return render_template('index.html', data = data)


if __name__ == "__main__":
    app.run(debug=True)