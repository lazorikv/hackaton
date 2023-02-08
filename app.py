from flask import Flask, render_template, request

application = Flask(__name__, template_folder="templates")


@application.route("/healthz")
def index():
    return render_template('heathz.html')


@application.route("/move", methods=["POST", "GET"])
def move():
    if request.method == 'POST':
        data = request.data
        print(data)
    return {
        "column": 2
    }


if __name__ == "__main__":
    application.run(host='0.0.0.0', port='8080', debug=True)
