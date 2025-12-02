#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificación final del sitio SINODE reestructurado
"""

import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright

async def verificar_sitio():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("=" * 80)
        print("VERIFICACION FINAL - SINODE.ORG REESTRUCTURADO")
        print("=" * 80)

        # Cargar
        print("\n1. Cargando sitio...")
        await page.goto("http://localhost:8000/index.html", wait_until="load")
        await page.wait_for_timeout(1000)

        # Screenshots de secciones principales
        sections = [
            (0, "01_header_hero"),
            (700, "02_somos_iglesia"),
            (1200, "03_no_somos"),
            (1800, "04_fundamentos"),
            (2400, "05_comunidad"),
            (3000, "06_edificando_juntos"),
            (3600, "07_cta_doctrina"),
            (4200, "08_eventos"),
            (5500, "09_footer"),
        ]

        print("\n2. Tomando screenshots de todas las secciones...")
        for scroll_pos, name in sections:
            await page.evaluate(f"window.scrollTo(0, {scroll_pos})")
            await page.wait_for_timeout(300)
            await page.screenshot(path=f"/tmp/{name}.png")
            print(f"   - {name}.png")

        # Verificar contenido clave
        print("\n3. Verificando contenido...")
        content = await page.evaluate("() => document.body.innerText")

        checks = {
            "Menu Fundamentos": "Fundamentos" in content,
            "Menu Comunidad": "Comunidad" in content,
            "Menu Participa": "Participa" in content,
            "Somos Iglesia": "Somos... Iglesia" in content or "Somos Iglesia" in content,
            "No Somos": "No Somos" in content,
            "Versiculo Mateo 16:18": "Mateo 16:18" in content,
            "Versiculo Efesios": "Efesios" in content,
            "Versiculo 1 Corintios": "Corintios" in content,
            "Versiculo Hechos": "Hechos 2:42" in content,
            "CTA Profundizar": "Profundizar" in content,
            "Doctrina.SINODE.org": "doctrina.sinode.org" in content.lower(),
            "Footer SINODE": "Somos Iglesia, No Denominaciones" in content,
        }

        print("\n   Contenido encontrado:")
        for item, found in checks.items():
            status = "[OK]" if found else "[X]"
            print(f"   {status} {item}")

        passed = sum(1 for v in checks.values() if v)
        total = len(checks)

        print(f"\n   TOTAL: {passed}/{total} verificaciones pasadas")

        # Screenshot final completo
        print("\n4. Screenshot de pagina completa...")
        await page.screenshot(path="/tmp/sinode_completo.png", full_page=True)
        print("   - sinode_completo.png (pagina completa)")

        print("\n" + "=" * 80)
        if passed == total:
            print("SITIO VERIFICADO CORRECTAMENTE")
        else:
            print(f"ADVERTENCIA: {total - passed} verificaciones fallaron")
        print("=" * 80)

        await page.wait_for_timeout(5000)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verificar_sitio())
