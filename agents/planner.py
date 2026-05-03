from core.llm import run_llm

def planner_agent(app_idea):
    return run_llm(
        system_prompt="You are a senior software architect.",
        user_prompt=f"""
        Break down this app idea:

        {app_idea}

        Include:
        - Features
        - Tech stack
        - Step-by-step plan
        """
    )