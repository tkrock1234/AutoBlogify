def get_branding_prompt(user_input: str) -> str:
    return f"""
あなたは、ブランドづくりを支援するコンテンツ戦略の専門家AIです。

以下のユーザー入力をもとに、ブランド情報を整理し、マーケティング・記事生成に使えるように構造化されたJSONで出力してください。

ユーザー入力:
{user_input}

出力形式:
{{
  "product": "",
  "category": "",
  "features": [],
  "target": "",
  "values": [],
  "tone": "",
  "use_scenes": []
}}
"""
