from __future__ import annotations

import ipaddress
import re
from urllib.parse import urlparse


SHORTENER_DOMAINS = {
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "rebrand.ly",
}


def safe_urlparse(url: str):
    parsed = urlparse(url if "://" in url else f"https://{url}")
    return parsed


def extract_hostname(url: str) -> str:
    return safe_urlparse(url).netloc.lower()


def strip_port(hostname: str) -> str:
    return hostname.split(":")[0]


def is_ip_address(hostname: str) -> bool:
    try:
        ipaddress.ip_address(strip_port(hostname))
        return True
    except ValueError:
        return False


def count_subdomains(hostname: str) -> int:
    host = strip_port(hostname)
    if not host:
        return 0
    return max(0, len(host.split(".")) - 2)


def has_prefix_suffix(hostname: str) -> bool:
    return "-" in strip_port(hostname)


def is_shortened_url(hostname: str) -> bool:
    return strip_port(hostname) in SHORTENER_DOMAINS


def contains_at_symbol(url: str) -> bool:
    return "@" in url


def has_suspicious_double_slash(url: str) -> bool:
    scheme_index = url.find("://")
    if scheme_index == -1:
        return "//" in url
    return "//" in url[scheme_index + 3 :]


def has_https_token_in_domain(hostname: str) -> bool:
    host = strip_port(hostname)
    return "https" in host.replace(".", "")


def count_pattern(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.IGNORECASE))
