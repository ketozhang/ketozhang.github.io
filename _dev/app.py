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
    freezer,
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
