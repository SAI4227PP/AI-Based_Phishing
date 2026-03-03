from .domain_features import extract_domain_features
from .html_features import extract_html_features
from .ssl_features import extract_ssl_features
from .url_features import extract_url_features


def extract_all_features(url: str, html: str = "") -> dict:
    features = {}
    features.update(extract_url_features(url))
    features.update(extract_html_features(html, url))
    features.update(extract_ssl_features(url))
    features.update(extract_domain_features(url))
    return features
