FROM docker.io/library/debian

LABEL name="terminal-fun"

# Update
RUN apt-get update
RUN apt-get upgrade
ARG DEBIAN_FRONTEND=noninteractive
ENV PATH /usr/local/games:/usr/games:$PATH


RUN apt-get --yes install python3 tmux dialog apt-utils git build-essential nano

# code
RUN apt-get --yes install  python3-pygments

# cmatrix
RUN apt-get --yes install cmatrix

# asciiquarium requirements
RUN apt-get --yes install perl-modules libcurses-perl

RUN apt-get --yes install jp2a

# lolcat requirement
RUN apt-get --yes install ruby

#
RUN apt-get --yes install cowsay fortunes fortune-mod

# Clean up cache
RUN apt-get clean

WORKDIR /usr/local/src/

# lolcat
# https://github.com/busyloop/lolcat
RUN gem install lolcat

# cowfortune
# https://github.com/anthraxx/cowfortune
RUN git clone https://github.com/anthraxx/cowfortune cowfortune
ENV TERM linux
RUN cd cowfortune && \
    make && \
    make install

# asciiquarium
# https://github.com/nothub/asciiquarium
RUN cpan -i Term::Animation
RUN git clone https://github.com/nothub/asciiquarium asciiquarium
RUN ln /usr/local/src/asciiquarium/asciiquarium /usr/local/bin/asciiquarium

# pipes
# https://github.com/pipeseroni/pipes.sh
RUN git clone https://github.com/pipeseroni/pipes.sh && \
    cd pipes.sh && \
    make install

# cbonsai
RUN apt-get --yes install cbonsai

# lavat
# https://github.com/AngelJumbo/lavat
RUN git clone https://github.com/AngelJumbo/lavat && \
    cd lavat && \
    make install

ADD app /app
WORKDIR /app

CMD "/app/entrypoint.py"
