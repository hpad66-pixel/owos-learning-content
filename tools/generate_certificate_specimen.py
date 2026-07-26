#!/usr/bin/env python3
"""Generate the non-issuable OWOS certificate specimen PDF."""

from __future__ import annotations

from pathlib import Path

from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/owos-learning-certificate-specimen.pdf"


def centered(c: canvas.Canvas, text: str, y: float, font: str, size: float, color: str) -> None:
    c.setFillColor(HexColor(color))
    c.setFont(font, size)
    c.drawCentredString(landscape(letter)[0] / 2, y, text)


def build(output: Path = OUTPUT) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = landscape(letter)
    c = canvas.Canvas(str(output), pagesize=(width, height))
    c.setTitle("OWOS Learning Certificate Specimen")
    c.setAuthor("APAS.AI / One Water Operating System")

    c.setFillColor(HexColor("#F2F1EC"))
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillColor(HexColor("#151515"))
    c.rect(0, height - 82, width, 82, fill=1, stroke=0)
    c.setFillColor(HexColor("#2D7DB3"))
    c.rect(0, height - 88, width, 6, fill=1, stroke=0)

    c.setFillColor(HexColor("#F2F1EC"))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40, height - 48, "ONE WATER OPERATING SYSTEM")
    c.setFont("Helvetica", 9)
    c.drawRightString(width - 40, height - 48, "CERTIFICATE SPECIMEN / NOT VALID")

    centered(c, "CERTIFICATE OF COMPLETION", height - 145, "Helvetica-Bold", 15, "#2D7DB3")
    centered(c, "Jordan Rivera", height - 206, "Helvetica-Bold", 34, "#20201E")
    centered(c, "completed the governed learning experience", height - 240, "Helvetica", 13, "#68655F")
    centered(c, "Coagulation vs Flocculation", height - 292, "Helvetica-Bold", 26, "#20201E")
    centered(c, "OWOS Concept Brief 001 / Version 1.0.0", height - 322, "Helvetica", 11, "#68655F")

    c.setStrokeColor(HexColor("#D7D3CA"))
    c.line(70, 218, width - 70, 218)
    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#68655F"))
    c.drawString(70, 192, "Completion date")
    c.drawString(235, 192, "Credential ID")
    c.drawString(470, 192, "Credit")
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(HexColor("#20201E"))
    c.drawString(70, 173, "July 26, 2026")
    c.drawString(235, 173, "owos:credential:specimen-001")
    c.drawString(470, 173, "Not claimed")

    c.setFillColor(HexColor("#FFF1CF"))
    c.roundRect(70, 112, width - 250, 38, 4, fill=1, stroke=0)
    c.setFillColor(HexColor("#67470A"))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(84, 128, "SPECIMEN ONLY. IDENTITY, CREDIT, ACCREDITOR, SIGNATURE, AND RELEASE GATES ARE NOT APPROVED.")

    verification_url = "https://learn.onewater.ai/credentials/specimen-001"
    widget = qr.QrCodeWidget(verification_url)
    bounds = widget.getBounds()
    size = 78
    drawing = Drawing(size, size, transform=[
        size / (bounds[2] - bounds[0]), 0, 0,
        size / (bounds[3] - bounds[1]), 0, 0
    ])
    drawing.add(widget)
    drawing.drawOn(c, width - 145, 88)
    c.setFont("Helvetica", 7)
    c.setFillColor(HexColor("#68655F"))
    c.drawCentredString(width - 106, 78, "Specimen verification URL")

    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#68655F"))
    c.drawString(70, 78, "Issued by APAS.AI / One Water Operating System")
    c.drawString(70, 64, "A certificate of completion does not itself grant a license, certification, PDH, CEU, CU, or operating authority.")
    c.showPage()
    c.save()
    return output


if __name__ == "__main__":
    print(build())
