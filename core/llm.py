from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.2
)

def run_llm(system_prompt, user_prompt):
    print("⏳ Sending request to LLM...")

    try:
        response = llm.invoke([
            ("system", system_prompt),
            ("user", user_prompt)
        ])

        print("✅ Response received")
        return response.content

    except Exception as e:
        print("❌ Error:", e)
        return "LLM Error"