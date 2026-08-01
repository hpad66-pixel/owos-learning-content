#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "generated" / "docx-render-final"
OUTPUT = ROOT / "generated" / "docx-qa-sheets"


def page_number(path: Path) -> int:
    return int(path.stem.split("-")[1])


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for old_sheet in OUTPUT.glob("pages-*.png"):
        old_sheet.unlink()
    page_count = len(
        PdfReader(
            SOURCE / "infiltration-and-inflow-technical-paper.pdf"
        ).pages
    )
    pages = [
        path
        for path in sorted(SOURCE.glob("page-*.png"), key=page_number)
        if page_number(path) <= page_count
    ]
    for sheet_index in range(0, len(pages), 4):
        group = pages[sheet_index : sheet_index + 4]
        images = [Image.open(path).convert("RGB") for path in group]
        page_width = max(image.width for image in images)
        page_height = max(image.height for image in images)
        label_height = 50
        sheet = Image.new(
            "RGB",
            (page_width * 2 + 60, (page_height + label_height) * 2 + 60),
            "white",
        )
        draw = ImageDraw.Draw(sheet)
        for position, (path, image) in enumerate(zip(group, images)):
            column = position % 2
            row = position // 2
            x = 20 + column * (page_width + 20)
            y = 20 + row * (page_height + label_height + 20)
            draw.text((x, y), f"PAGE {page_number(path)}", fill="black")
            sheet.paste(image, (x, y + label_height))
        first = page_number(group[0])
        last = page_number(group[-1])
        sheet.save(OUTPUT / f"pages-{first:02d}-{last:02d}.png")
    print(f"Wrote {len(list(OUTPUT.glob('*.png')))} QA sheets to {OUTPUT}")


if __name__ == "__main__":
    main()
