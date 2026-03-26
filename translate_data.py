import json
from data_translation_zh import (
    TITLES,
    CATEGORIES,
    OUTLOOK_DESC,
    EDUCATION,
    # EXPOSURE_RATIONALE,
)

with open("site/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["title"] = TITLES.get(item["title"], item["title"])
    item["category"] = CATEGORIES.get(item["category"], item["category"])
    item["outlook_desc"] = OUTLOOK_DESC.get(item["outlook_desc"], item["outlook_desc"])
    item["education"] = EDUCATION.get(item["education"], item["education"])
    # title = item["title"]
    # if title in EXPOSURE_RATIONALE:
    #     item["exposure_rationale"] = EXPOSURE_RATIONALE[title]

with open("site/data.zhCN.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已翻译 {len(data)} 条记录，输出到 site/data.zhCN.json")
