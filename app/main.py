# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano <Github@alejo-code>

from fastapi import FastAPI
from app.routers.invoice_router import router as invoice_router

app = FastAPI()

# Incluir el router de facturación
app.include_router(invoice_router)
