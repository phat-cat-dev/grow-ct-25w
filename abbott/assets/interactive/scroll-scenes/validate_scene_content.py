#!/usr/bin/env python3
"""Kept for convenience. Same as: python scenes.py check <file>"""
import sys
import scenes

sys.exit(scenes.main(["check", *sys.argv[1:]]))
