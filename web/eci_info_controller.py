from flask import Flask, request, current_app
from web.service.eci_info_service import search

app = Flask(__name__)


@app.route("/")
def index():
    return current_app.send_static_file("index.html")


@app.route("/eci_info")
def answer_question():
    query = request.args.to_dict()["q"]
    return search(query)


if __name__ == '__main__':
    app.run(debug=True)
