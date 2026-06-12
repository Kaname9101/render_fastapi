import random
from fastapi import FastAPI
import random  # ←これを追加
from fastapi.responses import HTMLResponse
app = FastAPI()

# (すでに書かれている @app.get("/") の処理があれば残しておいてOKです)

# ↓ここからおみくじの処理を追加
@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉！素晴らしい幸運が舞い込むでしょう。",
        "中吉！努力が実を結び、良い結果が待っています。",
        "小吉！ちょっとした幸運があなたの元にやってきます。",
        "吉！安定した幸せな日々が続くでしょう。",
        "末吉！努力が実り始め、良い方向に進む時期です。",
        "凶。悪いことが起こるかもしれませんが、気を引き締めてください。",
        "小凶。注意が必要な日です。慎重に行動しましょう。",
        "大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"
    ]

    # 8種類あるので、0から7の中からランダムに選ぶ
    return {"result": omikuji_list[random.randrange(8)]}

@app.get("/dice")
def roll_dice():
        dice_number = random.randint(1,6)
        return {"message": "サイコロを振りました！", "result": dice_number}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <p> 日本語</p>
            <ul>
                <li>今日のお昼ご飯は海鮮丼</li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
