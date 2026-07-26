# One Water OS Brand and Design Requirements

Graphite is the approved default for new public knowledge and learning products. Clearwater remains
the approved operational application system until those screens are deliberately migrated.
Sources of truth are [`owos-graphite.css`](owos-graphite.css) and
[`OWOS-GRAPHITE-VISUAL-STANDARD.md`](../standards/OWOS-GRAPHITE-VISUAL-STANDARD.md) for public
knowledge products, and [`owos-brand.css`](owos-brand.css) for existing Clearwater application
surfaces.

---

## 1. Identity

| | |
|---|---|
| **Product** | One Water OS (OWOS) |
| **Maker** | APAS.ai |
| **Category line** | The first knowledge-continuity platform built for water. |
| **Agent / mascot** | **Droobi** — the blue water-drop guide. Droobi is the face of the system: a helper, an anchor, a guide. |
| **Broadcast register** | One Water TV — "The Water Newsroom" (Droobi as anchor; serif display; darker studio blue). |
| **Design system** | v7 "Graphite" for public knowledge and learning products; v6 "Clearwater" retained for existing operational application surfaces. |
| **Design ethos** | Graphite depth, strong type, generous spacing, restrained water-blue illumination, and one clear idea at a time. |

**Sample voice lines (from live assets):**
- *"A career of wisdom deserves better than a binder."*
- *"The first knowledge-continuity platform built for water."*
- On-air proof style: `✓ verified · primary source`

---

## 2. Graphite default for public knowledge products

Use `#1C1B19` for the primary canvas, `#292826` for elevated surfaces, `#10232E` for deep process
surfaces, `#F2F1EC` and `#D9D6CF` for text, `#7DC6E8` for the water concept and active state,
`#E0A64A` for caution and consequence, `#4AC88C` for favorable or stable meaning, and `#EE7968`
for critical states.

Graphite is a visual identity, not a page template. Courses, Concept Briefs, articles, reports, and
SOP templates must still use a product-specific design brief and varied composition.

## 3. Clearwater tokens for retained application surfaces

Copy these exactly. Names match the CSS custom properties.

### Surfaces & ink (light (default) theme)
| Token | Hex | Role |
|---|---|---|
| `--bg` | `#F7F9FB` | Page background |
| `--surface` | `#FFFFFF` | Cards, panels |
| `--surface-2` | `#EFF3F7` | Recessed / hover |
| `--surface-3` | `#E5EBF1` | Table headers, chips |
| `--ink` | `#0F1728` | Headings, primary text |
| `--ink-2` | `#44546A` | Body text |
| `--ink-3` | `#8595AB` | Muted / captions |
| `--line` | `#E4E9F0` | Hairlines |
| `--line-2` | `#CDD6E1` | Stronger borders |

### Brand — water blue
| Token | Hex | Role |
|---|---|---|
| `--brand` | `#0A78BA` | Primary. Links, logo, buttons, kickers |
| `--brand-700` | `#08669F` | Hover |
| `--brand-800` | `#07547F` | Deep / text on light-blue |
| `--brand-50` | `#EAF5FC` | Tint background (pills, active nav) |
| `--brand-100` | `#D3EAF8` | Selection, focus ring, borders |

### Accent — gold, plus semantics
| Token | Hex | Role |
|---|---|---|
| `--gold` | `#A97B0F` | **The accent.** The drop-in-the-logo, highlights, one italic word |
| `--gold-500` | `#C9961B` | Brighter gold |
| `--gold-50` | `#FBF5E4` | Gold pill background |
| `--green` | `#0E8A64` | Go / verified / on-track |
| `--green-50` | `#E7F6F0` | Green pill background |
| `--red` | `#D64545` | Critical / at-risk |
| `--red-50` | `#FCEDED` | Red pill background |

### Dark panels
Panels on brand-blue or ink surfaces flip local tokens: `--ink:#FFFFFF`, `--ink-2:#DCEAF4`,
`--ink-3:#AFC8D9`, kickers become `#9BE3F8`, gold highlight `#F2C94C`.

---

## 4. Typography

Graphite public products use `Arial, Barlow, sans-serif` for primary display and body copy, with
`"Courier New", "Space Mono", monospace` for technical labels, sources, data, and navigation.
Existing Clearwater application surfaces retain Inter and JetBrains Mono until migrated.

- **One typeface everywhere: `Inter`.** Fallback stack: `'Inter', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif`.
  In production, host/embed Inter (the CSS assumes it is loaded). In sandboxed artifacts where font
  CDNs are blocked, the fallback (`-apple-system` / San Francisco) is the approved substitute.
- **Mono: `JetBrains Mono`** → `'JetBrains Mono','SF Mono',Menlo,monospace`. Used for kickers, labels,
  code, pills, breadcrumbs, data ("proof" text), tickers.
- **Base body:** 17px / line-height 1.7 / color `--ink-2`.
- **Headings:** weight **800**, letter-spacing **-0.022em**, line-height 1.12, color `--ink`.
  - h1 `clamp(34px, 4.6vw, 54px)` · h2 `clamp(26px, 3.2vw, 38px)` · h3 `clamp(19px, 2vw, 24px)`
- **Kicker / eyebrow label:** JetBrains Mono, 12px, weight 600, letter-spacing **.14em**, UPPERCASE,
  color `--brand` (or `#9BE3F8` on dark).

---

## 5. Geometry & elevation

| Token | Value |
|---|---|
| `--r` | `12px` (default radius) |
| `--r-lg` | `18px` (cards) |
| `--sh` | `0 1px 2px rgba(15,23,40,.06), 0 1px 3px rgba(15,23,40,.04)` |
| `--sh-lg` | `0 4px 6px -2px rgba(15,23,40,.05), 0 16px 40px -12px rgba(15,23,40,.16)` |
| `--wrap` | `1200px` content max-width (24px side padding; 16px on mobile) |

Buttons/inputs: radius 10px. Pills: 999px. Logo tile: 9px.

---

## 6. Core components

- **Nav** (`owos-nav`): fixed, 64px, translucent white with 14px blur, hairline bottom. Left = brand
  lockup; right = links + a primary **badge** CTA with a pulsing green "live" dot.
- **Logo lockup** (`owos-brand`): drop icon in a rounded tile + wordmark. Wordmark = `One Water` in ink
  with a **brand-blue bold** accent word; a small mono sub-line (`by APAS.ai`) with an italic `--gold` word.
- **Button** (`owos-btn`): brand fill, white text, radius 10, weight 650, soft shadow; hover → `--brand-700`.
  Ghost variant: white bg, `--line-2` border.
- **Card** (`owos-card`): white surface, `--line` border, radius 18, `--sh` shadow.
- **Pill** (`owos-pill`): mono, 11px, uppercase, .08em, radius 999. Variants: default (blue), `.gold`, `.green`.
- **Table:** uppercase mono headers in `--ink-3`; hairline rows; 15px body in `--ink-2`.
- **Motif:** the **knowledge-graph constellation** — connected nodes with one gold node — used as
  ambient decoration on dark hero surfaces.

---

## 7. Droobi, the agent

The character that guides the user. Reference: [`droobi.svg`](droobi.svg), [`onewater-tv-anchor-v3-poster.png`](onewater-tv-anchor-v3-poster.png).

| Feature | Spec |
|---|---|
| **Form** | A water drop with a face. |
| **Body gradient** | top `#8fd3f6` → mid `#3fa8e8` → base `#176fae` (vertical) |
| **Outline** | `#0b5f91`, ~8px stroke |
| **Eyes** | white sclera; iris `#2e6fa8`; pupil `#10253c`; white catch-light |
| **Brows / mouth** | `#153049` brows; `#10253c` smile; tongue `#ed8478` |
| **Signature badge** | a **gold water-drop pendant** at the base — `#f2c94c`, gold outline `#b7891f`, dark drop inside. This is Droobi's identifying mark. |
| **Personality** | calm, credible, helpful. A guide, not a cartoon. In "TV" mode: a headset-mic news anchor delivering *verified · primary source* facts. |
| **Use in PM system** | Droobi appears as the assistant/avatar in the playbook and dashboards — the voice of tips, the "ask me" affordance, the friendly proof-checker. Keep Droobi small and purposeful; never decorative filler. |

---

## 8. Voice and role lenses

**Tone:** plain, credible, calm-expert. Evidence over adjectives (`✓ verified · primary source`).
Water-sector fluent. Never hype; never a binder.

**Audience role lenses** (from *My Water OS* — use these to target reports and dashboards):

| Lens | Cares about |
|---|---|
| **Utility manager** | Decision risk, readiness, policy movement, accountable ownership |
| **Operator** | Practical operating knowledge, maintenance/treatment, field questions, training |
| **Researcher** | Evidence gaps, active threads, adopted work |
| **Consultant** | Patterns, scopes, cases, teaching opportunities |
| **Data leader** | Data governance, AI readiness, decision architecture |

---

## 9. Do and do not

**Do** use Graphite for new public knowledge products, water blue as the concept and action color,
amber only for caution or consequence, calm dark surfaces, generous spacing, and visible proof.
Keep Droobi purposeful.

**Do not** clone one page layout across different learning jobs, scatter accent colors, use amber as
a decorative background wash, publish restricted infrastructure detail, or let Droobi become
clip-art.

---

*Assets in this folder: `owos-graphite.css` (public knowledge identity), `owos-brand.css` (retained
Clearwater application system), `droobi.svg` (agent), `icon-192/512.png` (app icons),
`og-image.png` (social/positioning), `onewater-tv-anchor-v3-poster.png` (Droobi anchor reference).*
