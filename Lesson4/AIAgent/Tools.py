from langchain.agents import  tool
import re
from urllib.parse import urlparse



@tool
def extract_urls_from_text(text: str) -> list[str]:
    """
    Extracts URLs (links) from a given text.
    Example: 'Click here at https://example.com/fish and visit the site.' will return ['https://example.com/fish']
    """
    # Regex to identify URLs
    urls = re.findall(r'https?://(?:www\.)?\S+\.\S+', text)
    # This filtering removes trailing punctuation like periods at the end of sentences that might stick to the URL
    cleaned_urls = [url.rstrip('.,;)') for url in urls]
    return list(set(cleaned_urls)) # Remove duplicates


@tool
def check_url_reputation(url: str) -> str:
    """
    Checks the reputation of a URL.
    Simulates a check against an external service or a simple blacklist.
    Returns 'Suspicious' if the URL appears to be phishing, 'Safe' if it seems legitimate,
    or 'Unknown' if there's not enough information.
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    #print(domain)

    # Blacklist (for demonstration purposes only! Not for real security use)
    suspicious_domains = [
        "paypal-login.ru", "microsoft-support.xyz", "apple-verify.com",
        "bank-security.biz", "secure-login-update.info", "amazon-gift.co",
        "login-micr0s0ft.com" # Added for example 3
    ]

    # Simple reputation checks:
    if any(s_domain in domain for s_domain in suspicious_domains):
        return f"The domain '{domain}' was identified on the blacklist as highly suspicious for phishing."

    # Examples of common legitimate domains
    legit_domains = ["google.com", "microsoft.com", "apple.com", "paypal.com", "amazon.com", "bankhapoalim.co.il", "leumi.co.il"]
    if any(l_domain in domain for l_domain in legit_domains):
        return f"The domain '{domain}' appears legitimate and well-known."

    # Simple check for numbers within the domain name (might indicate spoofing)
    if re.search(r'\d', domain.split('.')[0]):
        return f"The domain '{domain}' contains numbers, which might indicate a spoofing attempt (phishing)."

    # Simple check for long and unfamiliar domains (not always accurate)
    if len(domain.split('.')[0]) > 20 and not any(d in domain for d in legit_domains):
        return f"The domain '{domain}' is long and unfamiliar, which could be suspicious."

    return f"The domain '{domain}' was not identified in known lists. Further investigation needed."




if __name__ == "__main__":
    SMS = """
    שלום
זיהינו פעילויות חריגות בכרטיס האשראי שלך. על מנת להגן עליך בוצעה חסימה זמנית של הכרטיס.
להחזרת הכרטיס לפעילות
https://t.co/t6MD4D73Ma
    
    """
    print(extract_urls_from_text(SMS))
    print(check_url_reputation(SMS))

