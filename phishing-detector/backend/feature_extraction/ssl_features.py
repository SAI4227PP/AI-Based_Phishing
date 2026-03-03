from __future__ import annotations

from .utils import extract_hostname, has_https_token_in_domain, safe_urlparse


def extract_ssl_features(url: str) -> dict:
    parsed = safe_urlparse(url)
    hostname = extract_hostname(url)
    is_https = parsed.scheme.lower() == "https"

    return {
        "SSLfinal_State": int(is_https),
        "HTTPS_token": int(has_https_token_in_domain(hostname) and not is_https),
    }
