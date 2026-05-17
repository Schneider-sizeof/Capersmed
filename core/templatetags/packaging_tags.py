from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.simple_tag
def render_packaging_icon(pkg_name):
    """
    Renders a custom SVG icon for a given packaging name.
    Dynamically adjusts size or label based on volume if present in the name.
    """
    name_lower = pkg_name.lower()
    
    # Extract volume if present (e.g., "17L", "250", "65L", "100ml")
    volume_match = re.search(r'(\d+)\s*(l|ml)?', name_lower)
    volume_num = int(volume_match.group(1)) if volume_match else 0
    volume_unit = volume_match.group(2) if volume_match and volume_match.group(2) else ''
    
    if volume_num > 0 and not volume_unit:
        # Default to L if just a number is found in a context where it's likely liters
        if 'fut' in name_lower:
            volume_unit = 'l'

    volume_str = f"{volume_num}{volume_unit.upper()}" if volume_num else ""

    # Base SVG settings
    svg_width = 48
    svg_height = 48
    
    if 'fut' in name_lower:
        # Fût / Barrel
        # Scale the barrel size slightly based on volume
        # Let's say 17L is small (scale 0.7), 250L is big (scale 1.1)
        scale = 1.0
        if volume_num:
            if volume_num <= 20: scale = 0.75
            elif volume_num <= 40: scale = 0.85
            elif volume_num <= 100: scale = 0.95
            else: scale = 1.1
            
        w = int(32 * scale)
        h = int(40 * scale)
        # Center it
        x = (48 - w) // 2
        y = (48 - h) // 2
        
        # A nice modern barrel SVG
        # We can use a deep green or blue color
        color_top = "#2c5f2d"
        color_body = "#3b7a3e"
        color_band = "#1e3d1f"
        
        svg = f"""
        <svg class="pkg-icon-svg" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate({x}, {y})">
                <!-- Barrel Body -->
                <path d="M 0,{(h*0.1)} C 0,{-h*0.05} {w},{-h*0.05} {w},{(h*0.1)} C {w+w*0.1},{(h*0.5)} {w+w*0.1},{(h*0.8)} {w},{(h*0.9)} C {w},{h*1.05} 0,{h*1.05} 0,{(h*0.9)} C {-w*0.1},{(h*0.8)} {-w*0.1},{(h*0.5)} 0,{(h*0.1)} Z" fill="{color_body}" />
                <!-- Bands -->
                <path d="M {-w*0.08},{(h*0.25)} Q {(w/2)},{(h*0.35)} {w+w*0.08},{(h*0.25)}" fill="none" stroke="{color_band}" stroke-width="{h*0.06}" stroke-linecap="round"/>
                <path d="M {-w*0.09},{(h*0.75)} Q {(w/2)},{(h*0.65)} {w+w*0.09},{(h*0.75)}" fill="none" stroke="{color_band}" stroke-width="{h*0.06}" stroke-linecap="round"/>
                <!-- Top Cap -->
                <ellipse cx="{w/2}" cy="{h*0.08}" rx="{w/2.1}" ry="{h*0.05}" fill="{color_top}" />
            </g>
            """
        if volume_str:
            svg += f"""
            <rect x="2" y="32" width="44" height="14" rx="4" fill="#ffffff" fill-opacity="0.9" stroke="{color_band}" stroke-width="1"/>
            <text x="24" y="42" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="{color_band}" text-anchor="middle">{volume_str}</text>
            """
        svg += "</svg>"

    elif 'seau' in name_lower or 'seaux' in name_lower:
        # Bucket
        color_body = "#e0ede3"
        color_rim = "#c2d6c6"
        color_handle = "#7a9b80"
        svg = f"""
        <svg class="pkg-icon-svg" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(8, 14)">
                <!-- Handle -->
                <path d="M 0,6 C -4,-8 36,-8 32,6" fill="none" stroke="{color_handle}" stroke-width="2.5" stroke-linecap="round"/>
                <!-- Bucket Body -->
                <polygon points="2,6 30,6 26,30 6,30" fill="{color_body}" />
                <!-- Rim -->
                <ellipse cx="16" cy="6" rx="15" ry="3" fill="{color_rim}" />
                <ellipse cx="16" cy="6" rx="13" ry="2" fill="{color_body}" />
            </g>
            """
        if volume_str:
            svg += f"""
            <rect x="2" y="32" width="44" height="14" rx="4" fill="#ffffff" fill-opacity="0.9" stroke="{color_handle}" stroke-width="1"/>
            <text x="24" y="42" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#2c5f2d" text-anchor="middle">{volume_str}</text>
            """
        svg += "</svg>"

    elif 'bocal' in name_lower:
        # Glass Jar
        color_glass = "#e8f4f8"
        color_lid = "#d4af37" # Gold lid
        svg = f"""
        <svg class="pkg-icon-svg" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(10, 8)">
                <!-- Jar Body -->
                <rect x="4" y="8" width="20" height="24" rx="6" fill="{color_glass}" stroke="#b0d0e0" stroke-width="2"/>
                <!-- Shine -->
                <path d="M 8,12 L 8,28" stroke="#ffffff" stroke-width="2" stroke-linecap="round" fill="none"/>
                <!-- Lid -->
                <rect x="2" y="2" width="24" height="6" rx="2" fill="{color_lid}" stroke="#b5952f" stroke-width="1"/>
            </g>
        </svg>
        """

    elif 'boite' in name_lower or 'metallique' in name_lower or 'metal' in name_lower:
        # Metal Tin / Can
        color_tin = "#cdd3d6"
        color_ribs = "#a4b0b5"
        svg = f"""
        <svg class="pkg-icon-svg" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(10, 10)">
                <!-- Tin Body -->
                <path d="M 2,4 L 26,4 L 26,24 Q 14,28 2,24 Z" fill="{color_tin}" />
                <!-- Ribs -->
                <line x1="2" y1="10" x2="26" y2="10" stroke="{color_ribs}" stroke-width="1.5"/>
                <line x1="2" y1="15" x2="26" y2="15" stroke="{color_ribs}" stroke-width="1.5"/>
                <line x1="2" y1="20" x2="26" y2="20" stroke="{color_ribs}" stroke-width="1.5"/>
                <!-- Top Cap -->
                <ellipse cx="14" cy="4" rx="12" ry="3" fill="#e2e8ea" stroke="{color_ribs}" stroke-width="1"/>
            </g>
        </svg>
        """

    elif 'doypack' in name_lower:
        # Pouch / Doypack
        color_pouch = "#f5e6d3" # Kraft paper color or white
        color_cap = "#e63946"
        svg = f"""
        <svg class="pkg-icon-svg" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(10, 6)">
                <!-- Cap -->
                <rect x="10" y="0" width="8" height="6" rx="1" fill="{color_cap}" />
                <!-- Pouch Body -->
                <path d="M 6,6 C 14,6 22,6 22,6 C 26,16 28,26 28,34 C 28,38 24,38 14,38 C 4,38 0,38 0,34 C 0,26 2,16 6,6 Z" fill="{color_pouch}" stroke="#d4bba3" stroke-width="2"/>
                <!-- Bottom crease -->
                <path d="M 2,34 Q 14,30 26,34" fill="none" stroke="#d4bba3" stroke-width="2"/>
            </g>
        </svg>
        """

    else:
        # Generic Box
        color_box = "#d2b48c"
        svg = f"""
        <svg class="pkg-icon-svg" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(8, 12)">
                <polygon points="16,2 30,8 16,14 2,8" fill="#e6cdab" stroke="#b89a74" stroke-width="1.5" stroke-linejoin="round"/>
                <polygon points="2,8 16,14 16,28 2,22" fill="#d2b48c" stroke="#b89a74" stroke-width="1.5" stroke-linejoin="round"/>
                <polygon points="16,14 30,8 30,22 16,28" fill="#c3a37a" stroke="#b89a74" stroke-width="1.5" stroke-linejoin="round"/>
            </g>
            """
        if volume_str:
            svg += f"""
            <rect x="2" y="32" width="44" height="14" rx="4" fill="#ffffff" fill-opacity="0.9" stroke="#b89a74" stroke-width="1"/>
            <text x="24" y="42" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#8b6b47" text-anchor="middle">{volume_str}</text>
            """
        svg += "</svg>"

    return mark_safe(svg)
