def apply(payload: dict) -> dict:
    return {"reviewed": True, "missing_evidence": payload.get("missing", [])}
