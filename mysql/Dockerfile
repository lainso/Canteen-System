# 使用MySQL官方docker镜像，指定版本为 MySQL8
FROM mysql:8

# 配置MySQL root账号的密码
ENV MYSQL_ROOT_PASSWORD=jQKOVqW0%W!n*cDq2B&2
# 在容器创建时创建一个名为 canteen 的数据库
ENV MYSQL_DATABASE=canteen

# 将目录下的init.sql和canteen.sql复制到容器内/docker-entrypoint-initdb.d目录
# 当容器启动时，会自动执行该目录下的sql文件，可通过这样的方法进行数据库的初始化
# init.sql 中定义了创建用户和授权的sql语句
# canteen.sql 则定义了数据库的结构和测试数据项
COPY ./init.sql /docker-entrypoint-initdb.d
COPY ./canteen.sql /docker-entrypoint-initdb.d

# 运行容器时，将容器内的 3306 端口进行暴露，以提供给后端进行连接
EXPOSE 3306

# 创建数据卷挂载点，用于持久化数据，保证容器停止或删除时数据不会被删除
VOLUME /var/lib/mysql2