def normalize_intake(payload: dict) -> dict:
    return {str(k).strip(): v for k, v in payload.items()}
