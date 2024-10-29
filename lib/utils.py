from typing import Dict, Any

def extract_key_data(data: Dict[str, Any], extractor_key: str) -> str | bytes | None:
    nested_level = extractor_key.split('.')
    result = data
    if len(nested_level) == 1:
        return data[nested_level[0]]
    for key in nested_level:
        result = result.get(key, data)
    return result
