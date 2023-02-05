from flask import Flask, render_template


application = Flask(__name__, template_folder="templates")


@application.route("/healthz")
def index():
    return render_template('heathz.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port='8080', debug=True)
