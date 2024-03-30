import gradio as gr
from transformers import pipeline,Conversation

chatbot = pipeline(model="facebook/blenderbot-400M-distill")


message_list = []
response_list = []

def yes_man(message, history):
    conversation = chatbot(message)
    

    return conversation[0]['generated_text']
chatbot("Hi, how are you?")[0]["generated_text"]


gr.ChatInterface(
    yes_man,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
    title="A vanilla",
    description="Ask Yes Man any question",
    theme="soft",
    examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch(debug=True)