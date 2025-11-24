import uvicorn
from fastapi import FastAPI
from src.external_api.router import router as external_router

app = FastAPI(
    title="EmojiHub Wrapper API",
    description="Сервіс для отримання випадкових емодзі через EmojiHub API",
    version="1.0.0"
)

app.include_router(external_router)

@app.get("/")
def root():
    return {
        "message": "API працює успішно!",
        "documentation": "/docs",
        "random_emoji_json": "/external/emoji",
        "random_emoji_html": "/external/emoji/html"
    }

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8080, reload=True)