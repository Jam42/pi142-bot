FROM python:latest

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install nodejs && \
    npm i -g pm2 