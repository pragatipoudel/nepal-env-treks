FROM python:3.10


# Install Node
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION v18.16.0

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION"

ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH


# SASS
RUN npm install --global sass

# Install other packages
RUN apt-get update && apt-get install -y \
        postgresql-client python-dev


RUN pip3 install uwsgi

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/