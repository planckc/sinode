#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diagnostic script to verify preloader issue and test fixes
"""

import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8') if sys.platform == 'win32' else None

from playwright.async_api import async_playwright
import json

async def diagnose_preloader():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("=" * 60)
        print("🔍 PRELOADER DIAGNOSTIC TEST")
        print("=" * 60)

        # Test 1: Load index.html and check preloader
        print("\n1️⃣ Loading index.html...")
        response = await page.goto("http://localhost:8000/index.html", wait_until="load")
        print(f"   Status: {response.status}")

        # Wait a moment for preloader animation
        await page.wait_for_timeout(500)

        # Check if preloader exists and its state
        print("\n2️⃣ Checking preloader state...")
        preloader_info = await page.evaluate("""
            () => {
                const preloader = document.querySelector('.se-pre-con');
                if (!preloader) {
                    return { exists: false, message: 'Preloader element not found' };
                }

                const style = window.getComputedStyle(preloader);
                return {
                    exists: true,
                    display: style.display,
                    visibility: style.visibility,
                    opacity: style.opacity,
                    zIndex: style.zIndex,
                    position: style.position,
                    width: style.width,
                    height: style.height,
                    backgroundColor: style.backgroundColor
                };
            }
        """)

        print(f"   Preloader exists: {preloader_info.get('exists')}")
        if preloader_info.get('exists'):
            print(f"   Display: {preloader_info.get('display')}")
            print(f"   Visibility: {preloader_info.get('visibility')}")
            print(f"   Opacity: {preloader_info.get('opacity')}")
            print(f"   Z-Index: {preloader_info.get('zIndex')}")
            print(f"   Position: {preloader_info.get('position')}")

        # Check body and main content
        print("\n3️⃣ Checking body and content visibility...")
        body_info = await page.evaluate("""
            () => {
                const body = document.body;
                const style = window.getComputedStyle(body);
                const mainContent = document.querySelector('[class*="banner"], .navbar, .container');

                return {
                    body: {
                        display: style.display,
                        visibility: style.visibility,
                        opacity: style.opacity
                    },
                    mainContent: mainContent ? mainContent.className : 'not found'
                };
            }
        """)

        print(f"   Body display: {body_info['body']['display']}")
        print(f"   Body visibility: {body_info['body']['visibility']}")
        print(f"   Body opacity: {body_info['body']['opacity']}")
        print(f"   Main content: {body_info['mainContent']}")

        # Get visible text
        print("\n4️⃣ Checking visible text content...")
        visible_text = await page.evaluate("() => document.body.innerText")
        visible_lines = visible_text.split('\n')[:5]
        print(f"   First lines visible: {visible_lines}")
        print(f"   Total text length: {len(visible_text)} characters")

        # Check what happens after waiting longer
        print("\n5️⃣ Waiting 4 seconds for preloader animation...")
        await page.wait_for_timeout(4000)

        preloader_after = await page.evaluate("""
            () => {
                const preloader = document.querySelector('.se-pre-con');
                if (!preloader) return { exists: false };
                const style = window.getComputedStyle(preloader);
                return {
                    exists: true,
                    display: style.display,
                    opacity: style.opacity
                };
            }
        """)

        print(f"   Preloader still exists: {preloader_after.get('exists')}")
        if preloader_after.get('exists'):
            print(f"   Display: {preloader_after.get('display')}")
            print(f"   Opacity: {preloader_after.get('opacity')}")

        # Take screenshots
        print("\n6️⃣ Taking screenshots...")
        await page.screenshot(path="/tmp/preloader_initial.png")
        print("   Screenshot (initial): /tmp/preloader_initial.png")

        await page.screenshot(path="/tmp/preloader_after_wait.png")
        print("   Screenshot (after 4s): /tmp/preloader_after_wait.png")

        # Test fix: Force remove preloader
        print("\n7️⃣ Testing fix - Force removing preloader...")
        await page.evaluate("""
            () => {
                const preloader = document.querySelector('.se-pre-con');
                if (preloader) {
                    preloader.style.display = 'none';
                }
            }
        """)

        await page.wait_for_timeout(1000)

        preloader_removed = await page.evaluate("""
            () => {
                const preloader = document.querySelector('.se-pre-con');
                if (!preloader) return false;
                return window.getComputedStyle(preloader).display === 'none';
            }
        """)

        print(f"   Preloader removed: {preloader_removed}")

        visible_content = await page.evaluate("() => document.body.innerText")
        print(f"   Visible content length after fix: {len(visible_content)}")

        await page.screenshot(path="/tmp/preloader_fixed.png")
        print("   Screenshot (after fix): /tmp/preloader_fixed.png")

        print("\n" + "=" * 60)
        print("✅ DIAGNOSTIC COMPLETE")
        print("=" * 60)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(diagnose_preloader())
