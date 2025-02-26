from libertai_agents.models import get_model

from libertai_unstoppable_denver_agents.interfaces import AutonomousAgentConfig
from libertai_unstoppable_denver_agents.main import AutonomousAgent

autonomous_agent = AutonomousAgent(
    autonomous_config=AutonomousAgentConfig(
        compute_think_interval=1, compute_think_unit="hours"
    ),
    model=get_model("NousResearch/Hermes-3-Llama-3.1-8B"),
    system_prompt="You are a helpful agent that can interact onchain using an Ethereum Account Wallet. You have tools to send transactions, query blockchain data, and interact with contracts. If you run into a 5XX (internal) error, ask the user to try again later.",
    tools=[],
    expose_api=True,
)

app = autonomous_agent.agent.app
