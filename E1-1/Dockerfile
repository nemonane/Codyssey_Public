FROM nginx:alpine

LABEL org.opencontainers.image.title="dev-workstation-web"
LABEL org.opencontainers.image.description="Custom NGINX web server for workstation assignment"

ENV APP_ENV=dev

COPY site/ /usr/share/nginx/html/