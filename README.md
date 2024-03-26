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
    2.canteenf-unpack/src/config/main.js
    ⭐：修改此项需要重新打包，并将新文件覆盖到canteenf目录中

系统提供三个身份，分别使用不同url登录：
    顾客：/
    店铺：/shop
    管理员：/super

数据库中提供了测试账号：
    顾客：
        账号：123
        密码：123456
    店铺：
        账号：456
        密码：123456
    管理员：
        账号：789
        密码：123456
    超级管理员（仅用于管理管理员账号，无其它权限，请勿删除此账号）：
        账号：SuperAdminForSystem
        密码：SuperAdmin