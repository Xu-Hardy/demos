# 🥟 Flask 工具集合小站
# 项目名称

![Build Status](https://github.com/Xu-Hardy/demos/actions/workflows/ci.yml/badge.svg)

项目描述...

这是一个使用 Flask 构建的多功能工具 Web 应用，包含以下模块：

- **面点配比计算器**（/mian）  
- **斗地主记分器**（/ddz）  
- **AirPrint 容器控制器**（/print + /restart）  
- **自动生成路由导航页（TODO）**

---

## 📦 项目结构

```bash
.
├── app.py                # 主 Flask 应用
├── templates/
│   ├── index.html        # 首页（待做自动导航）
│   ├── mian.html         # 面点比例计算页面
│   ├── score.html        # 斗地主记分器页面
│   └── airprint.html     # 打印机控制页面
├── static/               # 静态文件目录（如有）
├── Dockerfile            # 可选：构建镜像用
├── docker-compose.yml    # 可选：服务编排
└── README.md             # 本说明文件
```

---

## 🚀 启动方式

### ✅ 使用 Python 本地运行：

```bash
pip install flask docker
python app.py
```

默认监听在 `http://localhost:8000`

### ✅ 使用 Gunicorn（生产）：

```bash
gunicorn app:app --bind 0.0.0.0:5000
```

> 注意：使用 Gunicorn 时，如果你的代码中使用了 `docker.from_env()`，必须确保容器内可访问宿主机 Docker（如挂载 `/var/run/docker.sock`）

---

## 🛠 功能介绍

### 🔢 `/mian` — 面点配比计算器

输入任意面粉克数，选择对应类型（饺子皮、面条、馒头、馅饼皮、面包），自动计算所需水量和酵母量。

---

### 🎮 `/ddz` — 斗地主记分器

支持多轮积分记录，自动累计总分，页面互动式输入。

---

### 🖨 `/print` + `/restart` — 打印容器控制页

通过 Web 页面点击按钮，远程重启名为 `airprint` 的 Docker 容器。需要：

- 安装 Python Docker SDK
- 宿主机已安装并运行 Docker
- Flask 应用有权限访问 Docker 套接字（容器中运行时需挂载 `/var/run/docker.sock`）

---

## 🐳 使用 Docker（可选）

构建并启动服务：

```bash
docker build -t flask-mian .
docker run -p 8000:8000 flask-mian
```

或者使用 `docker-compose.yml`：

```bash
docker-compose up --build
```

---

## 🔐 注意事项

- 若 Flask 使用 `docker.from_env()`，请确保有权限访问宿主机 Docker 守护进程
- 默认目标容器名为 `airprint`，可根据实际场景修改

---

## 📌 TODO（可选优化）

- [ ] `/` 页面自动生成所有路由导航
- [ ] 打印控制页面支持状态查询
- [ ] 添加 Redis 做缓存优化
- [ ] 使用 Blueprint 分模块结构
- [ ] 配置 CI/CD 自动构建镜像推送

---

## 📄 License

MIT © 2025 CloudSmithy
