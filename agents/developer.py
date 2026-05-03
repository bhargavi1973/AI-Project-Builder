from core.llm import run_llm

def developer_agent(plan):
    return run_llm(
        system_prompt="""
        You are a strict developer.

        RULES:
        - Output ONLY code
        - Use format: FILE: <path>
        - No explanation
        """,
        user_prompt=f"""
        Build this project:

        {plan}
        """
    )