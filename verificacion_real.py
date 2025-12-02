#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificación REAL del contenido visible - con navegador abierto
"""

import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright

async def verificacion_real():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=False para VER
        page = await browser.new_page()

        print("=" * 80)
        print("🔍 VERIFICACIÓN REAL CON NAVEGADOR VISIBLE")
        print("=" * 80)
        print("\n⏳ Abriendo navegador... (mira la ventana del navegador)")
        print("El navegador se abrirá en pocos segundos...\n")

        # Cargar página
        print("1️⃣ Cargando http://localhost:8000/index.html...")
        await page.goto("http://localhost:8000/index.html", wait_until="domcontentloaded")
        print("   ✅ Página cargada")

        # Esperar y ver qué pasa
        print("\n2️⃣ Esperando 1 segundo...")
        await page.wait_for_timeout(1000)

        # Obtener el contenido visible
        print("\n3️⃣ Obteniendo contenido VISIBLE en la pantalla...")
        visible_content = await page.evaluate("""
            () => {
                // Obtener TODO lo que es visible
                const body = document.body;
                const allText = body.innerText;

                // Obtener elementos específicos
                const topbar = document.querySelector('.top-bar-area');
                const navbar = document.querySelector('.navbar');
                const banner = document.querySelector('.banner-area');
                const preloader = document.querySelector('.se-pre-con');

                return {
                    preloaderExists: preloader ? true : false,
                    preloaderDisplay: preloader ? window.getComputedStyle(preloader).display : 'N/A',
                    preloaderOpacity: preloader ? window.getComputedStyle(preloader).opacity : 'N/A',
                    topbarExists: topbar ? true : false,
                    navbarExists: navbar ? true : false,
                    bannerExists: banner ? true : false,
                    bodyText: allText.substring(0, 500),  // Primeros 500 caracteres
                    totalTextLength: allText.length
                };
            }
        """)

        print(f"\n📊 Estado del Preloader:")
        print(f"   Existe en DOM: {visible_content['preloaderExists']}")
        print(f"   Display CSS: {visible_content['preloaderDisplay']}")
        print(f"   Opacity: {visible_content['preloaderOpacity']}")

        print(f"\n📊 Elementos Principales:")
        print(f"   Top Bar existe: {visible_content['topbarExists']}")
        print(f"   Navbar existe: {visible_content['navbarExists']}")
        print(f"   Banner existe: {visible_content['bannerExists']}")

        print(f"\n📊 Contenido Visible:")
        print(f"   Longitud total del texto: {visible_content['totalTextLength']} caracteres")
        print(f"   Primeros 500 caracteres:")
        print(f"   {visible_content['bodyText']}")

        # Verificar si SINODE está presente
        print("\n4️⃣ Buscando contenido SINODE específico...")
        sinode_search = await page.evaluate("""
            () => {
                const text = document.body.innerText;
                return {
                    sinode: text.includes('SINODE'),
                    somos_iglesia: text.includes('Somos Iglesia'),
                    lo_que_hacemos: text.includes('Lo Que Hacemos'),
                    areas_ministerio: text.includes('Áreas de Ministerio'),
                    encuentros: text.includes('Encuentros'),
                    voluntariado: text.includes('Voluntar'),
                    blog: text.includes('Blog') || text.includes('blog'),
                    footer: text.includes('Copyright') || text.includes('Footer')
                };
            }
        """)

        print("\n✅ SINODE:", "SÍ" if sinode_search['sinode'] else "NO")
        print("✅ Somos Iglesia:", "SÍ" if sinode_search['somos_iglesia'] else "NO")
        print("✅ Lo Que Hacemos:", "SÍ" if sinode_search['lo_que_hacemos'] else "NO")
        print("✅ Áreas de Ministerio:", "SÍ" if sinode_search['areas_ministerio'] else "NO")
        print("✅ Encuentros:", "SÍ" if sinode_search['encuentros'] else "NO")
        print("✅ Voluntariado:", "SÍ" if sinode_search['voluntariado'] else "NO")
        print("✅ Blog:", "SÍ" if sinode_search['blog'] else "NO")
        print("✅ Footer:", "SÍ" if sinode_search['footer'] else "NO")

        # Esperar para que vea el navegador
        print("\n" + "=" * 80)
        print("👀 Mira la ventana del navegador abierta a la izquierda")
        print("El navegador permanecerá abierto por 10 segundos para que verifiques")
        print("=" * 80)

        await page.wait_for_timeout(10000)

        # Tomar screenshot final
        print("\n5️⃣ Tomando screenshot final...")
        await page.screenshot(path="/tmp/verificacion_real_final.png")
        print("   ✅ Screenshot guardado: /tmp/verificacion_real_final.png")

        await browser.close()
        print("\n✅ Verificación completada")

if __name__ == "__main__":
    asyncio.run(verificacion_real())
