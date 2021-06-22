#!/usr/bin/env python3
import argparse

import yaml
from flask import Flask, render_template
from flask_article import FlaskArticleDirectory
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
notes_directory = FlaskArticleDirectory(app, article_folder="notes/")
posts_directory = FlaskArticleDirectory(app, article_folder="posts/")

app.jinja_env.add_extension("jinja2.ext.do")


########################
# CUSTOM ROUTES
########################
@app.route("/")
def home():
    """Renders the home page."""
    config = BASE_CONFIG["home"]

    # Get post for Post showcase
    post_context = CONTEXTS["posts"]
    posts = []
    for url in config["posts"]:
        page = post_context.get_page(url)
        posts.append(page)

    # Get projects for Project showcase
    projects = config["projects"]

    context = {"posts": posts, "projects": projects}
    return render_template(config["template"], **context)


@app.route("/notes/")
def notes_home():
    context = {"notes_directory": notes_directory}
    return render_template("notes_home.html", **context, **config)


@app.route("/notes/<path:subpath>")
def notes(subpath):
    article = notes_directory.get_article(subpath)
    context = {"note": article}
    return render_template("note.html", **context, **config)


@app.route("/posts/")
def posts_home():
    context = {"posts_directory": posts_directory}
    return render_template("posts_home.html", **context, **config)


@app.route("/posts/<path:subpath>")
def posts(subpath):
    article = posts_directory.get_article(subpath)
    context = {"post": article}
    return render_template("post.html", **context, **config)


@app.route("/sitemap.xml")
def sitemap():
    from flask import make_response

    template = render_template("sitemap.xml", contexts=CONTEXTS.values())
    response = make_response(template)
    response.headers["Content-Type"] = "application/xml"
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["build", "freeze"], type=str)
    args = parser.parse_args()

    if args.command == "build":
        build_time = build_all()

        if build_time is not None:
            print(f"{'Build time:':<30} {build_time:.2f} secs")

    elif args.command == "freeze":
        freeze_time = freezer.freeze()

        if freeze_time is not None:
            print(f"{'Freeze time:':<30} {freeze_time:.2f} secs")
