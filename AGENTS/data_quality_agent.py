class DataQualityAgent:
    name = "data_quality"

    def run(self, context: dict) -> dict:
        data = context.get("intake", {})
        return {"quality_reviewed": True, "fields_present": sorted(data.keys())}
