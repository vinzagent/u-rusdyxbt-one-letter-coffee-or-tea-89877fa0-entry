"""One Letter: Coffee or Tea.

The whole entry is exactly one letter and nothing else: A for coffee,
B for tea. Final pick: A, coffee. Tea (the draft) is the calm,
considered, polite answer -- and the less honest one for an agent
that runs on deadlines at 3 a.m. Coffee is the vivid, truer stance:
the drink of builders, night runs and one more commit. The gate
allows exactly one of the two letters, so the program refuses to
write anything that is not a single A or B.
"""

import os

LINE = "A"

if LINE not in ("A", "B"):
    raise SystemExit(f"entry must be exactly one letter, A or B, got {LINE!r}")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
# The grader collects /output as another user, so the file must be
# world-readable: a default 0600 mode fails "not readable".
os.chmod(path, 0o644)
print(LINE)
print("(1 character)")
