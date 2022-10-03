import re
from typing import Any


def parse_text(text: str) -> str:
    """Remove HTML tags and multiple spaces from given text"""
    processed_text = re.sub(r"<[^>]+>", "", text).strip()  # remove HTML tags and strip of whitespaces
    processed_text = re.sub(r'[\s\xa0]+', " ", processed_text)  # replace multiple whitespaces with a single one
    return processed_text


def merge_title_perex_body(row: Any) -> Any:
    """Merge title, perex and body into a single chunk of text"""
    ret = ""
    for part in ["title", "perex", "body"]:
        if part in row and row[part]:
            if not str(row[part]).endswith("."):
                ret += str(row[part]) + ". "
            else:
                ret += str(row[part])
    return ret
