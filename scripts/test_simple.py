#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright

async def test_simple():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=False para VER el navegador
        page = await browser.new_page()

        # Ir a test_simple.html
        await page.goto("http://localhost:8000/test_simple.html", wait_until="networkidle")

        # Esperar un poco para que todo cargue
        await page.wait_for_timeout(3000)

        # Obtener contenido visible
        print("\n=== CONTENIDO VISIBLE ===")
        body_text = await page.evaluate("() => document.body.innerText")
        print(body_text[:1000])

        # Verificar elementos específicos
        print("\n=== VERIFICACIÓN DE ELEMENTOS ===")

        # Logo
        logo = await page.query_selector("img[src*='logo']")
        print(f"Logo: {'VISIBLE' if logo else 'OCULTO'}")

        # Botones Bootstrap
        buttons = await page.query_selector_all("button.btn")
        print(f"Botones Bootstrap: {len(buttons)} encontrados")

        # Grid columns
        cols = await page.query_selector_all("[class*='col-']")
        print(f"Columnas Bootstrap: {len(cols)} encontradas")

        # Verificar si Bootstrap está cargando CSS
        print("\n=== DIAGNÓSTICO CSS ===")
        css_check = await page.evaluate("""
            () => {
                const btn = document.querySelector('button.btn');
                if (btn) {
                    const style = window.getComputedStyle(btn);
                    return {
                        backgroundColor: style.backgroundColor,
                        color: style.color,
                        padding: style.padding,
                        borderRadius: style.borderRadius
                    };
                }
                return { error: 'No button found' };
            }
        """)
        print("Estilos del botón:", css_check)

        # Tomar screenshot
        await page.screenshot(path="/tmp/test_simple_screenshot.png")
        print("\nScreenshot tomado: /tmp/test_simple_screenshot.png")

        await browser.close()

asyncio.run(test_simple())
