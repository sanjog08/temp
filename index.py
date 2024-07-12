from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def client_app():
    # return "Hiiiii"
    return render_template('app.html')


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()