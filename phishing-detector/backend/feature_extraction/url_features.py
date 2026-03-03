from __future__ import annotations

from .utils import (
    contains_at_symbol,
    count_subdomains,
    extract_hostname,
    has_prefix_suffix,
    has_suspicious_double_slash,
    is_ip_address,
    is_shortened_url,
)


def extract_url_features(url: str) -> dict:
    hostname = extract_hostname(url)
    subdomain_count = count_subdomains(hostname)

    return {
        "having_IP_Address": int(is_ip_address(hostname)),
        "URL_Length": len(url),
        "Shortining_Service": int(is_shortened_url(hostname)),
        "having_At_Symbol": int(contains_at_symbol(url)),
        "double_slash_redirecting": int(has_suspicious_double_slash(url)),
        "Prefix_Suffix": int(has_prefix_suffix(hostname)),
        "having_Sub_Domain": subdomain_count,
    }
