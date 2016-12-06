FROM continuumio/anaconda3

MAINTAINER "Ushio Shugo" <ushio.s@gmail.com>

ADD . $HOME/d

ENTRYPOINT ["tail", "-f", "/dev/null"]
