# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>
from typing import List
from app.models.invoice import Product, InvoiceResponse, AppliedTax


def generate_invoice(tipo: str, detalles: List[Product]) -> InvoiceResponse:
    # Calcular el subtotal
    subtotal = sum(item.quantity * item.unit_price for item in detalles)

    # Determinar el IVA y el total según el tipo de factura
    if tipo == "A":
        iva_porcentaje = 21
        iva_monto = subtotal * (iva_porcentaje / 100)
    elif tipo == "B":
        iva_porcentaje = 10.5
        iva_monto = subtotal * (iva_porcentaje / 100)
    elif tipo == "C":
        iva_porcentaje = 0
        iva_monto = 0

    # Calcular el total
    total = subtotal + iva_monto

    # Crear la respuesta de la factura
    factura_resumen = InvoiceResponse(
        type=tipo,
        subtotal=subtotal,
        applied_tax=AppliedTax(percentage=iva_porcentaje, amount=iva_monto),
        total=total,
        details=detalles,
    )

    return factura_resumen
