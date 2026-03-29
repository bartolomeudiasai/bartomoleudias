from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm
import re

ROOT = Path(__file__).resolve().parent
src = ROOT / "build-your-first-ai-agent-playbook.md"
out = ROOT / "build-your-first-ai-agent-playbook.pdf"

text = src.read_text(encoding="utf-8")
lines = text.splitlines()

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER, fontSize=24, leading=28, spaceAfter=12))
styles.add(ParagraphStyle(name="SubtitleCenter", parent=styles["Heading2"], alignment=TA_CENTER, textColor=colors.HexColor("#444444"), fontSize=13, leading=17, spaceAfter=18))
styles.add(ParagraphStyle(name="Chapter", parent=styles["Heading1"], fontSize=18, leading=22, spaceBefore=10, spaceAfter=10, textColor=colors.HexColor("#111111")))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontSize=13, leading=16, spaceBefore=8, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyTight", parent=styles["BodyText"], fontSize=10.5, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name="BulletTight", parent=styles["BodyText"], fontSize=10.5, leading=14, leftIndent=14, bulletIndent=4, spaceAfter=3))


def inline_md(s: str) -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawRightString(195 * mm, 10 * mm, str(doc.page))
    canvas.restoreState()

story = []
first_title_done = False
for raw in lines:
    line = raw.rstrip()
    if not line:
        story.append(Spacer(1, 4))
        continue
    if line == "---":
        story.append(Spacer(1, 6))
        continue
    if line.startswith("# ") and not first_title_done:
        story.append(Spacer(1, 12))
        story.append(Paragraph(inline_md(line[2:].strip()), styles["TitleCenter"]))
        first_title_done = True
        continue
    if line.startswith("## Subtitle"):
        continue
    if first_title_done and not any(x.startswith("## ") for x in [line]) and not line.startswith("### ") and not line.startswith("#### ") and not line.startswith("- ") and not re.match(r"^\d+\. ", line) and raw == line and line and story and isinstance(story[-1], Paragraph) and story[-1].style.name == "TitleCenter":
        story.append(Paragraph(inline_md(line), styles["SubtitleCenter"]))
        story.append(PageBreak())
        continue
    if line.startswith("## Chapter "):
        story.append(PageBreak())
        story.append(Paragraph(inline_md(line[3:].strip()), styles["Chapter"]))
        continue
    if line.startswith("## "):
        story.append(Paragraph(inline_md(line[3:].strip()), styles["Chapter"]))
        continue
    if line.startswith("### "):
        story.append(Paragraph(inline_md(line[4:].strip()), styles["Section"]))
        continue
    if line.startswith("#### "):
        story.append(Paragraph(inline_md(line[5:].strip()), styles["BodyTight"]))
        continue
    if line.startswith("- "):
        story.append(Paragraph(inline_md(line[2:].strip()), styles["BulletTight"], bulletText="•"))
        continue
    m = re.match(r"^(\d+)\.\s+(.*)$", line)
    if m:
        story.append(Paragraph(inline_md(m.group(2)), styles["BulletTight"], bulletText=f"{m.group(1)}."))
        continue
    story.append(Paragraph(inline_md(line), styles["BodyTight"]))


doc = SimpleDocTemplate(
    str(out),
    pagesize=A4,
    rightMargin=18 * mm,
    leftMargin=18 * mm,
    topMargin=18 * mm,
    bottomMargin=16 * mm,
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(out)
