import re
from typing import List


def punctuation_split(line: str) -> List[str]:
    # TODO remove punctuation `.`(periods not decimals), `,`, `!`, `?`, `'`, `"`
    filtered = re.split(r"(?<!\d)[,.]|[,.](?!\d)|!|\?", line.strip())
    return list(filter(None, filtered))


def extra_spaces(line: str) -> str:
    # TODO remove multiple spaces '\s+'
    return re.sub(r"\s+", " ", line.strip())
