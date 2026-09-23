from langchain_community.llms import LlamaCpp
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
import re

# Load model
llm = LlamaCpp(
    model_path="./models/Phi-4-mini-instruct-Q4_K_M.gguf",
    temperature=0.7,
    max_tokens=512,
    n_ctx=2048,
    verbose=False,
    n_gpu_layers=0
)

#prompt
template = """You are a helpful assistant.
Answer ONLY the last Human question.
Give a short and direct answer.
Do not repeat the conversation history.
Do not write "Current conversation" or "Human:" or "AI:".

{history}
Human: {input}
AI:"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

memory = ConversationBufferMemory()
chatbot = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=False
)

print("Phi-4-mini Chatbot is ready!")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower().strip() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = chatbot.predict(input=user_input)

    # Clean the response - remove any leaked history
    cleaned = response.strip()
    cleaned = re.sub(r"(Current conversation:|Human:|AI:).*", "", cleaned, flags=re.DOTALL)
    cleaned = cleaned.strip()

    print(f"Bot: {cleaned}\n")