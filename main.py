from agents import JARVISAgents


def choose_agent(jarvis, task):
    text = task.lower()

    if any(x in text for x in ["code", "python", "program", "coding", "bug"]):
        return jarvis.coding

    if any(x in text for x in ["search", "research", "study", "information"]):
        return jarvis.research

    if any(x in text for x in ["website", "web", "internet"]):
        return jarvis.web

    if any(x in text for x in ["file", "folder", "document", "pdf"]):
        return jarvis.file

    if any(x in text for x in ["data", "excel", "table"]):
        return jarvis.data

    if any(x in text for x in ["write", "letter", "essay", "assignment"]):
        return jarvis.writing

    if any(x in text for x in ["automate", "automation", "routine"]):
        return jarvis.automation

    return jarvis.writing


def main():
    jarvis = JARVISAgents()

    print("=" * 45)
    print("           JARVIS AI SYSTEM")
    print("=" * 45)
    print("Agents: Research | Coding | Web | File")
    print("        Data | Writing | Automation")
    print("Type 'agents' to see all agents.")
    print("Type 'exit' to stop.")

    while True:
        task = input("\nYou: ").strip()

        if task.lower() in ["exit", "quit"]:
            print("JARVIS: Goodbye!")
            break

        if task.lower() == "agents":
            print("\nAvailable Agents:")
            for agent in jarvis.list_agents():
                print("✓", agent)
            continue

        if not task:
            continue

        agent = choose_agent(jarvis, task)
        print("JARVIS:", agent.run(task))


if __name__ == "__main__":
    main()
