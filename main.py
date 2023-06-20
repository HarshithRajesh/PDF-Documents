from fpdf import FPDF

pdf = FPDF(orientation='P',unit='pt',format='A4')
pdf.add_page()
pdf.set_font(family='Times', style='B',size=36)
pdf.cell(w=0,h=15,txt="AI FUTURE",align='C',ln=2)
pdf.image('ai.jpg',w=200,h=180,x=50,y=50)
pdf.set_font(family='Times',style='B',size=24)

pdf.cell(w=10,h=400,txt="AI is gonna change the future")


pdf.output('first_pdf.pdf')