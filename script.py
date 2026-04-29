import os
import random
from fpdf import FPDF
from datetime import datetime, date

# Configuración
FOLDER_NAME = "dataset_facturas_2025"
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

clientes = ["Tech Solutions", "Logística Global", "Tienda Don Pepe", "Inversiones ABC", "Servicios Express"]
productos = [
    ("Laptop Pro", 1200.00), ("Mouse Ergonómico", 25.50), ("Monitor 24p", 180.00),
    ("Teclado Mecánico", 75.00), ("Cable HDMI 2m", 12.99), ("Soporte Laptop", 45.00)
]

def generar_fecha_real_2025():
    """Genera una fecha válida considerando la duración real de cada mes."""
    mes = random.randint(1, 12)
    # 2025 no es bisiesto, así que febrero tiene 28 días
    if mes == 2:
        dia = random.randint(1, 28)
    elif mes in [4, 6, 9, 11]:
        dia = random.randint(1, 30)
    else:
        dia = random.randint(1, 31)
    
    fecha_valida = date(2025, mes, dia)
    return fecha_valida.strftime("%d/%m/%Y")

def generar_factura(id_factura):
    pdf = FPDF()
    pdf.add_page()
    
    # Encabezado y Estilo
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(190, 10, txt="FACTURA DE VENTA - 2025", ln=True, align='C')
    pdf.ln(10)

    # Datos de la Factura
    pdf.set_font("helvetica", "", 11)
    cliente = random.choice(clientes)
    fecha_str = generar_fecha_real_2025()
    
    pdf.cell(100, 10, txt=f"Cliente: {cliente}")
    pdf.cell(90, 10, txt=f"Factura N°: F25-{id_factura:04d}", ln=True, align='R')
    pdf.cell(100, 10, txt=f"Fecha de Emisión: {fecha_str}", ln=True)
    pdf.ln(10)

    # Tabla
    pdf.set_font("helvetica", "B", 11)
    pdf.cell(100, 10, "Descripción", border=1)
    pdf.cell(40, 10, "Cant.", border=1, align='C')
    pdf.cell(50, 10, "Total ($)", border=1, align='C', ln=True)

    pdf.set_font("helvetica", "", 11)
    subtotal = 0
    for _ in range(random.randint(1, 5)):
        prod, precio = random.choice(productos)
        cant = random.randint(1, 10)
        total_linea = precio * cant
        subtotal += total_linea
        pdf.cell(100, 10, prod, border=1)
        pdf.cell(40, 10, str(cant), border=1, align='C')
        pdf.cell(50, 10, f"{total_linea:.2f}", border=1, align='C', ln=True)

    # Totales
    iva = subtotal * 0.19
    total_final = subtotal + iva

    pdf.ln(5)
    pdf.set_font("helvetica", "B", 11)
    pdf.cell(140, 10, "Subtotal:", align='R')
    pdf.cell(50, 10, f"{subtotal:.2f}", align='C', ln=True)
    pdf.cell(140, 10, "IVA (19%):", align='R')
    pdf.cell(50, 10, f"{iva:.2f}", align='C', ln=True)
    pdf.cell(140, 10, "TOTAL:", align='R')
    pdf.cell(50, 10, f"{total_final:.2f}", align='C', ln=True)

    # Guardar
    file_path = os.path.join(FOLDER_NAME, f"factura_2025_{id_factura:04d}.pdf")
    pdf.output(file_path)

# Ejecución
CANTIDAD = 1000 
print(f"Generando {CANTIDAD} facturas para el año fiscal 2025...")
for i in range(1, CANTIDAD + 1):
    generar_factura(i)
print(f"¡Listo! Tienes 12 meses de datos en la carpeta '{FOLDER_NAME}'.")