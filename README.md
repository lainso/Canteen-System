## 内部餐饮系统

本系统为前后端分离系统。前端使用vue3构建，后端则采用了django框架。

### 涉及技术栈

前端：vue3, pinia, vue-router, element-plus, axios

后端：django, mysql, redis

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

4. 使用命令构建镜像并启动服务：

```bash
docker-compose up -d
```

### 自定义安装


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

### 特性

列出项目的几个主要特性。

- 特性1
- 特性2
- 特性3

### 支持与贡献

介绍用户在使用过程中遇到问题如何获取支持，以及如何为项目做出贡献。

```markdown
有疑问或需要帮助，请提交[issue](链接到你的issue页面)。

如果您想做出贡献，请首先阅读`CONTRIBUTING.md`（如果你有这样的文档），然后发送一个拉请求。
```

### 许可证

说明项目的许可证。