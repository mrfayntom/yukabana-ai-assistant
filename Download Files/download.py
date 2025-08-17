!pip install datasets --quiet

from datasets import load_dataset
import os

ds = load_dataset("wikimedia/wikipedia", "20231101.en", split="train")

sam_size = 200_000 if len(ds) > 200_000 else len(ds)
ds_sam = ds.shuffle(seed=42).select(range(sam_size))

save_pth = os.path.expanduser("~/Yukabana/wikipedia_1gb.jsonl") #your path
os.makedirs(os.path.dirname(save_pth), exist_ok=True)

ds_sam.to_json(save_pth, orient="records", lines=True)

print(save_pth)
