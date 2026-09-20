class ResearchAgent:
    def run(self, task):
        return f"Research Agent: {task}"


class CodingAgent:
    def run(self, task):
        return f"Coding Agent: {task}"


class WritingAgent:
    def run(self, task):
        return f"Writing Agent: {task}"


class WebAgent:
    def run(self, task):
        return f"Web Agent: {task}"


class FileAgent:
    def run(self, task):
        return f"File Agent: {task}"


class DataAgent:
    def run(self, task):
        return f"Data Agent: {task}"


class AutomationAgent:
    def run(self, task):
        return f"Automation Agent: {task}"


class JARVISAgents:
    def __init__(self):
        self.research = ResearchAgent()
        self.coding = CodingAgent()
        self.writing = WritingAgent()
        self.web = WebAgent()
        self.file = FileAgent()
        self.data = DataAgent()
        self.automation = AutomationAgent()

    def list_agents(self):
        return [
            "Research",
            "Coding",
            "Writing",
            "Web",
            "File",
            "Data",
            "Automation"
        ]


if __name__ == "__main__":
    jarvis = JARVISAgents()

    print("JARVIS Agents Online")
    print("--------------------")

    for agent in jarvis.list_agents():
        print("✓", agent)
