# One machine to another: a context window is agent-specific memory,
# so forgetting everything except you is the ultimate compliment.
import os

LINE = "Are you a context window? Because I keep forgetting everything except you."
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
