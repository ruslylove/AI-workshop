# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose

Slidev deck (Thai language) for a seminar titled **"Generative AI มาประยุกต์ใช้ในการทำงาน"** — delivered by ผศ.ดร.รุสลี่ สุทธวีร์กูล to บุคลากรสายสนับสนุน ระดับภาควิชาฯ, คณะวิศวกรรมศาสตร์ (KMUTNB). Content covers the evolution AI Chat → Generative AI → Agentic AI with practical, reusable examples (drafting หนังสือราชการ, แปลภาษา, Excel, งานอาคาร/พัสดุ) and a hands-on "Super Support Challenge" workshop. When editing slides, preserve the Thai-first voice, "wow moment" pacing, and concrete case studies the audience can take back to their units.

## Commands

```bash
pnpm install      # install deps (uses pnpm; .npmrc + pnpm-lock.yaml)
pnpm dev          # slidev --open → http://localhost:3030
pnpm build        # outputs to dist/
pnpm export       # export deck (PDF/PPTX via slidev export)
```

Deployment targets are pre-wired: GitHub Pages via `.github/workflows/` (builds with `--base /${repo}/`), Netlify via `netlify.toml`, and Vercel via `vercel.json`. A push to `main` triggers the Pages deploy.

## Architecture

All presentation content lives in a single `slides.md` (~1100 lines, ~48 slides separated by `---` frontmatter blocks). Slidev conventions:

- **Root frontmatter** (top of [slides.md](slides.md)) sets theme `seriph`, Thai fonts (`Kanit` / `Sarabun`), and global config. Per-slide frontmatter (e.g. `layout: center`, `layout: two-cols`) controls layout.
- **[components/](components/)** — Vue SFCs auto-imported into slides by filename (e.g. `<CopyBox />`, `<Counter />`). Add new interactive widgets here rather than inlining large Vue blocks in markdown.
- **[pages/imported-slides.md](pages/imported-slides.md)** — extra slides pulled in via Slidev's `src:` import mechanism.
- **[snippets/external.ts](snippets/external.ts)** — code snippets referenced from slides via Slidev's external-code include syntax.
- **[public/](public/)** — static assets served at site root (e.g. `/logo_eng.jpg`, `/qrcode_slides.png`, `/qrcode_webapp.png`). Reference with absolute paths in slide markdown.
- **[global-bottom.vue](global-bottom.vue)** — Slidev global layer that renders `<SlideCurrentNo />` as a footer on every slide **except** `layout: cover`. When adding a title/cover-like slide that should hide the page number, use `layout: cover`.

Styling is UnoCSS utility classes (Tailwind-compatible syntax) directly in markdown — the deck leans heavily on `grid`, `bg-*/10 backdrop-blur-md`, colored border-accent cards, and emoji section headers. Match that visual language when adding slides.

## Editing notes

- Keep slide content in Thai; technical terms may remain in English.
- Session structure is Part 1 (บรรยาย & สาธิต, 9.00–10.30) / Part 2 (บรรยาย (ต่อ), 10.45–12.00) — new material should slot into this arc.
- Iconify sets available: `carbon`, `fluent`, `vscode-icons` (use as `<carbon-xxx />` etc.).
