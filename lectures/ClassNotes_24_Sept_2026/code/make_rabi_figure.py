#!/usr/bin/env python3
"""Generate the resonant two-state Rabi-oscillation figure."""

from math import cos, pi, sin
from pathlib import Path

from reportlab.lib.colors import HexColor, black
from reportlab.pdfgen import canvas


def main() -> None:
    output_dir = Path(__file__).resolve().parents[1] / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    width, height = 460.0, 270.0
    left, bottom, right, top = 58.0, 42.0, 440.0, 235.0
    pdf = canvas.Canvas(str(output_dir / "rabi_oscillations.pdf"), pagesize=(width, height))

    def xy(x: float, y: float) -> tuple[float, float]:
        return left + (right - left) * x / (2 * pi), bottom + (top - bottom) * y

    pdf.setStrokeColor(HexColor("#d0d0d0"))
    pdf.setLineWidth(0.5)
    for y in (0.0, 0.25, 0.5, 0.75, 1.0):
        x0, yy = xy(0.0, y)
        x1, _ = xy(2 * pi, y)
        pdf.line(x0, yy, x1, yy)

    pdf.setStrokeColor(black)
    pdf.setLineWidth(1.0)
    pdf.line(left, bottom, right, bottom)
    pdf.line(left, bottom, left, top)

    ticks = [(0, "0"), (pi / 2, "pi/2"), (pi, "pi"), (3 * pi / 2, "3pi/2"), (2 * pi, "2pi")]
    pdf.setFont("Helvetica", 9)
    for x, label in ticks:
        xx, yy = xy(x, 0.0)
        pdf.line(xx, yy - 3, xx, yy + 3)
        pdf.drawCentredString(xx, yy - 15, label)
    for y in (0.0, 0.25, 0.5, 0.75, 1.0):
        xx, yy = xy(0.0, y)
        pdf.line(xx - 3, yy, xx + 3, yy)
        pdf.drawRightString(xx - 7, yy - 3, f"{y:g}")

    def curve(func, color: str) -> None:
        path = pdf.beginPath()
        for index in range(601):
            x = 2 * pi * index / 600
            xx, yy = xy(x, func(x))
            (path.moveTo if index == 0 else path.lineTo)(xx, yy)
        pdf.setStrokeColor(HexColor(color))
        pdf.setLineWidth(2.0)
        pdf.drawPath(path)

    curve(lambda x: cos(x) ** 2, "#1f77b4")
    curve(lambda x: sin(x) ** 2, "#d62728")

    pdf.setFillColor(black)
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString((left + right) / 2, 14, "Omega t")
    pdf.saveState()
    pdf.translate(14, (bottom + top) / 2)
    pdf.rotate(90)
    pdf.drawCentredString(0, 0, "Probability")
    pdf.restoreState()

    pdf.setFont("Helvetica", 9)
    pdf.setStrokeColor(HexColor("#1f77b4"))
    pdf.line(125, 251, 148, 251)
    pdf.setFillColor(black)
    pdf.drawString(153, 247.5, "P0(t) = cos^2(Omega t)")
    pdf.setStrokeColor(HexColor("#d62728"))
    pdf.line(282, 251, 305, 251)
    pdf.setFillColor(black)
    pdf.drawString(310, 247.5, "P1(t) = sin^2(Omega t)")
    pdf.showPage()
    pdf.save()


if __name__ == "__main__":
    main()
