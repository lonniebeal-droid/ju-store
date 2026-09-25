#!/usr/bin/env python3
"""
JU Storefront Verification Suite
Validates:
1. Local index.html structure, meta refresh, and canonical link
2. Live GitHub Pages HTTP status and redirection headers
3. Canonical AppDeploy storefront HTTP status and key catalog elements
4. Payment, contact, and media integration link invariants
"""

import sys
import os
import re
import urllib.request
import ssl
from pathlib import Path

# Setup unverified SSL context for environments with custom/strict CA bundles
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = {"User-Agent": "Mozilla/5.0 (JU-Storefront-Verifier/1.0)"}

CANONICAL_APPDEPLOY_URL = "https://ju-storefront-5hjkrj.v2.appdeploy.ai/"
GITHUB_PAGES_URL = "https://lonniebeal-droid.github.io/ju-store/"

PASS_COUNT = 0
FAIL_COUNT = 0

def record_pass(test_name):
    global PASS_COUNT
    PASS_COUNT += 1
    print(f"  [PASS] {test_name}")

def record_fail(test_name, reason):
    global FAIL_COUNT
    FAIL_COUNT += 1
    print(f"  [FAIL] {test_name}: {reason}")

def test_local_index_html():
    print("\n--- Testing Local index.html ---")
    index_path = Path(__file__).parent / "index.html"
    if not index_path.exists():
        record_fail("index.html exists", "File not found")
        return
    record_pass("index.html exists")

    content = index_path.read_text(encoding="utf-8")

    # Verify meta refresh
    if f'content="0;url={CANONICAL_APPDEPLOY_URL}"' in content:
        record_pass("Meta refresh points to canonical AppDeploy storefront")
    else:
        record_fail("Meta refresh points to canonical AppDeploy storefront", "Missing or incorrect URL in meta refresh")

    # Verify canonical link
    if f'<link rel="canonical" href="{CANONICAL_APPDEPLOY_URL}">' in content:
        record_pass("Canonical link points to canonical AppDeploy storefront")
    else:
        record_fail("Canonical link points to canonical AppDeploy storefront", "Missing or incorrect canonical link")

    # Verify title
    if "<title>JU Storefront</title>" in content:
        record_pass("Title is 'JU Storefront'")
    else:
        record_fail("Title check", "Expected <title>JU Storefront</title>")

    # Verify fallback anchor
    if f'href="{CANONICAL_APPDEPLOY_URL}"' in content and "Enter store" in content:
        record_pass("Fallback anchor link present")
    else:
        record_fail("Fallback anchor link", "Missing fallback link or anchor text")

def test_live_github_pages():
    print("\n--- Testing Live GitHub Pages ---")
    try:
        req = urllib.request.Request(GITHUB_PAGES_URL, headers=HEADERS)
        with urllib.request.urlopen(req, context=CTX, timeout=12) as resp:
            code = resp.getcode()
            body = resp.read().decode("utf-8")
            if code == 200:
                record_pass(f"GitHub Pages live HTTP 200 ({GITHUB_PAGES_URL})")
            else:
                record_fail("GitHub Pages live HTTP 200", f"Returned status {code}")
            
            if CANONICAL_APPDEPLOY_URL in body:
                record_pass("GitHub Pages body contains AppDeploy canonical redirect")
            else:
                record_fail("GitHub Pages body content", "Canonical AppDeploy URL missing from response body")
    except Exception as e:
        record_fail("GitHub Pages live check", str(e))

def test_canonical_appdeploy_storefront():
    print("\n--- Testing Canonical AppDeploy Storefront ---")
    try:
        req = urllib.request.Request(CANONICAL_APPDEPLOY_URL, headers=HEADERS)
        with urllib.request.urlopen(req, context=CTX, timeout=15) as resp:
            code = resp.getcode()
            body = resp.read().decode("utf-8")
            if code == 200:
                record_pass(f"AppDeploy storefront HTTP 200 ({CANONICAL_APPDEPLOY_URL})")
            else:
                record_fail("AppDeploy storefront HTTP 200", f"Returned status {code}")

            # Verify title
            if "<title>JU | Music, Books, AI, Business</title>" in body:
                record_pass("Storefront title matches 'JU | Music, Books, AI, Business'")
            else:
                record_fail("Storefront title check", "Page title does not match expected title")

            # Verify key sections
            expected_sections = [
                "JU Audiobooks",
                "JU Music Store",
                "JU Books & Digital Library",
                "JU Projects",
                "Contact JU",
            ]
            for sec in expected_sections:
                if sec in body:
                    record_pass(f"Section present: '{sec}'")
                else:
                    record_fail(f"Section present: '{sec}'", "Section text not found in storefront HTML")

            # Verify Stripe Checkout links (aligned to live AppDeploy HTML 2026-09-25)
            stripe_links = [
                "buy.stripe.com/8x29AV63P83R5Wg56adIA00",
                "buy.stripe.com/00w9AVfEp83R70kPUdIA01",
                "buy.stripe.com/bJefZjdwh83R4Sc1TYdIA02",
                "buy.stripe.com/28E28tak5gAnfwQeGKdIA03",
            ]
            for s in stripe_links:
                if s in body:
                    record_pass(f"Stripe checkout link found: {s}")
                else:
                    record_fail(f"Stripe checkout link found: {s}", "Stripe URL missing from HTML")

            # Verify Jessie AI Receptionist demo phone
            if "tel:+17708474325" in body:
                record_pass("Jessie Receptionist demo phone line found (+17708474325)")
            else:
                record_fail("Jessie Receptionist demo phone line", "tel:+17708474325 missing from HTML")

            # Verify Payhip products
            payhip_ids = ["1z2xi", "AnDrk", "lBpzb"]
            for pid in payhip_ids:
                if f"payhip.com/b/{pid}" in body:
                    record_pass(f"Payhip audiobook product found (id: {pid})")
                else:
                    record_fail(f"Payhip audiobook product {pid}", f"payhip.com/b/{pid} missing")

            # Verify Gumroad products
            if "atlantafinest.gumroad.com/l/BlackLawvol1" in body:
                record_pass("Gumroad product found (BlackLawvol1)")
            else:
                record_fail("Gumroad BlackLawvol1", "Link missing")

            if "atlantafinest.gumroad.com/l/streetlevelsurvival" in body:
                record_pass("Gumroad product found (streetlevelsurvival)")
            else:
                record_fail("Gumroad streetlevelsurvival", "Link missing")

    except Exception as e:
        record_fail("AppDeploy live check", str(e))

def main():
    print("==================================================")
    print("JU STOREFRONT VERIFICATION SUITE")
    print("==================================================")
    test_local_index_html()
    test_live_github_pages()
    test_canonical_appdeploy_storefront()

    print("\n==================================================")
    print(f"VERIFICATION SUMMARY: {PASS_COUNT} PASSED, {FAIL_COUNT} FAILED")
    print("==================================================")
    if FAIL_COUNT > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
