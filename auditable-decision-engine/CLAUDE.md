# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Auditable Decision Engine** (可稽核的決策證據鏈) - A marketing landing page for an enterprise decision-making platform that transforms evaluation processes from subjective debates to evidence-based decisions with full traceability.

## Technology Stack

- **HTML5** - Single self-contained file (`index.html`, ~88KB, 1450+ lines)
- **Tailwind CSS** - Via CDN (`cdn.tailwindcss.com`)
- **Noto Sans TC** - Google Fonts for Traditional Chinese typography
- **Vanilla JavaScript** - No frameworks

## Architecture

Single-file static site with all HTML, CSS, and JavaScript inline. No build process.

### Key Sections

1. Hero with value proposition
2. Three Core Capabilities (Boundary-Based Scoring, Evidence-Anchored Output, Consistency Guarantee)
3. Four Evaluation Solutions (Innovation Evaluator, Vendor Claim Verifier, Portfolio Signal Extractor, OKR Drift Scanner)
4. Auditable JSON Schema specifications
5. TAM/SAM/SOM market analysis
6. Pricing tiers (Starter, Growth, Enterprise)
7. Development roadmap and risk matrix

### JavaScript Features

- **Intersection Observer** - Scroll-triggered animations (threshold: 0.1)
- **Smooth Scrolling** - Anchor-based navigation
- **Tailwind Config** - Custom primary color palette

### CSS Patterns

- `@keyframes fadeInUp`, `float`, `pulse-glow`, `gradient-shift` - Custom animations
- `.glass`, `.glass-dark` - Backdrop blur effects
- `.card-hover` - Hover transform/shadow transitions
- `.gradient-text` - Multi-color gradient text
- `.grid-bg` - Subtle grid background pattern

## Development

```bash
# Preview locally
open index.html
# or
python3 -m http.server 8000
```

No build step required. Edit `index.html` directly.

## Deployment

GitHub Pages - commits to master branch auto-deploy.

## Language

Content in Traditional Chinese (zh-TW). UTF-8 encoding.
