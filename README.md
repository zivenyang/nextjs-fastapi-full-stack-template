# Next.js + FastAPI 全栈 AI 应用脚手架

这是一个基于 Next.js 15 和 FastAPI 的本地优先、生产级别的 AI Web 应用脚手架，采用 Monorepo 结构进行管理。

## 📝 项目概述

这个脚手架提供了一个快速启动 AI 相关 Web 应用开发的基础模板，特别关注：

- **本地优先体验**：确保应用在离线或网络不稳定时也能正常工作
- **生产级别设计**：遵循最佳实践，易于维护和扩展
- **现代化开发体验**：使用最新技术和工具链

## 🔧 技术栈

### 前端 (apps/web)
- **框架**: [Next.js 15+](https://nextjs.org/) - React 框架
- **语言**: [TypeScript](https://www.typescriptlang.org/)
- **样式**: [Tailwind CSS](https://tailwindcss.com/)
- **包管理器**: [pnpm](https://pnpm.io/)

### 后端 (apps/api)
- **框架**: [FastAPI](https://fastapi.tiangolo.com/) - Python Web 框架
- **Python 版本**: 3.9+ (推荐 3.12+)
- **包管理器**: [uv](https://github.com/astral-sh/uv) - 高速 Python 包管理器

### 项目管理
- **仓库结构**: Monorepo (使用 pnpm workspaces)
- **版本控制**: Git
- **依赖管理**: pnpm + uv

## 📁 项目结构

```
.
├── .github/            # GitHub Actions 配置 (CI/CD)
├── .vscode/            # VS Code 编辑器配置
├── apps/               # 应用程序
│   ├── web/            # Next.js 前端应用
│   │   ├── app/        # Next.js App Router 目录
│   │   ├── public/     # 静态资源
│   │   └── ...         # 其他前端相关文件
│   └── api/            # FastAPI 后端应用
│       ├── main.py     # FastAPI 主程序入口
│       └── ...         # 其他后端相关文件
├── packages/           # 共享代码包 (如有)
├── scripts/            # 项目脚本
├── .gitignore          # Git 忽略配置
├── LICENSE             # 开源许可证
├── package.json        # 项目根目录配置
├── pnpm-workspace.yaml # pnpm 工作区配置
└── README.md           # 项目说明文档 (本文件)
```

## 🚀 快速开始

### 前提条件

确保已安装以下工具：

- [Node.js](https://nodejs.org/) (v18+，推荐 v20+)
- [pnpm](https://pnpm.io/) (v9+，推荐 v10+)
- [Python](https://www.python.org/) (v3.9+，推荐 v3.12+)
- [uv](https://github.com/astral-sh/uv) (Python 包管理器)

### 安装

1. **克隆仓库**:
   ```bash
   git clone https://github.com/your-username/nextjs-fastapi-full-stack-template.git
   cd nextjs-fastapi-full-stack-template
   ```

2. **安装前端依赖**:
   ```bash
   pnpm install
   ```

3. **安装后端依赖**:
   ```bash
   cd apps/api
   uv venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   cd ../..
   ```

### 开发

#### 启动前端开发服务器:
```bash
pnpm dev:web
```
访问 [http://localhost:3000](http://localhost:3000) 查看前端应用

#### 启动后端开发服务器:
```bash
pnpm dev:api
```
访问 [http://localhost:8000/docs](http://localhost:8000/docs) 查看 API 文档

#### 同时启动前后端:
```bash
pnpm dev
```

### 构建和部署

#### 构建前端:
```bash
pnpm build:web
```

#### 运行前端生产版本:
```bash
pnpm start:web
```

#### 部署后端:
后端可使用 gunicorn、uvicorn 或 Docker 进行部署，详见文档。

## 🔮 AI 集成

该脚手架设计用于轻松集成各种 AI 服务：

- 支持本地和云端 AI 模型
- 可扩展以适应不同的 AI 提供商 (如 OpenAI, Anthropic, Gemini 等)
- 前后端协同处理 AI 请求和响应

## 🔄 工作流

1. 前端 (Next.js) 处理用户界面和交互
2. 后端 (FastAPI) 处理 API 请求和 AI 服务调用
3. 数据在前后端之间以 JSON 格式传输

## 🔬 未来计划

- [ ] 添加身份认证系统
- [ ] 集成数据库连接
- [ ] 提供 Docker 部署配置
- [ ] 添加自动化测试
- [ ] 简化 AI 服务集成

## 📄 许可证

该项目采用 [MIT 许可证](LICENSE)。 