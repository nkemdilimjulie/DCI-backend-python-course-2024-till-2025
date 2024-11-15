from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


# TODO: create na about me page that will
# display a few sentence about you.
# Hint: Be mindful of the URL or route of your new page
@app.route("/about-us")
def about_us():
    return "<h1 style='color:red'>Hey there, my name is Eyong and I am a Python developer</h1>"


# TODO: projects
# TODO: certificates

if __name__ == "__main__":
    app.run(debug=True)
