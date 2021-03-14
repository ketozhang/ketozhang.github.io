#!/usr/bin/env python3
import argparse
import sys

from flask import (
    Flask,
    abort,
    redirect,
    render_template,
    send_file,
    send_from_directory,
    url_for,
)
from flask_assets import Bundle, Environment
from staticpy import (
    BASE_CONFIG,
    CONTEXTS,
    PROJECT_PATH,
    TEMPLATE_PATH,
    app,
    build_all,
    freezer,
    log,
)
from staticpy.context import Context
from staticpy.source_handler import Page

"""
app = Staticpy()
"""

# assets = Environment(app)
# app.config["ASSETS_DEBUG"] = True
# assets.url = app.static_url_path
# scss = Bundle(
#     "_variables.scss",
#     "_base.scss",
#     "_header.scss",
#     "_note.scss",
#     "_post.scss",
#     "_markdown.scss",
#     "main.scss",
#     filters="pyscss",
#     output="main.css",
# )


# @app.context_processor
# def get_assets():
#     return {"assets_url": assets["scss_all"].urls()[0]}
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
