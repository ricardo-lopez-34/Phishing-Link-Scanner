# Phishing Link Scanner 🔍

A security tool that scrapes and analyzes URLs for malicious patterns, hidden redirects, and domain-spoofing indicators using heuristic analysis.

## Description
A proactive security tool that scrapes and analyzes URLs for malicious patterns, hidden redirects, and domain-spoofing indicators to identify phishing threats.

## Key Features
- **Heuristic Threat Detection:** Analyzes URL length, subdomains, and character obfuscation.
- **SSL Verification:** Inspects certificate authority and expiration status.
- **Redirect Mapping:** Follows shortened URLs to their final destination to uncover hidden malicious sites.

## Tech Stack
- **Language:** Python
- **Libraries:** Streamlit, BeautifulSoup4, Requests, Whois
- **Model:** Risk-scoring algorithm based on 12 common phishing indicators.

## Engineering Logic
- **Backend:** The scanner uses the `whois` protocol to check domain age (new domains are high-risk) and `BeautifulSoup` to find hidden "zero-pixel" redirects in the HTML.
- **Frontend:** A Streamlit dashboard provides a "Safety Meter" and a breakdown of the specific reasons a link was flagged.
