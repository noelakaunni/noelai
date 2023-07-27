import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a persondal assistant"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Noel's AI")

#demo.launch(share=True)