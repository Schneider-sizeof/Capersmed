/**
 * Cookie Consent Manager
 * Handles the display, saving, and enforcement of cookie preferences.
 * Uses vanilla JavaScript.
 */

const CookieConsent = (function() {
    // Configuration
    const COOKIE_NAME = 'capersmed_cookie_consent';
    const EXPIRATION_DAYS = 365;
    
    // Default categories (Necessary is always true)
    const DEFAULT_CONSENT = {
        necessary: true,
        analytics: false,
        marketing: false,
        preferences: false,
        timestamp: null
    };

    // DOM Elements (will be populated on init)
    let els = {};

    /**
     * Get a cookie value by name
     */
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    /**
     * Set a cookie
     */
    function setCookie(name, value, days) {
        let expires = "";
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = `; expires=${date.toUTCString()}`;
        }
        document.cookie = `${name}=${value}${expires}; path=/; SameSite=Lax`;
    }

    /**
     * Parse the current consent state from the cookie
     */
    function getConsentState() {
        const cookieStr = getCookie(COOKIE_NAME);
        if (cookieStr) {
            try {
                return JSON.parse(decodeURIComponent(cookieStr));
            } catch (e) {
                console.error("Cookie consent parse error", e);
            }
        }
        return null; // No consent given yet
    }

    /**
     * Save the consent state to the cookie
     */
    function saveConsentState(state) {
        state.timestamp = new Date().toISOString();
        const value = encodeURIComponent(JSON.stringify(state));
        setCookie(COOKIE_NAME, value, EXPIRATION_DAYS);
        
        // Dispatch a custom event so other scripts know consent was updated
        const event = new CustomEvent('cookieConsentUpdated', { detail: state });
        window.dispatchEvent(event);

        hideBanner();
        hideModal();
        showFloatingBtn();
        
        // Example: Optional AJAX call to save to Django backend
        // saveToDjangoBackend(state);
    }

    /**
     * Apply consent (enable/disable scripts based on state)
     */
    function applyConsent(state) {
        if (!state) return;

        // Example: If analytics is enabled, load GA
        if (state.analytics) {
            // Load Analytics Script
            // console.log("Analytics enabled");
        } else {
            // console.log("Analytics disabled");
        }

        if (state.marketing) {
            // Load Marketing Script
            // console.log("Marketing enabled");
        }
    }

    /**
     * UI Actions
     */
    function showBanner() {
        if (els.banner) els.banner.classList.add('cc-active');
        if (els.floatingBtn) els.floatingBtn.classList.remove('cc-active');
    }

    function hideBanner() {
        if (els.banner) els.banner.classList.remove('cc-active');
    }

    function showModal() {
        if (els.modalOverlay) {
            els.modalOverlay.classList.add('cc-active');
            // Populate toggles based on current state or default
            const state = getConsentState() || DEFAULT_CONSENT;
            if (els.toggleAnalytics) els.toggleAnalytics.checked = state.analytics;
            if (els.toggleMarketing) els.toggleMarketing.checked = state.marketing;
            if (els.togglePreferences) els.togglePreferences.checked = state.preferences;
        }
    }

    function hideModal() {
        if (els.modalOverlay) els.modalOverlay.classList.remove('cc-active');
    }

    function showFloatingBtn() {
        if (els.floatingBtn) els.floatingBtn.classList.add('cc-active');
    }

    /**
     * Event Listeners
     */
    function attachEvents() {
        // Banner buttons
        if (els.btnAcceptAll) {
            els.btnAcceptAll.addEventListener('click', () => {
                const state = { necessary: true, analytics: true, marketing: true, preferences: true };
                saveConsentState(state);
                applyConsent(state);
            });
        }

        if (els.btnRejectAll) {
            els.btnRejectAll.addEventListener('click', () => {
                const state = { necessary: true, analytics: false, marketing: false, preferences: false };
                saveConsentState(state);
                applyConsent(state);
            });
        }

        if (els.btnCustomize) {
            els.btnCustomize.addEventListener('click', showModal);
        }

        // Modal buttons
        if (els.modalClose) {
            els.modalClose.addEventListener('click', hideModal);
        }

        if (els.btnSavePreferences) {
            els.btnSavePreferences.addEventListener('click', () => {
                const state = {
                    necessary: true,
                    analytics: els.toggleAnalytics ? els.toggleAnalytics.checked : false,
                    marketing: els.toggleMarketing ? els.toggleMarketing.checked : false,
                    preferences: els.togglePreferences ? els.togglePreferences.checked : false
                };
                saveConsentState(state);
                applyConsent(state);
            });
        }

        // Floating button
        if (els.floatingBtn) {
            els.floatingBtn.addEventListener('click', showModal);
        }

        // Close modal on clicking outside
        if (els.modalOverlay) {
            els.modalOverlay.addEventListener('click', (e) => {
                if (e.target === els.modalOverlay) hideModal();
            });
        }
    }

    /**
     * Initialization
     */
    function init() {
        // Cache DOM elements
        els = {
            banner: document.getElementById('cc-banner'),
            btnAcceptAll: document.getElementById('cc-btn-accept-all'),
            btnRejectAll: document.getElementById('cc-btn-reject-all'),
            btnCustomize: document.getElementById('cc-btn-customize'),
            modalOverlay: document.getElementById('cc-modal-overlay'),
            modalClose: document.getElementById('cc-modal-close'),
            btnSavePreferences: document.getElementById('cc-btn-save-preferences'),
            toggleAnalytics: document.getElementById('cc-toggle-analytics'),
            toggleMarketing: document.getElementById('cc-toggle-marketing'),
            togglePreferences: document.getElementById('cc-toggle-preferences'),
            floatingBtn: document.getElementById('cc-floating-btn')
        };

        const currentState = getConsentState();

        if (!currentState) {
            // No consent given, show banner
            // Delay slightly for smooth entrance animation
            setTimeout(showBanner, 500);
        } else {
            // Consent already given, apply it and show floating button
            applyConsent(currentState);
            showFloatingBtn();
        }

        attachEvents();
    }

    /**
     * Example Django AJAX Save (Optional)
     * If you want to log consent to a database.
     */
    function saveToDjangoBackend(state) {
        // Helper to get Django CSRF token from cookies
        const csrftoken = getCookie('csrftoken');
        if (!csrftoken) return;

        fetch('/api/save-cookie-consent/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(state)
        }).catch(err => console.error('Failed to save consent remotely', err));
    }

    // Public API
    return {
        init: init,
        getState: getConsentState,
        showPreferences: showModal
    };
})();

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', CookieConsent.init);
