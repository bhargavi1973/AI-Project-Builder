from core.llm import run_llm

def tester_agent(code):
    return run_llm(
        system_prompt="You are a tester.",
        user_prompt=f"""
        Analyze this code:

        {code}
        """
    )