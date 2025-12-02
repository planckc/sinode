#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analizar todas las secciones de doctrina.sinode.org para mapear contenido
"""

import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright

async def explore_sections():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("=" * 100)
        print("📚 MAPEANDO TODAS LAS SECCIONES DE doctrina.sinode.org")
        print("=" * 100)

        # Secciones a explorar
        sections = {
            "Bases Doctrinales": "/es/bases-doctrinales",
            "Discernimiento": "/es/discernimiento",
            "Biblioteca": "/es/old-biblioteca",
            "Comunidad": "/es/iglesia-operativa",
            "Territorios": "/es/territorios",
            "Proyectos": "/es/proyectos",
            "Voluntariado": "/es/ser-voluntario",
            "Sobre SINODE": "/es/sobre-unisolid",
            "Testimonios": "/es/testimonios",
            "Doctrinas Comentadas": "/es/creencias/doctrinas",
        }

        all_content = {}

        for section_name, url_path in sections.items():
            print(f"\n{'='*100}")
            print(f"📖 SECCIÓN: {section_name}")
            print(f"{'='*100}")

            try:
                full_url = f"https://doctrina.sinode.org{url_path}"
                print(f"Accediendo a: {full_url}")

                response = await page.goto(full_url, wait_until="networkidle", timeout=15000)
                status = response.status if response else "N/A"
                print(f"Status: {status}")

                await page.wait_for_timeout(1000)

                # Extraer contenido
                content_data = await page.evaluate("""
                    () => {
                        const title = document.querySelector('h1')?.innerText || 'N/A';
                        const description = document.querySelector('[class*="description"], [class*="intro"], p')?.innerText || '';
                        const paragraphs = Array.from(document.querySelectorAll('p')).map(p => p.innerText.trim()).filter(p => p.length > 20).slice(0, 3);
                        const sections = Array.from(document.querySelectorAll('h2, h3')).map(h => h.innerText).slice(0, 10);
                        const lists = Array.from(document.querySelectorAll('ul, ol')).map(l => ({
                            items: Array.from(l.querySelectorAll('li')).map(li => li.innerText.trim()).slice(0, 5)
                        })).filter(l => l.items.length > 0).slice(0, 3);

                        return {
                            title,
                            description: description.substring(0, 200),
                            paragraphs,
                            sections,
                            lists,
                            bodyText: document.body.innerText.length
                        };
                    }
                """)

                print(f"\n✅ TÍTULO: {content_data['title']}")
                print(f"\n📝 DESCRIPCIÓN: {content_data['description'][:100]}...")

                if content_data['sections']:
                    print(f"\n🏗️ SUBSECCIONES:")
                    for sec in content_data['sections'][:8]:
                        print(f"   • {sec}")

                if content_data['lists']:
                    print(f"\n📋 LISTAS/ITEMS:")
                    for list_item in content_data['lists']:
                        for item in list_item['items'][:3]:
                            print(f"   • {item[:70]}")

                print(f"\n📊 Contenido total: {content_data['bodyText']} caracteres")

                all_content[section_name] = {
                    'url': url_path,
                    'title': content_data['title'],
                    'description': content_data['description'],
                    'subsections': content_data['sections'],
                    'items': content_data['lists']
                }

            except Exception as e:
                print(f"❌ Error: {str(e)[:100]}")

        print("\n" + "=" * 100)
        print("📊 RESUMEN DE CONTENIDO")
        print("=" * 100)

        # Crear resumen estructurado
        print("\n🎯 ESTRUCTURA PARA WEB-OUTPUT-2:\n")

        structure = {
            "FUNDAMENTOS": [
                {"nombre": "Bases Doctrinales", "url": "/es/bases-doctrinales", "emoji": "📖", "descripcion": "Los principios fundamentales de SINODE"},
                {"nombre": "Discernimiento", "url": "/es/discernimiento", "emoji": "🧠", "descripcion": "Cómo tomamos decisiones como iglesia"},
                {"nombre": "Doctrinas Comentadas", "url": "/es/creencias/doctrinas", "emoji": "💭", "descripcion": "Doctrinas explicadas en profundidad"},
            ],
            "COMUNIDAD": [
                {"nombre": "Iglesia Operativa", "url": "/es/iglesia-operativa", "emoji": "🏢", "descripcion": "Cómo funcionamos como comunidad"},
                {"nombre": "Territorios", "url": "/es/territorios", "emoji": "🌍", "descripcion": "SINODE en diferentes regiones"},
                {"nombre": "Testimonios", "url": "/es/testimonios", "emoji": "💬", "descripcion": "Historias de miembros de SINODE"},
            ],
            "ACCIÓN": [
                {"nombre": "Proyectos", "url": "/es/proyectos", "emoji": "🛠️", "descripcion": "Iniciativas y proyectos activos"},
                {"nombre": "Biblioteca", "url": "/es/old-biblioteca", "emoji": "📚", "descripcion": "Recursos digitales para aprender"},
                {"nombre": "Voluntariado", "url": "/es/ser-voluntario", "emoji": "🤝", "descripcion": "Cómo participar activamente"},
            ]
        }

        for grupo, items in structure.items():
            print(f"\n{grupo}:")
            for item in items:
                print(f"  {item['emoji']} {item['nombre']}")
                print(f"     → {item['descripcion']}")
                print(f"     🔗 {item['url']}")

        # Guardar análisis
        import json
        with open("C:\\workspace\\CLAUDE\\template-injection-demo\\content_mapping.json", "w", encoding="utf-8") as f:
            json.dump({
                "raw_content": all_content,
                "suggested_structure": structure
            }, f, indent=2, ensure_ascii=False)

        print("\n" + "=" * 100)
        print("✅ ANÁLISIS COMPLETADO - content_mapping.json guardado")
        print("=" * 100)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(explore_sections())
