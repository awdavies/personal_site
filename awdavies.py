from flask import Flask
site = Flask(__name__)

@site.route("/")
def main():
	return "This is the website of Andrew Davies!"

if __name__ == "__main__":
	site.run()
