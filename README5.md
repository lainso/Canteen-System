构建步骤：<br>
    > 1.修改canteenb/Canteen/config.py，对系统进行配置。<br>
    > 2.命令行运行docker-compose up -d。<br>
<br>
系统使用端口：<br>
    > 88：前端服务<br>
    > 8001：后端服务<br>
    > 3305：mysql<br>
    > 6378：redis<br>
<br>
涉及配置文件：<br>
    > 1.canteenb/Canteen/config.py<br>
    > 2.canteenf-unpack/src/config/main.js<br>
    ⭐：修改此项需要重新打包，并将新文件覆盖到canteenf目录中<br>
<br>
系统提供三个身份，分别使用不同url登录：<br>
    > 顾客：/<br>
    > 店铺：/shop<br>
    > 管理员：/super<br>
<br>
数据库中提供了测试账号：<br>
    > 顾客：<br>
        > > 账号：123<br>
        > > 密码：123456<br>
    > 店铺：<br>
        > > 账号：456<br>
        > > 密码：123456<br>
    > 管理员：<br>
        > > 账号：789<br>
        > > 密码：123456<br>
    > 超级管理员（仅用于管理管理员账号，无其它权限，请勿删除此账号）：<br>
        > > 账号：SuperAdminForSystem<br>
        > > 密码：SuperAdmin<br>
