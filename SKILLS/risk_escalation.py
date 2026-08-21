def apply(flags: list[str]) -> dict:
    return {"requires_human_review": bool(flags), "flags": flags}
