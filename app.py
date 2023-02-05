from flask import Flask
application = Flask(__name__)

@application.route("/healthz")
def index():
    return "ZAPRETI MNE NOSIT` STONE ISLAND"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port='8080')
