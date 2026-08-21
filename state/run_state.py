from dataclasses import dataclass, field

@dataclass
class RunState:
    phase: str = "intake"
    artifacts: dict = field(default_factory=dict)
    approvals: list = field(default_factory=list)
