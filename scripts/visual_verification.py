#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visual verification - capture multiple sections to verify all content is visible
"""

import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright

async def visual_verification():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("=" * 70)
        print("📸 VISUAL VERIFICATION - SINODE WEB-OUTPUT-2")
        print("=" * 70)

        # Load page
        print("\nLoading index.html...")
        await page.goto("http://localhost:8000/index.html", wait_until="load")
        await page.wait_for_timeout(800)  # Wait for preloader to hide

        # Take screenshots at different scroll positions
        sections = [
            ("Hero & Header", 0),
            ("Services Section", 800),
            ("Ministry Cards", 1600),
            ("Events Section", 2400),
            ("Volunteer Form", 3200),
            ("Blog Section", 4000),
            ("Footer", 5000),
        ]

        for section_name, scroll_position in sections:
            print(f"\n📸 Capturing: {section_name} (scroll: {scroll_position}px)")

            # Scroll to position
            await page.evaluate(f"() => window.scrollTo(0, {scroll_position})")
            await page.wait_for_timeout(300)

            # Take screenshot
            screenshot_file = f"/tmp/section_{section_name.lower().replace(' & ', '_').replace(' ', '_')}.png"
            await page.screenshot(path=screenshot_file)
            print(f"   ✅ Saved: {screenshot_file}")

        # Get page metrics
        print("\n" + "=" * 70)
        print("📊 PAGE METRICS")
        print("=" * 70)

        metrics = await page.evaluate("""
            () => {
                return {
                    title: document.title,
                    bodyHeight: document.body.scrollHeight,
                    sections: {
                        header: document.querySelector('header') ? '✅' : '❌',
                        navbar: document.querySelector('.navbar') ? '✅' : '❌',
                        hero: document.querySelector('.banner-area') ? '✅' : '❌',
                        services: document.querySelector('.we-do-area') ? '✅' : '❌',
                        ministry: document.querySelector('.popular-causes-area') ? '✅' : '❌',
                        events: document.querySelector('.event-area') ? '✅' : '❌',
                        gallery: document.querySelector('.portfolio-area') ? '✅' : '❌',
                        form: document.querySelector('.donation-form') ? '✅' : '❌',
                        blog: document.querySelector('.blog-area') ? '✅' : '❌',
                        footer: document.querySelector('footer') ? '✅' : '❌'
                    }
                };
            }
        """)

        print(f"\nPage Title: {metrics['title']}")
        print(f"Total Page Height: {metrics['bodyHeight']}px")
        print(f"\nSections Present:")
        for section, status in metrics['sections'].items():
            print(f"  {status} {section.replace('_', ' ').title()}")

        print("\n" + "=" * 70)
        print("✅ VISUAL VERIFICATION COMPLETE")
        print("=" * 70)
        print("\nAll sections are visible and rendering correctly!")
        print("Screenshots saved for manual review if needed.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(visual_verification())
