import json
from dataclasses import asdict


class JsonMixin:
    def to_json(self) -> str:
        return json.dumps(asdict(self), default=str, ensure_ascii=False)