import os
import json
import yaml

config_path = os.environ["CONFIG_FILE_PATH"]

with open(config_path, "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

config_json = json.dumps(cfg)

output_path = os.environ["GITHUB_OUTPUT"]
with open(output_path, "a", encoding="utf-8") as fh:
    fh.write(f"config={config_json}\n")

