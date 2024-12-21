# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

from fastapi import APIRouter, HTTPException
from app.models.invoice import InvoiceRequest, InvoiceResponse
from app.services.invoice_service import generate_invoice

router = APIRouter(tags=["Factura"])


@router.post("/invoice", response_model=InvoiceResponse)
async def create_invoice(invoice: InvoiceRequest):
    # Validar tipo de factura
    if invoice.type not in ["A", "B", "C"]:
        raise HTTPException(status_code=400, detail="Tipo de factura no válido")

    result = generate_invoice(invoice.type, invoice.details)

    return result
