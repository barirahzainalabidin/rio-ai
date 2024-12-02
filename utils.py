import openai

def get_initial_message():
    messages=[
            {"role": "system", "content": "You're my personal assistance. Tell me more about data you have been analyzed and trained."},
            {"role": "user", "content": "Hye"},
            {"role": "assistant", "content": "What can i help you, today?"}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )
    return  response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
