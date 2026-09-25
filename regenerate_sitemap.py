#!/usr/bin/env python3
"""Superseded: use scripts/generate_sitemap.py (real per-page lastmod dates).
Kept as a thin wrapper so existing habits keep working."""
import os
import runpy

runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts', 'generate_sitemap.py'), run_name='__main__')
