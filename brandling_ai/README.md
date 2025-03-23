# branding_ai/chat_runner.py

import os
import json
from datetime import datetime
from pathlib import Path

# 質問テンプレート
questions = [
    ("product", "まず、どんな商品を扱っていますか？（例：オーガニック紅茶）"),
    ("category", "商品はどんなカテゴリに分類されますか？（例：飲料、雑貨など）"),
    ("features", "その商品の特徴やこだわりを教えてください（カンマ区切りでOK）"),
    ("target", "どんな人に届けたいですか？（年齢層・ライフスタイルなど）"),
    ("values", "ブランドが大切にしている価値観は？（カンマ区切りでOK）"),
    ("tone", "文章やデザインにおけるブランドのトーンは？（例：やさしく、上品など）"),
    ("use_scenes", "どんなシーンで使われることを想定していますか？（カンマ区切りでOK）")
]

# データ保存先
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
chat_log_path = Path(f"data/chat_sessions/{timestamp}.json")
markdown_path = Path(f"data/brand_sheets/{timestamp}.md")

# 会話ログと回答格納用
conversation = []
answers = {}

# 会話開始
print("🗣 ブランドづくりを一緒に始めましょう。質問に答えてください。\n")

for key, question in questions:
    print(f"🤖 {question}")
    answer = input("あなた: ").strip()
    answers[key] = answer
    conversation.append({"role": "assistant", "message": question})
    conversation.append({"role": "user", "message": answer})

# フォルダ作成
chat_log_path.parent.mkdir(parents=True, exist_ok=True)
markdown_path.parent.mkdir(parents=True, exist_ok=True)

# ログ保存（JSON）
with open(chat_log_path, "w", encoding="utf-8") as f:
    json.dump({
        "timestamp": timestamp,
        "conversation": conversation
    }, f, ensure_ascii=False, indent=2)

# Markdown出力
markdown = f"""# ブランドシート（{timestamp}）

## 商品概要
{answers['product']}

## カテゴリ
{answers['category']}

## 特徴
- {"\n- ".join(answers['features'].split(","))}

## ターゲット
{answers['target']}

## ブランド価値観
- {"\n- ".join(answers['values'].split(","))}

## 使用シーン
- {"\n- ".join(answers['use_scenes'].split(","))}

## トーン
{answers['tone']}
"""

with open(markdown_path, "w", encoding="utf-8") as f:
    f.write(markdown)

print("\n✅ ブランディング情報を保存しました！")
print(f"- チャットログ: {chat_log_path}")
print(f"- ブランドシート: {markdown_path}")
