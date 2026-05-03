from core.llm import run_llm

response = run_llm(
    "You are helpful",
    "Say hello in one line"
)

print(response)