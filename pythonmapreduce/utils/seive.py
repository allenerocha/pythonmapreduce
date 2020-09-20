import re
from typing import List


def punctuation_split(line: str) -> List[str]:
    filtered = re.split(r"(?<!\d)[,.]|[,.](?!\d)|!|\?", line.strip())
    return list(filter(None, filtered))


def extra_spaces(line: str) -> str:
    return re.sub(r"\s+", " ", line.strip())
