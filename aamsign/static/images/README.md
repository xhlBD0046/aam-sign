# Static Images Folder Structure

This directory contains all static images for the Aamsign website, organized by product categories.

## Folder Structure

```
images/
├── channel-letters/           # Channel Letters Products
│   ├── front-lit/            # Front-Lit Channel Letters
│   ├── back-lit/             # Back-Lit / Halo-Lit Channel Letters
│   ├── front-back-lit/       # Front + Back-Lit Channel Letters
│   ├── open-face/            # Open-Face / Marquee Letters
│   ├── non-illuminated/      # Non-Illuminated 3D Letters
│   └── rgb-programmable/     # RGB / Programmable Channel Letters
│
├── neon-signs/               # LED Neon Signs
│   ├── custom-neon/          # Custom Neon Words & Logos
│   └── neon-lamps/           # Desk & Counter Neon Lamps
│
├── light-boxes/              # Light Box Products
│   ├── slim/                 # Slim LED Light Boxes
│   ├── blade/                # Double-Sided Blade Light Boxes
│   └── fabric/               # Fabric SEG Light Boxes
│
├── logo-signs/               # Logo Sign Products
│   └── metal-acrylic/        # Metal / Acrylic Logo Signs
│
├── factory/                  # Factory & Production Images
│   ├── production/           # Production process photos
│   └── facilities/           # Factory facilities and equipment
│
├── portfolio/                # Portfolio & Case Studies
│   ├──retail/              # Retail store projects
│   ├── restaurant/           # Restaurant & bar projects
│   ├── hotel/                # Hotel & hospitality projects
│   └── corporate/            # Corporate & office projects
│
└── general/                  # General Website Images
    ├── hero/                 # Hero section backgrounds
    ├── icons/                # Icons and graphics
    └── misc/                 # Miscellaneous images
```

## File Naming Conventions

### Format
Use lowercase with hyphens (kebab-case):
```
{category}-{type}-{description}-{number}.{ext}
```

### Examples

**Channel Letters:**
```
channel-letters/front-lit/
├── front-lit-storefront-red-01.jpg
├── front-lit-outdoor-night-02.jpg
└── front-lit-closeup-detail-03.jpg
```

**Neon Signs:**
```
neon-signs/custom-neon/
├── custom-neon-bar-logo-01.jpg
├── custom-neon-restaurant-text-02.jpg
└── custom-neon-office-design-03.jpg
```

**Light Boxes:**
```
light-boxes/slim/
├── slim-lightbox-menu-board-01.jpg
├── slim-lightbox-wall-mounted-02.jpg
└── slim-lightbox-backlit-display-03.jpg
```

**Portfolio:**
```
portfolio/retail/
├── retail-nike-store-exterior-01.jpg
├── retail-apple-store-interior-02.jpg
└── retail-mall-signage-03.jpg
```

## Image Guidelines

### Size Recommendations
- **Hero images**: 1920x1080px or larger
- **Product photos**: 1200x800px minimum
- **Portfolio images**: 1200x800px minimum
- **Thumbnails**: 400x300px

### Format
- **Primary**: WebP (for modern browsers)
- **Fallback**: JPG/PNG
- **Icons**: SVG preferred

### Quality
- Use high-quality, professional photos
- Optimize file sizes (compress without losing quality)
- Target: < 200KB per image

## Usage in Templates

### Django Template Example
```django
{% load static %}
<img src="{% static 'images/channel-letters/front-lit/front-lit-storefront-01.jpg' %}" 
     alt="Front-Lit Channel Letters Storefront">
```

### With Category Variable
```django
<img src="{% static 'images/channel-letters/'|add:category.slug|add:'/image-01.jpg' %}" 
     alt="{{ category.name }}">
```

## Quick Reference

| Product Category | URL Slug | Folder Path |
|-----------------|----------|-------------|
| Front-Lit Channel Letters | `front-lit` | `channel-letters/front-lit/` |
| Back-Lit Channel Letters | `back-lit` | `channel-letters/back-lit/` |
| Front+Back-Lit | `front-back-lit` | `channel-letters/front-back-lit/` |
| Open-Face Letters | `open-face` | `channel-letters/open-face/` |
| Non-Illuminated 3D | `non-illuminated` | `channel-letters/non-illuminated/` |
| RGB Programmable | `rgb-programmable` | `channel-letters/rgb-programmable/` |
| Custom Neon | `custom-neon` | `neon-signs/custom-neon/` |
| Neon Lamps | `neon-lamps` | `neon-signs/neon-lamps/` |
| Slim Light Boxes | `slim` | `light-boxes/slim/` |
| Blade Light Boxes | `blade` | `light-boxes/blade/` |
| Fabric Light Boxes | `fabric` | `light-boxes/fabric/` |
| Logo Signs | `metal-acrylic` | `logo-signs/metal-acrylic/` |

## Maintenance

- Keep folder structure consistent with product categories
- Remove unused images regularly
- Update this README when adding new categories
- Maintain .gitkeep files in empty folders for version control

---

**Last Updated**: 2025-12-04
**Maintained By**: Aamsign Dev Team
