FROM jekyll/jekyll:4.2.0

WORKDIR /tmp
COPY Gemfile .
RUN bundle install && rm Gemfile

WORKDIR /srv/jekyll