FROM nginx:latest

COPY . /usr/share/nginx/html

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 800

CMD ["nginx", "-g", "daemon off;"]