#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Explorar estructura completa de doctrina.sinode.org
"""

import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright

async def explore_doctrina():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("=" * 80)
        print("🔍 EXPLORANDO ESTRUCTURA DE doctrina.sinode.org")
        print("=" * 80)

        try:
            # Cargar sitio
            print("\n1️⃣ Accediendo a https://doctrina.sinode.org...")
            response = await page.goto("https://doctrina.sinode.org", wait_until="networkidle", timeout=10000)
            print(f"   Status: {response.status if response else 'N/A'}")
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:100]}")
            # Continuar de todas formas

        await page.wait_for_timeout(2000)

        # Extraer estructura
        print("\n2️⃣ Extrayendo estructura de navegación...")
        structure = await page.evaluate("""
            () => {
                const result = {
                    title: document.title,
                    url: window.location.href,
                    meta_description: document.querySelector('meta[name="description"]')?.content || 'N/A',

                    // Navbars
                    navbars: Array.from(document.querySelectorAll('nav, [role="navigation"], .navbar')).map(n => ({
                        class: n.className,
                        text: n.innerText.substring(0, 100)
                    })),

                    // Links principales
                    links: Array.from(document.querySelectorAll('a[href]')).map(a => ({
                        text: a.innerText.trim(),
                        href: a.href,
                        visible: a.offsetHeight > 0
                    })).filter(l => l.text.length > 0 && l.visible).slice(0, 50),

                    // Menús
                    menus: Array.from(document.querySelectorAll('menu, [role="menu"], .menu, ul.nav, .sidebar')).map(m => ({
                        class: m.className,
                        items: Array.from(m.querySelectorAll('li, a')).slice(0, 20).map(item => item.innerText.trim())
                    })),

                    // Headings (estructura de contenido)
                    headings: Array.from(document.querySelectorAll('h1, h2, h3, h4')).map(h => ({
                        level: h.tagName,
                        text: h.innerText.trim()
                    })).slice(0, 30),

                    // Sections
                    sections: Array.from(document.querySelectorAll('section, [role="region"], .section, [class*="section"]')).map(s => ({
                        class: s.className,
                        text: s.innerText.substring(0, 150)
                    })).slice(0, 20)
                };
                return result;
            }
        """)

        print(f"\n📄 Página: {structure['title']}")
        print(f"URL: {structure['url']}")
        print(f"Meta Description: {structure['meta_description']}")

        print("\n🔗 LINKS ENCONTRADOS:")
        if structure['links']:
            for i, link in enumerate(structure['links'][:30], 1):
                href = link['href'].replace('https://doctrina.sinode.org', '').replace('https://sinode.org', '')
                print(f"   {i:2d}. {link['text'][:40]:40s} → {href[:50]}")
        else:
            print("   (No se encontraron links)")

        print("\n📋 HEADINGS (Estructura de contenido):")
        if structure['headings']:
            for heading in structure['headings'][:20]:
                indent = "   " * (int(heading['level'][-1]) - 1)
                print(f"{indent}{heading['level']}: {heading['text'][:60]}")
        else:
            print("   (No se encontraron headings)")

        print("\n📦 MENÚS:")
        if structure['menus']:
            for i, menu in enumerate(structure['menus'][:5], 1):
                print(f"   Menú {i} ({menu['class'][:40]}):")
                for item in menu['items'][:10]:
                    if item:
                        print(f"      - {item[:60]}")
        else:
            print("   (No se encontraron menús estructurados)")

        print("\n🏢 SECCIONES:")
        if structure['sections']:
            for i, section in enumerate(structure['sections'][:10], 1):
                print(f"   {i}. {section['class'][:50]}")
                preview = section['text'].replace('\n', ' ')[:80]
                print(f"      → {preview}")
        else:
            print("   (No se encontraron secciones)")

        # Tomar screenshot
        print("\n3️⃣ Tomando screenshot...")
        await page.screenshot(path="/tmp/doctrina_sinode_org.png")
        print("   ✅ Screenshot: /tmp/doctrina_sinode_org.png")

        # Obtener todo el HTML para análisis
        print("\n4️⃣ Extrayendo HTML completo...")
        html_content = await page.content()
        print(f"   HTML size: {len(html_content)} bytes")

        # Guardar HTML para análisis
        with open("C:\\workspace\\CLAUDE\\template-injection-demo\\doctrina_sinode_html.txt", "w", encoding="utf-8") as f:
            f.write(html_content[:10000])  # Primeros 10KB
        print("   ✅ HTML guardado: doctrina_sinode_html.txt")

        print("\n" + "=" * 80)
        print("✅ EXPLORACIÓN COMPLETADA")
        print("=" * 80)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(explore_doctrina())
