# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

from pydantic import BaseModel
from typing import List


# Modelo para cada producto o servicio
class Product(BaseModel):
    product: str
    quantity: int
    unit_price: float


# Modelo para la solicitud de creación de factura
class InvoiceRequest(BaseModel):
    type: str
    details: List[Product]


# Modelo para la respuesta con resumen de la factura
class AppliedTax(BaseModel):
    percentage: float
    amount: float


class InvoiceResponse(BaseModel):
    type: str
    subtotal: float
    applied_tax: AppliedTax
    total: float
    details: List[Product]
