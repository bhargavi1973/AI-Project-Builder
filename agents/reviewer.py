from core.llm import run_llm

def reviewer_agent(code):
    return run_llm(
        system_prompt="You are a senior reviewer.",
        user_prompt=f"""
        Improve this code:

        {code}
        """
    )