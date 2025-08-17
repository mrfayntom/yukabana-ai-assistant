import shutil
import os

src_pth = os.path.expanduser("~/Yukabana/wikipedia_1gb.jsonl")
out_dir = "/content/drive/MyDrive/Yukabana"
out_path = os.path.join(out_dir, "wikipedia_1gb.jsonl")

os.makedirs(out_dir, exist_ok=True)

if os.path.exists(src_pth):
    shutil.move(src_pth, out_path)
    print(f"Successfully moved {src_pth} to {out_path}")
else:
    print(f"Source file {src_pth} does not exist.")
