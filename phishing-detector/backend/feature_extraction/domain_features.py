from __future__ import annotations

from .utils import extract_hostname, strip_port


def extract_domain_features(url: str) -> dict:
    hostname = strip_port(extract_hostname(url))
    domain_parts = hostname.split(".") if hostname else []
    registration_length = max(0, 365 - (len(hostname) * 3))
    age = max(1, len(domain_parts) * 30)
    has_dns = int(bool(hostname and "." in hostname))

    return {
        "Domain_registeration_length": registration_length,
        "age_of_domain": age,
        "DNSRecord": has_dns,
    }
