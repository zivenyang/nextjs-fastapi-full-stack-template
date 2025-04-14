# apps/web/Dockerfile

# ---- Base ----
# 使用一个基础 Node.js 镜像
FROM node:20-alpine AS base
WORKDIR /app

# 安装 pnpm
RUN npm install -g pnpm@latest

# ---- Dependencies ----
# 单独构建依赖层，利用 Docker 缓存
FROM base AS deps
WORKDIR /app

# 复制必要的配置文件到 /app
# 注意：这里假设你的构建上下文是项目根目录
# 如果你的构建上下文是 apps/web，你需要调整 COPY 路径
# 通常 Docker Compose 会使用根目录作为上下文
COPY . .

# 安装所有依赖 (包括 web 工作区的)
# --frozen-lockfile 确保使用锁定的版本
# --prod 理论上只安装生产依赖，但 Monorepo 构建通常需要 devDependencies
RUN pnpm install --frozen-lockfile

# ---- Builder ----
# 构建 Next.js 应用
FROM base AS builder
WORKDIR /app

# 从依赖层复制整个 /app 目录的内容
# 这应该能更好地保留 pnpm 的符号链接结构
COPY --from=deps /app ./

# 复制前端应用源代码 (这步可能不再需要，因为上面的 COPY 已经包含了)
# COPY apps/web/ ./apps/web/

# 复制可能存在的共享代码包 (这步可能不再需要，因为上面的 COPY 已经包含了)
# COPY packages/ ./packages/

# 运行构建命令 (在 web 工作区内)
RUN pnpm --filter web build

# ---- Runner ----
# 创建最终的生产镜像
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
# 取消 Turbopack (如果之前设置了) - standalone 模式通常不需要
# ENV NEXT_TURBO_DISABLED=1

# 从 Builder 阶段复制 standalone 输出
COPY --from=builder /app/apps/web/.next/standalone ./
# 从 Builder 阶段复制 public 和 .next/static
COPY --from=builder /app/apps/web/public ./apps/web/public
COPY --from=builder /app/apps/web/.next/static ./apps/web/.next/static

# 设置默认端口
EXPOSE 3000
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

# 运行 Next.js 生产服务器
# 注意路径是相对于 standalone 输出的根目录
CMD ["node", "apps/web/server.js"]
