python
from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import datetime

class PDFLabel:
    def generate(self, patient_name, medications, output_path='label.pdf'):
        c = canvas.Canvas(output_path, pagesize=A6)
        width, height = A6
        
        c.setFont("Helvetica-Bold", 16)
        c.drawString(10*mm, height-15*mm, "Pharmacy Label")
        
        c.setFont("Helvetica", 12)
        c.drawString(10*mm, height-30*mm, f"Patient: {patient_name}")
        c.drawString(10*mm, height-40*mm, f"Date: {datetime.date.today()}")
        
        c.setFont("Helvetica-Bold", 11)
        c.drawString(10*mm, height-55*mm, "Medications:")
        
        y = height-70*mm
        c.setFont("Helvetica", 10)
        for i, med in enumerate(medications[:5]):
            name = med['info'].get('name_fa', med['info'].get('name', 'Unknown'))
            c.drawString(15*mm, y, f"{i+1}. {name}")
            y -= 7*mm
        
        c.save()
        return output_path
