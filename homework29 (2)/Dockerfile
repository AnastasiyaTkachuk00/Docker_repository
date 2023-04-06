FROM python:3.9
USER root
RUN mkdir /my_app
WORKDIR /my_app

# Adding trusting keys to apt for repositories
RUN apt-get -y update && apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# Updating apt to see and install Google Chrome
RUN apt-get -y update
# Magic happens
RUN apt-get install -y google-chrome-stable
# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# set display port to avoid crash

ENV DISPLAY=:99

# upgrade pip
RUN pip3 install --upgrade pip

COPY . /Downloads/Docker_repository
RUN pip install -r /Downloads/Docker_repository/requirements.txt
CMD ["pytest", "/Downloads/Docker_repository/tests_for_docker/web_tests.py"]
