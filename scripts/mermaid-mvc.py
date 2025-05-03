import mermaid as md
from mermaid.graph import Graph

sequence = Graph(
    "Sequence-diagram",
    """
flowchart TD
    M(board_model) --> |is observed by| B(board_view)
    B --> |interactions directly trigger| C(board_controller)
    C --> |instructs to update| M
""",
)
render = md.Mermaid(sequence)

render.to_png("mermaid-mvc.png")
