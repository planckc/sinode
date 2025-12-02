#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for SINODE web-output-2 sitio
Diagnostica problemas de UX/UI y funcionalidad
"""

import asyncio
import sys
import os
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright
import json
from datetime import datetime

class SINODETester:
    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "tests": [],
            "issues": [],
            "screenshots": []
        }

    async def run_all_tests(self):
        """Ejecuta todas las pruebas"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            print("🔍 INICIANDO TESTS DE SINODE WEB-OUTPUT-2")
            print("=" * 60)

            try:
                # 1. Carga de página
                print("\n1️⃣ Probando carga de página...")
                await self.test_page_load(page)

                # 2. Verificar elementos críticos
                print("\n2️⃣ Verificando elementos críticos...")
                await self.test_critical_elements(page)

                # 3. Verificar secciones
                print("\n3️⃣ Verificando secciones SINODE...")
                await self.test_sinode_sections(page)

                # 4. Verificar CSS
                print("\n4️⃣ Verificando CSS y estilos...")
                await self.test_css_loading(page)

                # 5. Verificar JavaScript
                print("\n5️⃣ Verificando JavaScript...")
                await self.test_javascript(page)

                # 6. Verificar responsive
                print("\n6️⃣ Verificando responsive design...")
                await self.test_responsive(page)

                # 7. Consola errors
                print("\n7️⃣ Buscando errores en consola...")
                await self.test_console_errors(page)

                # 8. Performance
                print("\n8️⃣ Midiendo performance...")
                await self.test_performance(page)

                # 9. Screenshot
                print("\n9️⃣ Tomando screenshot...")
                await page.screenshot(path="/tmp/sinode_screenshot.png")
                self.results["screenshots"].append("/tmp/sinode_screenshot.png")

            finally:
                await browser.close()

            return self.results

    async def test_page_load(self, page):
        """Verifica que la página cargue correctamente"""
        try:
            response = await page.goto("http://localhost:8000", timeout=10000)
            status = response.status if response else "No response"
            print(f"   ✅ Página cargada - Status: {status}")
            self.results["tests"].append({
                "nombre": "Page Load",
                "status": "PASS",
                "detalle": f"Status code: {status}"
            })
            return True
        except Exception as e:
            print(f"   ❌ Error cargando página: {e}")
            self.results["issues"].append({
                "tipo": "CRÍTICO",
                "descripción": f"No se pudo cargar la página: {e}"
            })
            return False

    async def test_critical_elements(self, page):
        """Verifica que elementos críticos estén presentes"""
        try:
            # Check HTML
            html = await page.content()
            print(f"   📄 Tamaño HTML: {len(html)} bytes")

            # Elementos críticos
            critical_elements = {
                "Logo": 'img[src*="logo"]',
                "Hero Banner": '.banner-area',
                "Navigation": '.navbar',
                "Hero Title": '.hero-title, h1',
                "Services Section": '.we-do-area',
                "Ministerios Cards": '.popular-causes-area',
                "Events": '.event-area',
                "Gallery": '.portfolio-area, .gallery',
                "Blog": '.blog-area',
                "Footer": 'footer',
            }

            found = 0
            missing = []

            for name, selector in critical_elements.items():
                try:
                    element = await page.query_selector(selector)
                    if element:
                        found += 1
                        print(f"   ✅ {name}: ENCONTRADO")
                    else:
                        missing.append(name)
                        print(f"   ❌ {name}: FALTANTE")
                except:
                    missing.append(name)
                    print(f"   ⚠️ {name}: Error verificando")

            self.results["tests"].append({
                "nombre": "Critical Elements",
                "status": "PASS" if len(missing) == 0 else "WARNING",
                "encontrados": found,
                "faltantes": missing
            })

            if missing:
                self.results["issues"].append({
                    "tipo": "IMPORTANTE",
                    "descripción": f"Elementos faltantes: {', '.join(missing)}"
                })

        except Exception as e:
            print(f"   ❌ Error verificando elementos: {e}")
            self.results["issues"].append({
                "tipo": "ERROR",
                "descripción": f"Error en verificación de elementos: {e}"
            })

    async def test_sinode_sections(self, page):
        """Verifica contenido específico SINODE"""
        try:
            content_checks = {
                "Somos Iglesia": "Somos Iglesia",
                "Lo Que Hacemos": "Lo Que Hacemos",
                "Áreas de Ministerio": "Áreas de Ministerio",
                "Encuentros": "Encuentros",
                "Voluntariado": "Voluntaria",
                "Blog SINODE": "Discernimiento y Formación"
            }

            found_content = 0
            missing_content = []

            for label, text in content_checks.items():
                try:
                    # Buscar texto en la página
                    locator = page.locator(f"text={text}")
                    count = await locator.count()
                    if count > 0:
                        found_content += 1
                        print(f"   ✅ Contenido '{label}': ENCONTRADO ({count} instancias)")
                    else:
                        missing_content.append(label)
                        print(f"   ❌ Contenido '{label}': NO ENCONTRADO")
                except Exception as e:
                    print(f"   ⚠️ Contenido '{label}': Error ({str(e)[:50]})")
                    missing_content.append(label)

            self.results["tests"].append({
                "nombre": "SINODE Content",
                "status": "PASS" if len(missing_content) == 0 else "FAIL",
                "encontrado": found_content,
                "faltante": missing_content
            })

            if missing_content:
                self.results["issues"].append({
                    "tipo": "CRÍTICO",
                    "descripción": f"Contenido SINODE faltante: {', '.join(missing_content)}"
                })

        except Exception as e:
            print(f"   ❌ Error verificando contenido SINODE: {e}")

    async def test_css_loading(self, page):
        """Verifica que CSS se cargue correctamente"""
        try:
            # Obtener todos los stylesheets
            stylesheets = await page.evaluate("""
                () => {
                    return Array.from(document.styleSheets).map(sheet => ({
                        href: sheet.href || 'inline',
                        rules: sheet.cssRules ? sheet.cssRules.length : 0
                    }));
                }
            """)

            print(f"   📊 Stylesheets cargados: {len(stylesheets)}")
            for i, sheet in enumerate(stylesheets):
                print(f"      {i+1}. {sheet['href']} ({sheet['rules']} rules)")

            # Verificar que hay estilos
            computed_style = await page.evaluate("""
                () => {
                    const body = document.body;
                    const style = window.getComputedStyle(body);
                    return {
                        display: style.display,
                        backgroundColor: style.backgroundColor,
                        color: style.color
                    };
                }
            """)

            print(f"   🎨 Body styles: {computed_style}")

            if len(stylesheets) > 0:
                print(f"   ✅ CSS cargado correctamente")
                self.results["tests"].append({
                    "nombre": "CSS Loading",
                    "status": "PASS",
                    "detalle": f"{len(stylesheets)} stylesheets cargados"
                })
            else:
                print(f"   ❌ NO HAY CSS CARGADO")
                self.results["issues"].append({
                    "tipo": "CRÍTICO",
                    "descripción": "No se encontró CSS cargado - Los estilos no se están aplicando"
                })

        except Exception as e:
            print(f"   ❌ Error verificando CSS: {e}")
            self.results["issues"].append({
                "tipo": "ERROR",
                "descripción": f"Error verificando CSS: {e}"
            })

    async def test_javascript(self, page):
        """Verifica JavaScript y librerías"""
        try:
            js_info = await page.evaluate("""
                () => {
                    return {
                        jQuery: typeof jQuery !== 'undefined',
                        Bootstrap: typeof bootstrap !== 'undefined',
                        Owl: typeof $.fn.owlCarousel !== 'undefined',
                        Isotope: typeof Isotope !== 'undefined',
                        scripts: document.scripts.length,
                        errors: window.__errors || []
                    };
                }
            """)

            print(f"   📦 jQuery: {'✅' if js_info['jQuery'] else '❌'}")
            print(f"   📦 Bootstrap: {'✅' if js_info['Bootstrap'] else '❌'}")
            print(f"   📦 Owl Carousel: {'✅' if js_info['Owl'] else '❌'}")
            print(f"   📦 Isotope: {'✅' if js_info['Isotope'] else '❌'}")
            print(f"   📊 Scripts cargados: {js_info['scripts']}")

            status = "PASS" if (js_info['jQuery'] and js_info['Bootstrap']) else "WARNING"
            self.results["tests"].append({
                "nombre": "JavaScript",
                "status": status,
                "detalle": js_info
            })

        except Exception as e:
            print(f"   ❌ Error verificando JavaScript: {e}")

    async def test_responsive(self, page):
        """Verifica responsive design"""
        viewports = {
            "Mobile (375x667)": {"width": 375, "height": 667},
            "Tablet (768x1024)": {"width": 768, "height": 1024},
            "Desktop (1920x1080)": {"width": 1920, "height": 1080}
        }

        try:
            for name, viewport in viewports.items():
                await page.set_viewport_size(viewport)
                await page.wait_for_load_state("networkidle")

                # Verificar que el contenido es visible
                logo = await page.query_selector('img[src*="logo"]')
                if logo:
                    print(f"   ✅ {name}: VISIBLE")
                else:
                    print(f"   ❌ {name}: LOGO NO VISIBLE")

            self.results["tests"].append({
                "nombre": "Responsive Design",
                "status": "PASS",
                "viewports_testeados": list(viewports.keys())
            })

        except Exception as e:
            print(f"   ❌ Error en responsive: {e}")

    async def test_console_errors(self, page):
        """Captura errores de consola"""
        console_messages = []
        errors = []

        page.on("console", lambda msg: console_messages.append({
            "type": msg.type,
            "text": msg.text
        }))

        page.on("pageerror", lambda exc: errors.append(str(exc)))

        # Recargar para capturar errores
        await page.reload()
        await page.wait_for_load_state("networkidle")

        print(f"   📋 Mensajes console: {len(console_messages)}")
        print(f"   ⚠️ Errores JavaScript: {len(errors)}")

        if errors:
            print("   ERRORES ENCONTRADOS:")
            for error in errors[:5]:  # Primeros 5
                print(f"      • {error[:100]}")

            self.results["issues"].append({
                "tipo": "ERROR",
                "descripción": f"{len(errors)} errores JavaScript encontrados"
            })

        self.results["tests"].append({
            "nombre": "Console & Errors",
            "status": "PASS" if len(errors) == 0 else "WARNING",
            "errores": len(errors),
            "mensajes": len(console_messages)
        })

    async def test_performance(self, page):
        """Mide performance"""
        try:
            metrics = await page.evaluate("""
                () => {
                    const nav = window.performance.getEntriesByType('navigation')[0];
                    return {
                        loadTime: nav ? nav.loadEventEnd - nav.loadEventStart : 0,
                        domReady: nav ? nav.domContentLoadedEventEnd - nav.domContentLoadedEventStart : 0,
                        resources: window.performance.getEntriesByType('resource').length
                    };
                }
            """)

            print(f"   ⏱️ Load time: {metrics['loadTime']}ms")
            print(f"   ⏱️ DOM ready: {metrics['domReady']}ms")
            print(f"   📦 Recursos: {metrics['resources']}")

            self.results["tests"].append({
                "nombre": "Performance",
                "status": "PASS",
                "detalle": metrics
            })

        except Exception as e:
            print(f"   ⚠️ Error midiendo performance: {e}")

    def print_summary(self):
        """Imprime resumen de resultados"""
        print("\n" + "=" * 60)
        print("📊 RESUMEN DE TESTS")
        print("=" * 60)

        passed = sum(1 for t in self.results["tests"] if t["status"] == "PASS")
        total = len(self.results["tests"])

        print(f"\n✅ Tests pasados: {passed}/{total}")
        print(f"❌ Problemas encontrados: {len(self.results['issues'])}")

        if self.results["issues"]:
            print("\n🔴 ISSUES CRÍTICOS:")
            for issue in self.results["issues"]:
                print(f"  [{issue['tipo']}] {issue['descripción']}")

        print("\n" + "=" * 60)

        # Guardar resultados en JSON
        with open("/tmp/sinode_test_results.json", "w") as f:
            json.dump(self.results, f, indent=2)

        print("📄 Resultados guardados en: /tmp/sinode_test_results.json")

async def main():
    tester = SINODETester()
    await tester.run_all_tests()
    tester.print_summary()

if __name__ == "__main__":
    asyncio.run(main())
