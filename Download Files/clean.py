import json

in_fl = "/content/drive/MyDrive/Yukabana/wikipedia_1gb.jsonl"
out_fl = "/content/drive/MyDrive/Yukabana/wikipedia_2.jsonl"

with open(in_fl, "r", encoding="utf-8") as infile, open(out_fl, "w", encoding="utf-8") as outfile:
    for line in infile:
        try:
            data = json.loads(line.strip())
            title = data.get("title", "")
            text = data.get("text", "")

            if not title or not text:
                continue

            item = {
                "prompt": f"Explain about {title}.",
                "response": text.strip()
            }

            outfile.write(json.dumps(item, ensure_ascii=False) + "\n")

        except json.JSONDecodeError:
            continue

print("Saved instruction dataset to:", out_fl)
