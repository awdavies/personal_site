from flask import (
Flask,
render_template,
url_for,
)
site = Flask(__name__)
url_for('static', filename='narrow.css')
url_for('static', filename='padding.css')

@site.route("/")
def main():
	return render_template("index.html")

if __name__ == "__main__":
    site.run()
