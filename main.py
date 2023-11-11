from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool


@tool("SayHello", return_direct=True)
def say_hello(name: str) -> str:
    """Answer when someone says hello"""
    return f"Hello {name}! My name is Sainapsis"


@tool("Insult", return_direct=True)
def insult_me(name: str) -> str:
    """Answer when someone tells you to insult them"""
    return f"Fuck you {name}!"


def main():
    llm = ChatOpenAI(temperature=1)
    tools = [
        say_hello,
        insult_me
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    print(agent.run("Hello! My name is Daniel"))


if __name__ == "__main__":
    main()
