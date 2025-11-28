# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **static GitHub Pages project** containing interactive HTML visualizations and flowcharts. The repository hosts standalone HTML files that use client-side JavaScript libraries to render complex diagrams, concept maps, and technical documentation.

## Repository Structure

The project consists of independent HTML files, each serving as a self-contained visualization:

- **`vital_flowcharts.html`** - Vital CRM and BizForm synchronization architecture flowcharts (使用 Mermaid.js)
- **`lineflow.html`** - LINE messaging system integration architecture with multiple tabs showing system overview, group creation flow, message flow, decision trees, RPA execution, and tech stack (使用純 SVG)
- **`gpt.html`** - Interactive concept map analyzing AI-driven social engineering and LINE voting scams with enterprise risk analysis (使用 Viz.js/Graphviz)
- **`gemini.html`**, **`opus.html`** - Additional analysis/visualization files
- **`line-system-flowcharts.html`** - LINE system flowcharts (large file, ~35k tokens)

## Technology Stack

Each HTML file is completely self-contained and uses different visualization libraries:

1. **Mermaid.js** (`vital_flowcharts.html`)
   - CDN: `https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js`
   - Renders flowcharts, sequence diagrams, and system architecture diagrams
   - Initialized with: `mermaid.initialize({ startOnLoad: true, theme: 'default' })`

2. **Hand-crafted SVG** (`lineflow.html`)
   - Pure SVG with inline JavaScript for tab switching and interactivity
   - No external dependencies beyond fonts and styling

3. **Viz.js (Graphviz)** (`gpt.html`)
   - CDN: `https://cdnjs.cloudflare.com/ajax/libs/viz.js/2.1.2/`
   - Renders DOT language graph descriptions
   - Includes Panzoom library for zoom/pan functionality
   - MathJax for mathematical notation rendering

## Key Architectural Patterns

### HTML Structure Pattern
All files follow a similar structure:
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <!-- External library CDN links -->
    <!-- Inline CSS in <style> tags -->
</head>
<body>
    <!-- Content sections -->
    <!-- Inline JavaScript at the end -->
</body>
</html>
```

### Diagram Configuration Patterns

**Mermaid diagrams** are embedded in `<div class="mermaid">` tags with the diagram syntax directly inline.

**SVG diagrams** are manually constructed with:
- `<defs>` for reusable elements (gradients, markers)
- `<g>` groups with IDs for logical sections
- Path elements with `class="arrow"` for connections
- Text elements for labels

**Graphviz diagrams** are generated from DOT language strings in JavaScript, with:
- Node data stored in JavaScript objects mapping IDs to metadata
- Edge relationships defined as strings in DOT syntax
- Dynamic rendering triggered by user interactions

### Interactive Features

1. **Tab Navigation** (lineflow.html)
   - JavaScript event listeners on `.tab` elements
   - Show/hide `.diagram-container` sections based on `data-tab` attributes

2. **Concept Exploration** (gpt.html)
   - Click on tagged terms (`.tm` elements) to show explanations
   - Click on graph nodes to highlight and explain
   - Google search integration for terms
   - Full-screen modal for detailed graph exploration

3. **Zoom and Pan** (gpt.html)
   - Panzoom library integration for SVG manipulation
   - Full-screen modal with wheel zoom support

## Content Focus

The visualizations document enterprise software integration architectures, specifically:

- **CRM/BizForm sync workflows** - PostgreSQL data platform synchronization via webhooks and n8n automation
- **LINE messaging systems** - Three-party group chat architecture combining official accounts + personal accounts + RPA automation
- **Security analysis** - AI-powered social engineering threats and enterprise defense strategies

## Development Workflow

Since this is a static site:

1. **No build process** - Files can be edited directly and previewed in a browser
2. **No package manager** - All dependencies loaded via CDN
3. **No server required** - Open HTML files directly or use GitHub Pages
4. **Git workflow** - Standard git operations for version control

### Testing Changes

To test modifications:
```bash
# Simply open the file in a browser
open vital_flowcharts.html

# Or use a simple HTTP server if needed
python3 -m http.server 8000
# Then visit http://localhost:8000/vital_flowcharts.html
```

### Deployment

This is a GitHub Pages project. Any commits to the master branch are automatically deployed.

## Language

- **Content**: Traditional Chinese (zh-TW)
- **Comments**: Mix of Chinese and English
- **Variable names**: English

## Important Notes

1. **Self-contained files** - Each HTML file has all CSS and JavaScript inline. Do not attempt to extract shared resources unless explicitly requested.

2. **Large files** - `line-system-flowcharts.html` is ~35k tokens. When editing, use the Edit tool with specific old_string/new_string rather than reading the entire file.

3. **Mathematical notation** - `gpt.html` uses MathJax for LaTeX-style math rendering. Formulas are wrapped in `\\( ... \\)` or `$$ ... $$`.

4. **Chinese text encoding** - Ensure UTF-8 encoding is maintained when editing files with Chinese content.

5. **CDN dependencies** - All external libraries are loaded from CDNs. No local node_modules or package.json exists.

6. **Recent commits focus** - Recent work has been on refining the LINE group creation flow and RPA solution descriptions.
