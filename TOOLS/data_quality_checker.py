def missing_fields(payload: dict, required: list[str]) -> list[str]:
    return [key for key in required if payload.get(key) in (None, "")]
