# brandling_ai/run.py

import openai
from brandling_ai.prompt import get_branding_prompt

openai.api_key = "your-api-key-here"  # 環境変数で管理するのが理想

def main():
    print("🔧 ブランド情報を入力してください：")
    user_input = ""
    fields = [
        ("商品名", "product"),
        ("カテゴリ", "category"),
        ("特徴（カンマ区切り）", "features"),
        ("ターゲット", "target"),
        ("価値観（カンマ区切り）", "values"),
        ("トーン", "tone"),
        ("使用シーン（カンマ区切り）", "use_scenes")
    ]
    for label, key in fields:
        val = input(f"{label}: ")
        user_input += f"{label}: {val}\n"

    prompt = get_branding_prompt(user_input)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたはマーケティングに詳しいAIアシスタントです。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    print("\n🧠 生成されたブランド情報：\n")
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    main()
