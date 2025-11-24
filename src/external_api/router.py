from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from src.external_api.service import service
from src.external_api.models import EmojiModel

router = APIRouter(prefix="/external", tags=["Emoji API"])


@router.get("/emoji", response_model=EmojiModel)
def get_emoji_data() -> EmojiModel:
    try:
        return service.get_random_emoji()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/emoji/html", response_class=HTMLResponse)
def get_emoji_html() -> str:
    try:
        result = service.get_random_emoji()
        emoji_char = result.html_code[0] if result.html_code else ""

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Random Emoji</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f2f5;
                }}
                .card {{
                    background: white;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                    text-align: center;
                    max-width: 400px;
                }}
                .emoji-display {{
                    font-size: 100px;
                    margin: 20px 0;
                }}
                h1 {{ color: #333; font-size: 24px; text-transform: capitalize; }}
                p {{ color: #666; }}
                .badge {{
                    display: inline-block;
                    padding: 5px 10px;
                    background-color: #e1ecf4;
                    color: #2c5282;
                    border-radius: 20px;
                    font-size: 0.9em;
                    margin-top: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <div class="emoji-display">{emoji_char}</div>
                <h1>{result.name}</h1>
                <p>Category: <strong>{result.category}</strong></p>
                <div class="badge">{result.group}</div>
            </div>
        </body>
        </html>
        """
        return html_content

    except Exception as e:
        return f"<h3>Error loading emoji: {e}</h3>"