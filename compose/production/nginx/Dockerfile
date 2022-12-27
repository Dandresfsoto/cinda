FROM nginx:1.18.0-alpine

LABEL maintainer="John Tamayo <john.tamayo@greensill.com>" version="1.0.0"

ARG APP_ENV=production

COPY ./compose/${APP_ENV}/nginx/nginx.conf /etc/nginx/conf.d/default.conf
