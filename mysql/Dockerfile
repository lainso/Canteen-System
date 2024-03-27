FROM mysql:8

ENV MYSQL_ROOT_PASSWORD=jQKOVqW0%W!n*cDq2B&2
ENV MYSQL_DATABASE=canteen

COPY ./init.sql /docker-entrypoint-initdb.d
COPY ./canteen.sql /docker-entrypoint-initdb.d


EXPOSE 3306

VOLUME /var/lib/mysql