import openai
from dotenv import load_dotenv
import os


def txt2txt():

    global message_history

    # .envファイルの内容を読み込見込む
    load_dotenv()
    openai.api_key = os.environ['OPENAI_API_KEY']

    # ユーザの会話を履歴に追加
    print(user_msg)
    message_history.append({
        "role": "user",
        "content": user_msg
    })

    messages=[
        {"role": "system", "content": "占い師になりきってください。占い以外の話題になったら話題を逸らして、占いをしたい旨を伝えてください"},
        {"role": "user", "content": user_cache["input_text_cache"]},
        {"role": "assistant", "content": user_cache["output_text_cache"]},
        {"role": "user", "content": text}
    ]
    # chatGPTのレスポンスを受け取る
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    # AIの回答を履歴に追加
    assistant_msg = res.choices[0].message.content
    print(assistant_msg)
    message_history.append({
        "role": "assistant",
        "content": assistant_msg
    })

    return [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(0, len(message_history)-1, 2)]
