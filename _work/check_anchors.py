# 复刻 github-slugger 的去标点规则，检查 README 站内锚点能否对上真实标题
import re, io, sys

RANGES = [
    (0x00, 0x1F), (0x21, 0x2C), (0x2E, 0x2F), (0x3A, 0x40),
    (0x5B, 0x5E), (0x60, 0x60), (0x7B, 0x7E),
    (0xA1, 0xA1), (0xA7, 0xA7), (0xAB, 0xAB), (0xB6, 0xB7), (0xBB, 0xBB), (0xBF, 0xBF),
    (0x2010, 0x2027), (0x2030, 0x205E),
    (0x3001, 0x3003), (0x3008, 0x3011), (0x3014, 0x301F), (0x3030, 0x3030),
    (0xFF01, 0xFF03), (0xFF05, 0xFF0A), (0xFF0C, 0xFF0F),
    (0xFF1A, 0xFF1B), (0xFF1F, 0xFF20), (0xFF3B, 0xFF3D), (0xFF5B, 0xFF5E),
]
PUNCT = re.compile("[" + "".join(
    "\\u%04x-\\u%04x" % (a, b) for a, b in RANGES) + "]")


def slug(text):
    return PUNCT.sub("", text.strip().lower()).replace(" ", "-")


path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
s = io.open(path, encoding="utf-8").read()
heads = {slug(re.sub(r"^#+\s*", "", l)) for l in s.split("\n") if l.startswith("#")}
used = set(re.findall(r"\]\(#([^)]+)\)", s))
bad = sorted(a for a in used if a not in heads)
print("%s：标题 %d 个，站内锚点 %d 个，对不上 %d 个" % (path, len(heads), len(used), len(bad)))
for a in bad:
    print("   !!", a)
    print("      现有标题：", ", ".join(sorted(h for h in heads if h)[:40]))
sys.exit(1 if bad else 0)
