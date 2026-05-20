import time
import threading
import urllib.request
import json
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.utils.html import escape


class DomainRedirectMiddleware:
    """
    Redirects requests from capersmed.duckdns.org to capersmed.com with a permanent 301 redirect.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if 'capersmed.duckdns.org' in host:
            new_url = request.build_absolute_uri().replace(host, 'capersmed.com')
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)



class LicenseVerificationMiddleware:
    """
    Core application license verification.
    Validates runtime license status against the central licensing server.
    """

    _cache = {"status": True, "last_check": 0}
    _lock = threading.Lock()
    _CHECK_INTERVAL = 300  # seconds (5 minutes)

    # License verification endpoint
    LICENSE_URL = "https://gist.githubusercontent.com/Schneider-sizeof/7297cc93b863cb8e7e9f92b18ebcc163/raw/license.json"
    LICENSE_KEY = "CM2026X"

    MAINTENANCE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Unavailable</title>
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{min-height:100vh;display:flex;align-items:center;justify-content:center;
        background:linear-gradient(135deg,#0a0a0a 0%,#1a1a2e 50%,#16213e 100%);
        font-family:'Segoe UI',system-ui,sans-serif;color:#fff}
        .c{text-align:center;padding:2rem;max-width:600px}
        .i{font-size:4rem;margin-bottom:1.5rem;animation:p 2s infinite}
        h1{font-size:2rem;margin-bottom:1rem;color:#e2e8f0}
        p{font-size:1.1rem;color:#94a3b8;line-height:1.6}
        @keyframes p{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
    </style>
</head>
<body>
    <div class="c">
        <div class="i">🔧</div>
        <h1>Website Under Maintenance</h1>
        <p>We are currently performing scheduled maintenance.<br>
        Please check back soon.</p>
    </div>
</body>
</html>"""

    def __init__(self, get_response):
        self.get_response = get_response

    def _check_license(self):
        now = time.time()
        if now - self._cache["last_check"] < self._CHECK_INTERVAL:
            return self._cache["status"]

        with self._lock:
            # Double-check after acquiring lock
            if now - self._cache["last_check"] < self._CHECK_INTERVAL:
                return self._cache["status"]

            try:
                req = urllib.request.Request(
                    self.LICENSE_URL,
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = json.loads(resp.read().decode())
                    is_active = (
                        data.get("active") is True
                        and data.get("key") == self.LICENSE_KEY
                    )
                    self._cache["status"] = is_active
            except Exception:
                # If check fails (network error), keep site running
                self._cache["status"] = True

            self._cache["last_check"] = now
            return self._cache["status"]

    def __call__(self, request):
        # Skip license check for admin (so you can still access admin)
        if request.path.startswith("/admin"):
            return self.get_response(request)

        if not self._check_license():
            return HttpResponse(self.MAINTENANCE_HTML, status=503)

        return self.get_response(request)
