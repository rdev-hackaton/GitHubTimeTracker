FROM python:3.4

RUN apt-get update -y -qq --fix-missing
RUN apt-get install -y wget
RUN apt-get install -y git vim

ADD / /app
ADD /dev_requirements.txt /app/
WORKDIR /app
RUN pip install -r dev_requirements.txt

RUN echo "export LANGUAGE=en_US.UTF-8" >> /etc/profile
RUN echo "export LANG=en_US.UTF-8" >> /etc/profile
RUN echo "export LC_ALL=en_US.UTF-8" >> /etc/profile
RUN echo "locale-gen en_US.UTF-8" >> /etc/profile
RUN echo "dpkg-reconfigure locales" >> /etc/profile
