from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors


OUT = "bravo-robot-coloring-cards.pdf"


def rr(c, x, y, w, h, r, stroke=1, fill=0):
    c.roundRect(x, y, w, h, r, stroke=stroke, fill=fill)


def line(c, x1, y1, x2, y2):
    c.line(x1, y1, x2, y2)


def draw_shape(c, kind, x, y, size=12):
    r = size / 2
    if kind == "circle":
        c.circle(x, y, r, stroke=1, fill=0)
    elif kind == "square":
        c.rect(x - r, y - r, size, size, stroke=1, fill=0)
    elif kind == "triangle":
        p = c.beginPath()
        p.moveTo(x, y + r)
        p.lineTo(x - r, y - r)
        p.lineTo(x + r, y - r)
        p.close()
        c.drawPath(p, stroke=1, fill=0)
    elif kind == "diamond":
        p = c.beginPath()
        p.moveTo(x, y + r)
        p.lineTo(x - r, y)
        p.lineTo(x, y - r)
        p.lineTo(x + r, y)
        p.close()
        c.drawPath(p, stroke=1, fill=0)
    elif kind == "star":
        p = c.beginPath()
        pts = [
            (x, y + r),
            (x + r * 0.28, y + r * 0.28),
            (x + r, y + r * 0.2),
            (x + r * 0.43, y - r * 0.14),
            (x + r * 0.6, y - r),
            (x, y - r * 0.52),
            (x - r * 0.6, y - r),
            (x - r * 0.43, y - r * 0.14),
            (x - r, y + r * 0.2),
            (x - r * 0.28, y + r * 0.28),
        ]
        p.moveTo(*pts[0])
        for pt in pts[1:]:
            p.lineTo(*pt)
        p.close()
        c.drawPath(p, stroke=1, fill=0)


def draw_speech_bubble(c, x, y, w, h):
    c.setLineWidth(2.4)
    rr(c, x, y, w, h, 18)
    p = c.beginPath()
    p.moveTo(x + w * 0.42, y)
    p.lineTo(x + w * 0.35, y - 18)
    p.lineTo(x + w * 0.54, y)
    c.drawPath(p, stroke=1, fill=0)

    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 35)
    c.drawCentredString(x + w / 2, y + h / 2 - 12, "BRAVO!")


def draw_robot(c, cx, base_y, scale=1.0):
    s = scale
    c.saveState()
    c.translate(cx, base_y)
    c.scale(s, s)
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.white)
    c.setLineJoin(1)
    c.setLineCap(1)

    # Color only the left half so children can finish the robot symmetrically.
    c.saveState()
    clip = c.beginPath()
    clip.rect(-160, -100, 160, 360)
    c.clipPath(clip, stroke=0, fill=0)
    c.setFillColor(colors.HexColor("#9fd7ff"))
    rr(c, -72, 125, 144, 82, 18, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#ffd166"))
    rr(c, -82, 2, 164, 105, 20, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#95d67f"))
    rr(c, -143, 103, 31, 28, 10, stroke=0, fill=1)
    rr(c, -57, -65, 36, 67, 13, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#f8a5c2"))
    rr(c, -76, -87, 67, 24, 11, stroke=0, fill=1)
    rr(c, -92, 150, 20, 35, 8, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#c7b8ff"))
    rr(c, -25, 105, 50, 22, 8, stroke=0, fill=1)
    c.circle(0, 63, 24, stroke=0, fill=1)
    c.restoreState()
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.white)

    # Antenna
    c.setLineWidth(3)
    line(c, 0, 206, 0, 234)
    c.circle(0, 243, 8, stroke=1, fill=0)
    line(c, -15, 218, -35, 236)
    c.circle(-42, 242, 7, stroke=1, fill=0)
    line(c, 15, 218, 35, 236)
    c.circle(42, 242, 7, stroke=1, fill=0)

    # Head
    c.setLineWidth(3.4)
    rr(c, -72, 125, 144, 82, 18)
    c.circle(-32, 168, 13, stroke=1, fill=0)
    c.circle(32, 168, 13, stroke=1, fill=0)
    c.circle(-32, 168, 4, stroke=1, fill=0)
    c.circle(32, 168, 4, stroke=1, fill=0)
    c.arc(-34, 140, 34, 166, 205, 130)
    line(c, -72, 188, 72, 188)
    line(c, -50, 207, -50, 222)
    line(c, 50, 207, 50, 222)

    # Ears
    rr(c, -92, 150, 20, 35, 8)
    rr(c, 72, 150, 20, 35, 8)

    # Neck
    rr(c, -25, 105, 50, 22, 8)

    # Body
    rr(c, -82, 2, 164, 105, 20)
    c.circle(0, 63, 24, stroke=1, fill=0)
    line(c, -17, 63, 17, 63)
    line(c, 0, 46, 0, 80)
    rr(c, -58, 78, 42, 16, 7)
    rr(c, 16, 78, 42, 16, 7)
    c.circle(-46, 32, 7, stroke=1, fill=0)
    c.circle(-20, 32, 7, stroke=1, fill=0)
    c.circle(20, 32, 7, stroke=1, fill=0)
    c.circle(46, 32, 7, stroke=1, fill=0)

    # Arms
    c.setLineWidth(3.2)
    line(c, -82, 84, -118, 111)
    line(c, 82, 84, 118, 111)
    rr(c, -143, 103, 31, 28, 10)
    rr(c, 112, 103, 31, 28, 10)
    line(c, -133, 131, -138, 148)
    line(c, -125, 131, -124, 151)
    line(c, -117, 130, -110, 146)
    line(c, 133, 131, 138, 148)
    line(c, 125, 131, 124, 151)
    line(c, 117, 130, 110, 146)

    # Legs and feet
    rr(c, -57, -65, 36, 67, 13)
    rr(c, 21, -65, 36, 67, 13)
    rr(c, -76, -87, 67, 24, 11)
    rr(c, 9, -87, 67, 24, 11)
    line(c, -38, -12, -38, -55)
    line(c, 38, -12, 38, -55)

    # Decorative colorable panels
    c.setDash(5, 4)
    rr(c, -65, 13, 130, 83, 14)
    c.setDash()
    c.circle(-55, 193, 4, stroke=1, fill=0)
    c.circle(55, 193, 4, stroke=1, fill=0)

    c.restoreState()


def draw_color_key(c, x, y):
    c.saveState()
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.black)
    c.setLineWidth(1.7)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "Color key")

    items = [
        ("circle", "BLUE"),
        ("square", "RED"),
        ("triangle", "GREEN"),
        ("star", "YELLOW"),
        ("diamond", "ORANGE"),
    ]

    c.setFont("Helvetica-Bold", 10)
    for index, (shape, label) in enumerate(items):
        row_y = y - 25 - index * 28
        draw_shape(c, shape, x + 12, row_y + 3, 14)
        c.drawString(x + 30, row_y, f"= {label}")
    c.restoreState()


def draw_card(c, x, y, w, h):
    c.saveState()
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.white)

    # Cut boundary for each prize.
    c.setDash(7, 5)
    c.setLineWidth(1.2)
    rr(c, x + 12, y + 10, w - 24, h - 20, 10)
    c.setDash()

    # Name line
    c.setLineWidth(1.8)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(x + 28, y + h - 40, "Name:")
    line(c, x + 82, y + h - 37, x + w - 28, y + h - 37)

    # Speech bubble and robot
    bubble_w = 250
    bubble_h = 68
    draw_speech_bubble(c, x + (w - bubble_w) / 2, y + h - 150, bubble_w, bubble_h)
    draw_robot(c, x + w / 2, y + 198, 0.90)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(x + w / 2, y + 100, "I AM LEO THE ROBOT")
    c.restoreState()


def main():
    w, h = landscape(A4)
    c = canvas.Canvas(OUT, pagesize=landscape(A4))
    c.setTitle("Bravo robot coloring cards")

    # Center cut line.
    c.setStrokeColor(colors.black)
    c.setLineWidth(1.1)
    c.setDash(8, 5)
    line(c, w / 2, 24, w / 2, h - 24)
    c.setDash()
    c.setFont("Helvetica", 8)
    c.drawCentredString(w / 2, 14, "cut here")

    draw_card(c, 0, 0, w / 2, h)
    draw_card(c, w / 2, 0, w / 2, h)

    c.showPage()
    c.save()


if __name__ == "__main__":
    main()
