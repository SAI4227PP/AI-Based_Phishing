URL_FEATURES = [
    "having_IP_Address",
    "URL_Length",
    "Shortining_Service",
    "having_At_Symbol",
    "double_slash_redirecting",
    "Prefix_Suffix",
    "having_Sub_Domain",
]

HTML_FEATURES = [
    "Request_URL",
    "URL_of_Anchor",
    "Links_in_tags",
    "SFH",
    "Submitting_to_email",
    "Abnormal_URL",
    "Redirect",
    "on_mouseover",
    "RightClick",
    "popUpWidnow",
    "Iframe",
]

SSL_FEATURES = [
    "SSLfinal_State",
    "HTTPS_token",
]

DOMAIN_FEATURES = [
    "Domain_registeration_length",
    "age_of_domain",
    "DNSRecord",
]

FEATURE_COLUMNS = URL_FEATURES + HTML_FEATURES + SSL_FEATURES + DOMAIN_FEATURES
