"""Wrap original Test 2 raster excerpts in self-contained, theme-aware SVGs.

Run from any directory. Original PNGs and their source provenance are preserved.
Dark mode uses luminance inversion with hue compensation; it does not assign
mechanistic role colors to source annotations. No external image references.
"""
import base64
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / 'figures/test2_source_manifest.json').read_text())
    mapping = {}
    for entry in manifest:
        source = ROOT / entry['asset']
        if source.suffix != '.png':
            continue
        width, height = Image.open(source).size
        encoded = base64.b64encode(source.read_bytes()).decode('ascii')
        target = source.with_suffix('.svg')
        target.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>{source.stem}: original lecture or textbook excerpt</title>
<desc>Original PNG in light mode; hue-compensated luminance inversion in dark mode. Source provenance: figures/test2_source_manifest.json.</desc>
<style>@media (prefers-color-scheme:dark){{image{{filter:url(#dark)}}}}</style>
<defs><filter id="dark" color-interpolation-filters="sRGB" x="0" y="0" width="100%" height="100%"><feColorMatrix type="hueRotate" values="180"/><feComponentTransfer><feFuncR type="linear" slope="-1" intercept="1"/><feFuncG type="linear" slope="-1" intercept="1"/><feFuncB type="linear" slope="-1" intercept="1"/></feComponentTransfer><feComponentTransfer><feFuncR type="gamma" amplitude="0.78431372549" exponent="0.6" offset="0.11764705882"/><feFuncG type="gamma" amplitude="0.78431372549" exponent="0.6" offset="0.11764705882"/><feFuncB type="gamma" amplitude="0.78431372549" exponent="0.6" offset="0.11764705882"/></feComponentTransfer></filter></defs>
<image width="{width}" height="{height}" href="data:image/png;base64,{encoded}"/>
</svg>
''')
        mapping[source.relative_to(ROOT).as_posix()] = target.relative_to(ROOT).as_posix()
    modified = []
    for directory in ['notes', 'practice', 'wiki']:
        for doc in (ROOT / directory).rglob('*.md'):
            text = doc.read_text()
            updated = text
            for source, target in mapping.items():
                updated = updated.replace(source, target)
            if updated != text:
                doc.write_text(updated)
                modified.append(doc.relative_to(ROOT).as_posix())
    print(json.dumps({'wrappers': len(mapping), 'documents': modified}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
