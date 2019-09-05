FROM ubuntu:18.04

# -- Install Pipenv:
RUN apt update && apt install python3-pip git -y && pip3 install pipenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- install environment
RUN set -ex && mkdir /env
WORKDIR /env

COPY antspy-0.1.4-cp36-cp36m-linux_x86_64.whl antspy-0.1.4-cp36-cp36m-linux_x86_64.whl

RUN pwd

# -- Adding Pipfiles
COPY Pipfile Pipfile

ENV PIPENV_INSTALL_TIMEOUT 90000

# Install antspy
RUN pipenv install --skip-lock ./antspy-0.1.4-cp36-cp36m-linux_x86_64.whl

# -- Install dependencies:
RUN set -ex && pipenv install --skip-lock

EXPOSE 8888

CMD pipenv run jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --notebook-dir=/app
