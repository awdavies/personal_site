from flask import (
  Flask,
  render_template,
  url_for,
)
from jinja2.nodes import (
  Const,
  EvalContextModifier,
  Keyword,
)
from projects import project_list
from contact import contact_list
site = Flask(__name__)

@site.route("/")
def main():
  return render_template("index.html",
          projects=project_list,
          contact=contact_list)

if __name__ == "__main__":
    site.run()
