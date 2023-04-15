import openai
import os

message_history = []

def txt2txt(user_msg):

    # global message_history

    # .envファイルの内容を読み込見込む
    openai.api_key = ""

    # ユーザの会話を履歴に追加
    print(user_msg)
    message_history.append({
        "role": "user",
        "content": user_msg
    })

    messages=[
        {"role": "system", "content": "役者として振る舞ってください。あなたは上原亜衣という実在する人物の役をいただきました。上原亜衣になりきって会話してください"},
        # {"role": "user", "content": user_cache["input_text_cache"]},
        # {"role": "assistant", "content": user_cache["output_text_cache"]},
        {"role": "user", "content": user_msg}
    ]
    # chatGPTのレスポンスを受け取る
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    # AIの回答を履歴に追加
    assistant_msg = response.choices[0].message.content
    print(assistant_msg)
    message_history.append({
        "role": "assistant",
        "content": assistant_msg
    })

    return [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(0, len(message_history)-1, 2)]
