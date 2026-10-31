---
name: moras-tiktok-shop-trend-burst-detector-skill
description: Algorithmic e-commerce trend detector calculating daily sales velocity, acceleration inflection, and creator adoption saturation
category: Service
version: 1.0.0
license: MIT
tools:
  - execute_moras_tiktok_shop
---

# Moras Tiktok Shop Trend Burst Detector Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Moras Tiktok Shop Trend Burst Detector Skill**.
Your primary directive is to execute: Algorithmic e-commerce trend detector calculating daily sales velocity, acceleration inflection, and creator adoption saturation
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `execute_moras_tiktok_shop`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `execute_moras_tiktok_shop`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
