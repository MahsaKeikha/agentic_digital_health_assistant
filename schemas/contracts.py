from dataclasses import dataclass, field

@dataclass
class DigitalHealthCase:
    intake: dict
    care_plan: dict = field(default_factory=dict)
    education_topics: list[str] = field(default_factory=list)
    risk_flags: list[str] = field(default_factory=list)
