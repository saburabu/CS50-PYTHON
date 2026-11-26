from pathlib import Path
from datetime import datetime, timedelta
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

# Standard CR80 ID Card Size (3.375 in x 2.125 in)
CARD_WIDTH = 3.375 * inch
CARD_HEIGHT = 2.125 * inch

BASE_DIR = Path(__file__).resolve().parent
CARDS_DIR = BASE_DIR / "cards"
CARDS_DIR.mkdir(exist_ok=True)


def _draw_base_card(c: canvas.Canvas, role_label: str, accent_color: colors.Color):
    # Dark slate background
    c.setFillColor(colors.HexColor("#12161F"))
    c.rect(0, 0, CARD_WIDTH, CARD_HEIGHT, fill=1, stroke=0)

    # Top accent bar
    c.setFillColor(accent_color)
    c.rect(0, CARD_HEIGHT - 0.36 * inch, CARD_WIDTH, 0.36 * inch, fill=1, stroke=0)

    # Gym Name
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.18 * inch, CARD_HEIGHT - 0.24 * inch, "FITNESS SABUR GYM")

    # Role Badge (MEMBER / TRAINER)
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(CARD_WIDTH - 0.18 * inch, CARD_HEIGHT - 0.23 * inch, role_label)

    # Bottom footer strip
    c.setFillColor(colors.HexColor("#1E2433"))
    c.rect(0, 0, CARD_WIDTH, 0.24 * inch, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#9CA3AF"))
    c.setFont("Helvetica", 6.5)
    c.drawString(0.18 * inch, 0.08 * inch, "LAGOS, NIGERIA  |  OFFICIAL ACCESS PASS")


def generate_member_card_pdf(member) -> Path:
    file_path = CARDS_DIR / f"{member.membership_id}_card.pdf"
    c = canvas.Canvas(str(file_path), pagesize=(CARD_WIDTH, CARD_HEIGHT))

    accent = colors.HexColor("#EAB308")  # Gold accent for Members
    _draw_base_card(c, "MEMBER PASS", accent)

    # Member ID Highlight
    c.setFillColor(accent)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.18 * inch, 1.42 * inch, member.membership_id)

    # Full Name
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.18 * inch, 1.20 * inch, member.full_name.upper())

    # Details
    c.setFillColor(colors.HexColor("#D1D5DB"))
    c.setFont("Helvetica", 8)
    c.drawString(0.18 * inch, 0.96 * inch, f"Program: {member.program}")
    c.drawString(0.18 * inch, 0.78 * inch, f"Gender / Age: {member.gender} / {member.age} yrs")

    # Plan Validity Dates
    start = datetime.strptime(member.start_date, "%Y-%m-%d").date()
    expiry = (start + timedelta(days=7)).strftime("%Y-%m-%d")
    status = "ACTIVE" if member.is_plan_active() else "EXPIRED"

    c.drawString(0.18 * inch, 0.56 * inch, f"Valid: {member.start_date}  to  {expiry}")

    # Status Pill
    status_color = colors.HexColor("#22C55E") if status == "ACTIVE" else colors.HexColor("#EF4444")
    c.setFillColor(status_color)
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(CARD_WIDTH - 0.18 * inch, 0.56 * inch, f"[{status}]")

    c.save()
    return file_path


def generate_trainer_card_pdf(trainer) -> Path:
    file_path = CARDS_DIR / f"{trainer.trainer_id}_card.pdf"
    c = canvas.Canvas(str(file_path), pagesize=(CARD_WIDTH, CARD_HEIGHT))

    accent = colors.HexColor("#0EA5E9")  # Electric Blue accent for Trainers
    _draw_base_card(c, "CERTIFIED TRAINER", accent)

    # Trainer ID Highlight
    c.setFillColor(accent)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.18 * inch, 1.42 * inch, trainer.trainer_id)

    # Full Name
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(0.18 * inch, 1.20 * inch, trainer.full_name.upper())

    # Details (Hides bank account & salary for security)
    c.setFillColor(colors.HexColor("#D1D5DB"))
    c.setFont("Helvetica", 8)
    c.drawString(0.18 * inch, 0.96 * inch, f"Specialty: {trainer.specialty}")
    c.drawString(0.18 * inch, 0.78 * inch, f"Phone: {trainer.phone_number}")
    c.drawString(0.18 * inch, 0.56 * inch, f"Joined: {trainer.reg_date}")

    # Availability Pill
    avail_text = "AVAILABLE" if trainer.is_available else "UNAVAILABLE"
    avail_color = colors.HexColor("#22C55E") if trainer.is_available else colors.HexColor("#F59E0B")
    c.setFillColor(avail_color)
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(CARD_WIDTH - 0.18 * inch, 0.56 * inch, f"[{avail_text}]")

    c.save()
    return file_path