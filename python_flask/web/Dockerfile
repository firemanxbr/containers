FROM centos:latest
MAINTAINER Marcelo Barbosa "firemanxbr@fedoraproject.org"

ENV PYTHONUNBUFFERED 1

RUN mkdir /srv/worker
WORKDIR /srv/worker

RUN yum -y update; yum -y upgrade
RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all

ADD requirements.txt /srv/worker
RUN pip install -r requirements.txt

ADD . /srv/worker

ENTRYPOINT ["python"]
CMD ["app.py"]
