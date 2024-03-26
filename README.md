构建步骤：
    1.修改canteenb/Canteen/config.py，对系统进行配置。
    2.命令行运行docker-compose up -d。

系统使用端口：
    88：前端服务
    8001：后端服务
    3305：mysql
    6378：redis

涉及配置文件：
    1.canteenb/Canteen/config.py
    ----修改以下文件需要重新执行 npm run build----
    2.canteenf-unpack/vite.config.js
    3.canteenf-unpack/src/config/baseURL.js