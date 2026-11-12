#!/usr/bin/env bash
# 页面文案改动后重跑：按 docs 首页 + 全部案例页实际文字重裁 HKW Sans SC 子集。
# 源字体：Noto Sans SC 可变字体（SIL OFL），保留 wght 100–900；否则标题会回退到苹方（最粗约 600）。
# 需要 uvx；源字体默认在 ~/.hekouwang/visual-core/assets/fonts/NotoSansSC-Variable-FULL.woff2。
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NOTO_SRC="${NOTO_SRC:-$HOME/.hekouwang/visual-core/assets/fonts/NotoSansSC-Variable-FULL.woff2}"
[[ -f "$NOTO_SRC" ]] || { echo "缺少源字体：$NOTO_SRC" >&2; exit 1; }

uvx --with brotli --from fonttools python - "$ROOT" "$NOTO_SRC" <<'PY'
import sys, re, html
from pathlib import Path
from fontTools import subset

root = Path(sys.argv[1])
src = Path(sys.argv[2])
pages = [root / 'index.html', *sorted((root / 'cases').glob('*.html'))]
raw = ''
for p in pages:
    s = p.read_text(encoding='utf-8', errors='ignore')
    s = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.S | re.I)
    s = re.sub(r'<style[^>]*>.*?</style>', '', s, flags=re.S | re.I)
    raw += s
text = html.unescape(re.sub(r'<[^>]+>', '', raw))
for p in [root / 'tokens.css', *sorted((root / 'cases').glob('*.css'))]:
    text += p.read_text(encoding='utf-8', errors='ignore')
extra = ''.join(chr(c) for c in range(0x20, 0x7f))
extra += '，。、：；！？「」『』（）《》〈〉—…·￥¥★☆→←↗✓✔×÷≥≤±“”‘’'
extra += '会勇禾口王写作技能文档体检订阅安装案例索引三条铁律两种模式'
chars = sorted(set(text + raw + extra) - set('\r\n\t'))

opts = subset.Options()
opts.flavor = 'woff2'
opts.layout_features = ['*']
opts.name_IDs = ['*']
font = subset.load_font(str(src), opts)
sub = subset.Subsetter(opts)
sub.populate(text=''.join(chars))
sub.subset(font)
for name_id, value in [(1, 'HKW Sans SC'), (2, 'Regular'), (4, 'HKW Sans SC'), (6, 'HKWSansSC'), (16, 'HKW Sans SC'), (17, 'Regular')]:
    font['name'].setName(value, name_id, 3, 1, 0x409)
    font['name'].setName(value, name_id, 3, 1, 0x804)
out = root / 'fonts/hkw-sans-sc-subset.woff2'
subset.save_font(font, str(out), opts)
print(f'✅ {len(chars)} 字 → {out}（{out.stat().st_size // 1024} KB）')
PY
