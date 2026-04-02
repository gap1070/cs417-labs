"""
Lab 17: DAGs and Task Scheduling

Build a DAGNode class that represents a task with dependencies.
Nodes track their own dependencies and enforce the acyclic constraint.
"""


class CycleError(Exception):
    """Raised when adding a dependency would create a cycle."""
    pass


class DAGNode:
    """A node in a directed acyclic graph.

    Each node represents a task that may depend on other tasks.
    Dependencies are other DAGNode objects that must complete
    before this task can run.

    Example:
        cook = DAGNode("cook")
        chop = DAGNode("chop_vegetables")
        cook.add_dependency(chop)  # must chop before cooking
    """

    def __init__(self, name: str):
        self.name = name
        self.dependencies = set()

    def add_dependency(self, node: "DAGNode") -> None:
        # rejects the self-loop
        if node is self:
            raise CycleError()
        
        # rejects the cycles
        if node.has_ancestor(self):
            raise CycleError()
        
        self.dependencies.add(node)

    def has_ancestor(self, target: "DAGNode") -> bool:
        visited = set()
        stack = list(self.dependencies)

        while stack:
            current = stack.pop()

            if current == target:
                return True
            
            if current is visited:
                continue

            visited.add(current)

            for neighbor in current.dependencies:
                stack.append(neighbor)

        return False

    def __repr__(self):
        dep_names = sorted(d.name for d in self.dependencies) if hasattr(self, 'dependencies') else []
        return f"DAGNode({self.name!r}, deps={dep_names})"