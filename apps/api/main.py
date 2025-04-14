# apps/api/main.py
from fastapi import FastAPI
import uvicorn # 引入 uvicorn

app = FastAPI(
    title="AI App API",
    description="API for the Next.js FastAPI AI Starter",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    """
    Root endpoint providing a welcome message.
    """
    return {"message": "Hello World from FastAPI backend!"}

# Example of another endpoint
@app.get("/api/v1/hello")
async def read_hello():
    return {"message": "Hello from API v1"}

# --- Development Server Runner ---
# This allows running 'python main.py' for development
# Production deployment should use Uvicorn directly (e.g., via gunicorn or docker)
if __name__ == "__main__":
    uvicorn.run(
        "main:app", # 指向 FastAPI 实例
        host="0.0.0.0", # 监听所有网络接口
        port=8000,      # 监听 8000 端口
        reload=True     # 开发模式下自动重载
    )