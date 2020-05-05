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
    CONTEXTS,
    BASE_CONFIG,
    PROJECT_PATH,
    TEMPLATE_PATH,
)
from staticpy.context import Context
from staticpy.source_handler import Page

"""
app = Staticpy()
"""

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


# @app.route("/notes/")
# def notes_homepage():
#     """Renders the notes home page located in /notes/index.html ."""

#     # Get metadata from context's config
#     context = BASE_CONFIG["contexts"]["notes"]
#     source_path = PROJECT_PATH / context["source_path"]
#     pages = get_subpages(source_path)

#     for page in pages:
#         page["subpages"] = get_subpages(page["url"], recursive=False)

#     # for category_url in categories.keys():
#     #     notebooks = get_subpages(category_url)
#     kwargs = {"pages": pages}
#     return render_template(f"notes/index.html", **kwargs)


# @app.route("/posts/")
# def posts_homepage():
#     """Renders the posts home page of URL /posts/index.html ."""

#     # Get metadata from post's config
#     context = BASE_CONFIG["contexts"]["posts"]
#     source_path = PROJECT_PATH / context["source_path"]
#     posts = get_subpages(source_path)

#     modified_times = [post["last_updated"] for post in posts]
#     print(posts)
#     sort_idx = sorted(range(len(modified_times)), key=modified_times.__getitem__)[::-1]
#     # posts = OrderedDict((list(posts.items())[i]) for i in sort_idx)

#     context = dict(posts=posts)

#     return render_template("posts/index.html", **context)


if __name__ == "__main__":
    args = sys.argv[1:]
    times = []

    if "build" in args:
        build_time = build_all()

        if build_time is not None:
            print(f"{'Build time:':<30} {build_time:.2f} secs")
            times.append(build_time)

    if "freeze" in args:
        freeze_time = freezer.freeze()
        if freeze_time is not None:
            print(f"{'Static convert time:':<30} {freeze_time:.2f} secs")
            times.append(build_time)

        else:
            print(
                "Static conversion failed \nTry setting `FLASK_ENV=development` for debugging"
            )

    if times:
        print(f"\n{'':=^80}")
        print(f"{'Total time:':<30} {sum(times) :.2f} secs\n")
