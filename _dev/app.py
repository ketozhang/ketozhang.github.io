#!/usr/bin/env python3
import sys
from flask import (Flask, abort, redirect, render_template,
                   send_file, send_from_directory, url_for)
from staticpy import (app, build_all, run, log, get_subpages,
                      BASE_CONFIG, PROJECT_PATH, TEMPLATE_PATH)
from collections import OrderedDict


########################
# CUSTOM ROUTES
########################

def home():
    """Renders the home page."""
    config = get_config('home')
    pages = {}  # TODO: Deprecate sitemap

    posts = config['posts']
    posts_dict = {}
    for post in posts:
        fm = get_frontmatter(post)
        posts_dict[post] = fm

    projects = config['projects']

    context = dict(
        pages=pages,
        posts=posts_dict,
        projects=projects
    )

    return render_template(config['template'], **context)
app.home = home

@app.route('/notes/')
def notes_homepage():
    """Renders the notes home page located in /notes/index.html ."""

    # Get metadata from context's config
    context = BASE_CONFIG['contexts']['notes']
    source_path = PROJECT_PATH / context['source_path']
    pages = get_subpages(source_path)

    for url, page in pages.items():
        page['subpages'] = get_subpages(url)

    # for category_url in categories.keys():
    #     notebooks = get_subpages(category_url)
    print(pages)
    kwargs = dict(
        pages=pages,
    )
    return render_template(f"notes/index.html", **kwargs)


@app.route('/posts/')
def posts_homepage():
    """Renders the posts home page of URL /posts/index.html ."""
    def get_all_posts():
        """Get post urls (path relative to `TEMPLATE_PATH`).

        Returns
        -------list[str]
            A list of post urls as strings.
        """
        posts_path = TEMPLATE_PATH / 'posts'
        posts = posts_path.glob('**/[!index]*.html')
        posts = [str(post.relative_to(TEMPLATE_PATH).as_posix())
                 for post in posts]

        return posts

    posts = OrderedDict(get_subpages(PROJECT_PATH / 'posts'))

    modified_times = []
    for post in posts.values():
        modified_times.append(post['last_updated'])
    sort_idx = sorted(range(len(modified_times)),
                      key=modified_times.__getitem__)[::-1]
    posts = OrderedDict((list(posts.items())[i]) for i in sort_idx)

    context = dict(
        posts=posts
    )

    return render_template('posts/index.html', **context)


@app.route('/flashcards')
def flashcard_homepage():
    return render_template('flashcards.html')



if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        app.run(debug=True, host='0.0.0.0', port=8080, local=True)
    elif 'build' in args:
        log.setLevel('INFO')
        elapsed_time = build_all()
        print(f"Building templates finished in {elapsed_time:.2f}secs")
    else:
        raise ValueError("Invalid command. Use `python app.py [build]`")
