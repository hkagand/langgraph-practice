from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
   message : str

def greeting_node(state: AgentState) -> AgentState:
    state['message'] = "Hello " + state['message'] + "!, How can I assist you today?"
    return state

graph = StateGraph(AgentState)
graph.add_node('greeter', greeting_node)

graph.set_entry_point('greeter')
graph.set_finish_point('greeter')

app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({'message': 'Bob'})

print(result["message"])
