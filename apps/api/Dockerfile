# apps/api/Dockerfile

# 使用官方 Python 镜像 (slim 版本更小)
FROM python:3.12-slim AS base

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装 uv
RUN pip install uv

# 创建工作目录
WORKDIR /app

# ---- Dependencies ----
# 单独安装依赖以利用缓存
FROM base AS dependencies
WORKDIR /app

# 复制依赖定义文件
COPY apps/api/pyproject.toml apps/api/uv.lock* ./

# 创建虚拟环境并安装依赖
# 使用 uv sync 确保环境与 lock 文件一致
RUN uv sync --frozen


# ---- Runner ----
# 创建最终的应用镜像
FROM base AS runner
WORKDIR /app

# 从依赖阶段复制虚拟环境
COPY --from=dependencies /app/.venv /app/.venv

# 将虚拟环境的 bin 目录添加到 PATH
ENV PATH="/app/.venv/bin:$PATH"

# 复制应用代码
COPY apps/api/ /app/

# 暴露端口
EXPOSE 8000

# 运行 uvicorn 生产服务器
# 注意：不使用 --reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]