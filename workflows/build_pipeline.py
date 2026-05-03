from agents.planner import planner_agent
from agents.developer import developer_agent
from agents.tester import tester_agent
from agents.reviewer import reviewer_agent
from tools.parser import parse_and_save

def build_app(idea):
    print("\n🧠 Planning...")
    plan = planner_agent(idea)

    print("\n💻 Generating code...")
    code = developer_agent(plan)

    print("\n📂 Saving files...")
    parse_and_save(code)

    print("\n🧪 Testing...")
    test_report = tester_agent(code)
    print(test_report)

    print("\n🔍 Reviewing...")
    final_code = reviewer_agent(code)

    return final_code