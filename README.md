## 内部餐饮系统

本系统为前后端分离系统。

前端使用 vue3 构建，涉及 pinia, vue-router, element-plus, axios。

后端采用了django框架，引入了 mailer 组件进行发送邮件，并采用了 redis 缓存方案优化数据库性能。

### 部署环境要求

⭐：docker + docker-compose

## 安装

1. 根据 `canteenb/Canteen/config_example.py` 模板在同一级目录下创建 `config.py` 配置文件，对系统进行配置。

2. 修改 `canteenf-unpack/src/config/main.js` 文件，定义前后端的接口地址。

3. 在 `canteenf-unpack` 下运行构建命令，将前端进行打包。

```bash
npm run build
```

4. 将 `canteenf-unpack/dist` 中的所有内容移动到 `canteenf/` 目录下。

5. 使用命令构建镜像并启动服务：

```bash
docker-compose up -d
```

### 项目端口占用

项目涉及四个容器，需要占用宿主机的四个端口，考虑到常用端口占用，本项目默认绕开了这些端口，如果仍发生了冲突需要自定义端口，可以考虑修改 `docker-compose.yml` 文件，且需要同步更新 `canteenb/Canteen/config.py` 。

- 88：前端nginx容器端口
- 8001：后端django容器端口
- 3305：mysql容器端口
- 6378：redis容器端口

### 系统自带测试账号

为方便开箱即用，本系统数据库并非为空，提供了以下测试账号，若需要进行上线，请考虑删除这些账号。

```markdown
顾客端：
> URL：/
> 账号：123
> 密码：123456

商户端：
> URL：/shop
> 账号：456
> 密码：123456

管理员端：
> URL：/super
> 账号：789
> 密码：123456

账户管理员（仅用于管理管理员账号，无其它权限，请谨慎删除此账号）：
> URL：/super
> 账号：SuperAdminForSystem
> 密码：SuperAdmin
```