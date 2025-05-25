from flask import Flask, render_template, request
from scanner import scan_target
from utils import is_valid_target
from report import generate_report, generate_html_report
from shodan_lookup import shodan_info

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    info = {}
    target = ""

    if request.method == "POST":
        target = request.form["target"]
        if is_valid_target(target):
            results = scan_target(target)
            generate_report(target, results)
            generate_html_report(target, results)
            info = shodan_info(target)
        else:
            info["error"] = "Invalid IP or domain."

    return render_template("index.html", target=target, results=results, info=info)

if __name__ == "__main__":
    app.run(debug=True)
