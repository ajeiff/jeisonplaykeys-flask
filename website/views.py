from flask import Blueprint, render_template
from mapper.mapping_manager import ListMusicSoundcloud

views = Blueprint('views', __name__)

@views.route("/", methods=['GET'])
def home():
    data = ListMusicSoundcloud("https://kymuvqgv84.execute-api.eu-west-3.amazonaws.com/api/")
    return render_template("home.html", data=data.getlistmetadatasongdict())

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/news")
def news():
    return render_template("news.html")