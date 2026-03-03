from __future__ import annotations

from .utils import count_pattern


def extract_html_features(html: str, url: str) -> dict:
    if not html:
        html = ""

    return {
        "Request_URL": count_pattern(html, r"<img|<video|<audio"),
        "URL_of_Anchor": count_pattern(html, r"<a\s"),
        "Links_in_tags": count_pattern(html, r"<link|<script|<meta"),
        "SFH": count_pattern(html, r"<form"),
        "Submitting_to_email": int("mailto:" in html.lower()),
        "Abnormal_URL": int(url not in html if html else 0),
        "Redirect": count_pattern(html, r"http-equiv=['\"]refresh['\"]"),
        "on_mouseover": count_pattern(html, r"onmouseover\s*="),
        "RightClick": int("contextmenu" in html.lower() or "button==2" in html.lower()),
        "popUpWidnow": count_pattern(html, r"window\.open"),
        "Iframe": count_pattern(html, r"<iframe"),
    }
