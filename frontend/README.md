# Hangzhou Real Estate — Frontend Specification

## Overview
A 3-page real estate web application for the Hangzhou market. Clean, elegant, West Lake–inspired aesthetic. No AI-generated images — all image paths are placeholders you replace with your own assets.

---

## Design System

- **Aesthetic**: Refined minimalist — frosted glass cards, soft sky-blue palette, ink-wash textures
- **Font**: `Cormorant Garamond` (display) + `DM Sans` (body) — loaded from Google Fonts
- **Color palette**:
  - Background: `#ddeaf5` → `#f0f6fc` gradient (sky)
  - Card surface: `rgba(255,255,255,0.55)` (glass)
  - Accent: `#1a3f6f` (deep lake blue)
  - Text primary: `#12243a`
  - Text muted: `#5a7a9a`
- **Hover interaction**: Every card/row scales up slightly (`transform: scale(1.025)`) with a lifted shadow — applied globally via CSS
- **Transition**: `0.25s cubic-bezier(0.34,1.56,0.64,1)` (springy)

---

## Navigation (all pages)

- **Left**: Hangzhou pagoda logo (SVG inline) + "Hangzhou" wordmark
- **Center**: **EMPTY** — no nav links in the center
- **Right**: User icon + Hamburger menu icon
  - **Hamburger menu drawer** contains:
    - `Home` (always visible)
    - `Contact Us` (always visible)
    - Current page is highlighted / grayed out

---

## Page 1 — User Profile Dashboard (`index.html` / slide 1)

### Layout: 2 columns

**Column A — User Card** (left, narrow)
- Avatar image: `assets/user/avatar.jpg` ← replace with your file
- Name: "Li Wei"
- Badge: "Premium" (pill)
- Nav list: Home · Navigation · Notification · User Profile (with icons)

**Column B — Content** (right, wide) — 2 sub-cards side by side:

**Sub-card 1: My Saved Forecasts**
- List of saved forecast rows
- Each row: `{RoomType}, {District} | ¥{Price}`
- Bottom button: **"Generate New Forecast"** → navigates to Page 3

**Sub-card 2: Favorite Listings**
- 2×N grid of listing thumbnails
- Each thumbnail: `assets/listings/listing-{n}.jpg` ← replace with your files
- Heart icon overlay (toggle)
- Caption: room type + district

### Hover rule
Every card, every row, every listing thumbnail → scale up + shadow lift on hover.

---

## Page 2 — Contact Us (`contact.html` / slide 2)

### Layout: 2 columns

**Column A — Get in Touch form**
- Fields: Name, Email, Topic (dropdown: General / Forecast Help / Listing Query), Message (textarea)
- Submit button: **"Send Message"**
- No images generated — bamboo/pagoda decorative SVG only (inline, already in code)

**Column B — Our Office / Support**
- Map embed placeholder: `assets/map/hangzhou-map.jpg` ← replace with your screenshot or embed
- Address block
- Phone: `+007-053-5880`
- Email: `Support@hangzhou.com`
- Social icons: Facebook · Telegram · Twitter

### Hover rule
Form fields glow on focus. Submit button lifts. Office card lifts on hover.

---

## Page 3 — Price Forecast / Home (`forecast.html` / slide 3)

### Layout: top result + 3 filter cards + CTA

**Price Forecast Result box** (top right)
- Shows calculated price: `¥ 3,850,000`
- Updates live as filters change (JS)

**Filter Card 1 — Area & Location**
- Subway Line (pill toggles: Line 1 / Line 2 / Line 3)
- Subway Distance (range slider)
- School Distance (dropdown)
- Neighborhood Amenities (dropdown)
- **NEW — District selector** (above this card, slim bar):
  - Hangzhou districts with Chinese names:
    - Xihu (西湖) · Gongshu (拱墅) · Shangcheng (上城) · Binjiang (滨江) · Xiaoshan (萧山) · Yuhang (余杭)
  - Active district highlighted; clicking updates filter

**Filter Card 2 — House Details**
- Floor (Low / Medium / High toggles)
- Age (New / <10 years / 10-20 years)
- Decoration (Standard / Luxury / Simple)
- Has Elevator (toggle switch)

**Filter Card 3 — Property Specifics**
- Property Type (Apartment / House / Villa)
- Room Type (1-Bedroom / 2-Bedroom / 3-Bedroom)
- Bathrooms (1 / 2 / 3 / etc)
- Parking Rate (dropdown)

**CTA Button**: **"Find Matching Listings"** → navigates to listings

### Hover rule
Each filter card lifts on hover. Pill/toggle buttons pop on hover. District bar items highlight on hover.

---

## Image Asset Paths (replace with your files)

```
assets/
  user/
    avatar.jpg              ← user profile photo
  listings/
    listing-1.jpg
    listing-2.jpg
    listing-3.jpg
    listing-4.jpg
    listing-5.jpg
    listing-6.jpg           ← favorite listing thumbnails
  map/
    hangzhou-map.jpg        ← office location map screenshot
  bg/
    westlake.jpg            ← (optional) hero background photo
```

All `<img>` tags in the HTML use these relative paths. Replace the files and the UI updates automatically.

---

## File Structure

```
/
├── index.html          ← Page 1: User Profile Dashboard
├── contact.html        ← Page 2: Contact Us
├── forecast.html       ← Page 3: Price Forecast (Home)
├── style.css           ← Shared styles, design tokens, hover animations
├── nav.js              ← Shared navigation / hamburger drawer
├── README.md           ← This file
└── assets/
    ├── user/
    ├── listings/
    ├── map/
    └── bg/
```

---

## Interactions Summary

| Element | Hover Effect |
|---|---|
| Any card / panel | `scale(1.025)` + shadow lift |
| Nav menu items | Color shift + underline slide |
| Listing thumbnails | Scale + heart icon appears |
| Forecast rows | Background tint + scale |
| Pill toggles | Pop scale + color fill |
| Buttons | Lift + slight scale |
| Form fields | Glow border |
| District pills | Color fill + scale |

---

## Notes
- No external image generation. All visuals = your local assets + inline SVG decorations.
- Pages link to each other via `<a href>`.
- Menu drawer slides in from right; backdrop closes it.
- All animations use CSS only (no heavy JS libraries needed).
