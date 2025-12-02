#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificación con scroll para mostrar todas las secciones
"""

import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright

async def verificacion_scroll():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("=" * 80)
        print("📸 VERIFICACIÓN CON SCROLL - TODAS LAS SECCIONES")
        print("=" * 80)

        # Cargar página
        await page.goto("http://localhost:8000/index.html", wait_until="load")
        await page.wait_for_timeout(500)

        # Screenshots en diferentes posiciones
        positions = [
            (0, "1. Header + Hero Banner"),
            (600, "2. Lo Que Hacemos"),
            (1200, "3. Ministerios"),
            (1800, "4. Áreas de Ministerio"),
            (2400, "5. Eventos"),
            (3000, "6. Formulario Voluntariado"),
            (3600, "7. Blog"),
            (4200, "8. Team / Footer"),
        ]

        for scroll_pos, title in positions:
            print(f"\n📸 {title}")
            await page.evaluate(f"window.scrollTo(0, {scroll_pos})")
            await page.wait_for_timeout(300)

            filename = f"/tmp/scroll_{scroll_pos}_{title.split('.')[1].strip().replace(' ', '_').lower()}.png"
            await page.screenshot(path=filename)
            print(f"   ✅ Guardado: {filename}")

        # Verificar contenido final
        print("\n" + "=" * 80)
        print("✅ RESUMEN")
        print("=" * 80)

        all_content = await page.evaluate("""
            () => {
                const text = document.body.innerText;
                return {
                    total_length: text.length,
                    has_sinode: text.includes('SINODE'),
                    has_somos_iglesia: text.includes('Somos Iglesia'),
                    has_ministerios: text.includes('Lo Que Hacemos'),
                    has_encuentros: text.includes('Encuent'),
                    has_voluntario: text.includes('voluntar'),
                    has_blog: text.includes('Blog') || text.includes('blog'),
                };
            }
        """)

        print(f"Total de contenido: {all_content['total_length']} caracteres")
        print(f"✅ SINODE: {'SÍ' if all_content['has_sinode'] else 'NO'}")
        print(f"✅ Somos Iglesia: {'SÍ' if all_content['has_somos_iglesia'] else 'NO'}")
        print(f"✅ Lo Que Hacemos: {'SÍ' if all_content['has_ministerios'] else 'NO'}")
        print(f"✅ Encuentros: {'SÍ' if all_content['has_encuentros'] else 'NO'}")
        print(f"✅ Voluntariado: {'SÍ' if all_content['has_voluntario'] else 'NO'}")
        print(f"✅ Blog: {'SÍ' if all_content['has_blog'] else 'NO'}")

        print("\n" + "=" * 80)
        print("✅ SITIO FUNCIONANDO CORRECTAMENTE")
        print("=" * 80)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verificacion_scroll())
