from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/photo-detail")
def photo_detail():
    return render_template("photo-detail.html")


@app.route("/video-detail")
def video_detail():
    return render_template("video-detail.html")


@app.route("/videos")
def videos():
    return render_template("videos.html")


if __name__ == "__main__":
    app.run(debug=True)