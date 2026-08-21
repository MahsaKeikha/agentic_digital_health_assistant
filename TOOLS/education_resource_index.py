def index_topics(topics: list[str]) -> dict:
    return {"topics": list(dict.fromkeys(topics)), "source_review_required": True}
