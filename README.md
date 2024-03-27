## 内部餐饮系统

本系统为前后端分离系统。前端使用vue3构建，后端则采用了django框架。

### 部署环境要求

⭐：docker + docker-compose

### 安装

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

### 涉及技术栈

前端：vue3, pinia, vue-router, element-plus, axios

后端：django, mysql, redis


### 项目端口占用

项目涉及四个容器，需要占用宿主机的四个端口，考虑到常用端口占用，本项目默认绕开了这些端口，如果仍发生了冲突需要自定义端口，可以考虑修改 `docker-compose.yml` 文件，且需要同步更新 `canteenb/Canteen/config.py` 。

- 88：前端nginx容器端口
- 8001：后端django容器端口
- 3305：mysql容器端口
- 6378：redis容器端口

### 系统自带测试账号

为方便开箱即用，本系统数据库并非为空，提供了以下测试账号，若需要进行上线，请考虑删除这些账号。

```markdown
顾客端：/
> 账号：123<br>
> 密码：123456<br>

商户端：/shop
> 账号：456<br>
> 密码：123456<br>

管理员端：/super
> 账号：789<br>
> 密码：123456<br>

账户管理员（仅用于管理管理员账号，无其它权限，请谨慎删除此账号）：/super
> 账号：SuperAdminForSystem<br>
> 密码：SuperAdmin<br>
```

### 使用示例

演示如何使用你的项目，给出一些代码示例。

```python
# Python示例
import your_project

your_project.do_something()
```

```javascript
// JavaScript示例
const yourProject = require('your-project');

yourProject.doSomething();
```

### 许可证

说明项目的许可证。