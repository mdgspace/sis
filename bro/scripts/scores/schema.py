scores_data_schema = {
    "users": {
        "type": dict,
        "schema": {
            "name": {
                "type": str,
                "nullable": False
            },
            "score": {
                "type": int,
                "nullable": False
            }
        }
    }
}