#!/usr/bin/env python3
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
from flask_assets import Environment, Bundle
from staticpy import (
    app,
    build_all,
    log,
    get_config,
    get_page,
    get_subpages,
    get_frontmatter,
    BASE_CONFIG,
    PROJECT_PATH,
    TEMPLATE_PATH,
)
from collections import OrderedDict

assets = Environment(app)
scss = Bundle(
    "main.scss",
    "_variables.scss",
    "_base.scss",
    "_header.scss",
    "_note.scss",
    "_post.scss",
    "_markdown.scss",
    filters="pyscss",
    output="main.css",
)
assets.register("scss_all", scss)


@app.context_processor
def get_assets():
    return {"assets_url": assets["scss_all"].urls()[0]}


########################
# CUSTOM ROUTES
########################


@app.route("/")
def home():
    """Renders the home page."""
    config = get_config("home")
    pages = {}  # TODO: Deprecate sitemap

    # Get post for Post showcase
    posts = []
    for url in config["posts"]:
        posts.append(get_page(url))

    # Get projects for Project showcase
    projects = config["projects"]

    context = {"pages": pages, "posts": posts, "projects": projects}
    return render_template(config["template"], **context)


@app.route("/notes/")
def notes_homepage():
    """Renders the notes home page located in /notes/index.html ."""

    # Get metadata from context's config
    context = BASE_CONFIG["contexts"]["notes"]
    source_path = PROJECT_PATH / context["source_path"]
    pages = get_subpages(source_path)

    for page in pages:
        page["subpages"] = get_subpages(page["url"], recursive=False)

    # for category_url in categories.keys():
    #     notebooks = get_subpages(category_url)
    kwargs = {"pages": pages}
    return render_template(f"notes/index.html", **kwargs)


@app.route("/posts/")
def posts_homepage():
    """Renders the posts home page of URL /posts/index.html ."""

    # Get metadata from post's config
    context = BASE_CONFIG["contexts"]["posts"]
    source_path = PROJECT_PATH / context["source_path"]
    posts = get_subpages(source_path)

    modified_times = [post["last_updated"] for post in posts]
    sort_idx = sorted(range(len(modified_times)), key=modified_times.__getitem__)[::-1]
    # posts = OrderedDict((list(posts.items())[i]) for i in sort_idx)

    context = dict(posts=posts)

    return render_template("posts/index.html", **context)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        app.run(debug=True, host="0.0.0.0", port=8080)
    elif "build" in args:
        log.setLevel("INFO")
        elapsed_time = build_all()
        print(f"Building templates finished in {elapsed_time:.2f}secs")
    else:
        raise ValueError("Invalid command. Use `python app.py [build]`")
