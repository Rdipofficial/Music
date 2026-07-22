import os
import time

# ── Telegram (non-sensitive — safe as defaults) ─────────────────────────────────
API_ID      = os.getenv("API_ID", "2040")
API_HASH    = os.getenv("API_HASH", "b18441a1ff607e10a989891a5462e627")
OWNER_ID    = int(os.getenv("OWNER_ID", "740397179"))
GROUP       = os.getenv("GROUP", "nub_coder_s")

# ── Sensitive — must be set via environment, no defaults ────────────────────────
BOT_TOKEN      = os.getenv("BOT_TOKEN", "8975766165:AAENEio15whYE0FmOObR8xVlFZ1x1hNsMto")
STRING_SESSION = os.getenv("STRING_SESSION", "BQFGMU4AoJIoI576_9ctxVTWo2Iy8YkRqtMfxKiv22vwlpzz2xE_I5_ZRuCGCEMILYiv5Q-kTtLirqT4GorSN1h7XHETnAwFuvxUVgmVygAHr2P-CWT0cFl3qfN_uDMFkUI9xRdB8EG1t6gpaXMbbzIcNWTBdb6UzJLngFTt6M8q1aK0OEtI72STkt--cvKSlxDI1vSKnxfp4vCx7uqzwFcykpay1ExkjulHmMlRY90g6dHvCuvwF2AvO0ujK5kOrj2_fawWglET8Yl69DHfvmw24TTBTs2ZQ8rU11tk9fzswGQHaIva7JAy6Lc9K-pYveDR6E2Gk2WfFp0Ct_B_HiDa2KGGXwAAAAH-pi3FAA")
MONGODB_URI    = os.getenv("MONGODB_URI", "mongodb+srv://TeleVault:TeleVault@televault.6kr2f9n.mongodb.net/?appName=TeleVault")
# ── Optional ──────────────────────────────────────────────────────────────────────
LOGGER_ID = os.getenv("LOGGER_ID", None)
DB_NAME   = os.getenv("DB_NAME", "musicbot")

# ── YouTube API ───────────────────────────────────────────────────────────────────
# Comma-separated list of YouTube Data API v3 keys.
# Get from https://console.cloud.google.com  (10K req/day free per key)
# Leave blank → yt-dlp only (no view counts / channel info from Data API)
YOUTUBE_API_KEYS = os.getenv("YOUTUBE_API_KEYS", "")

# External YouTube proxy (optional)
YT_API_TOKEN      = os.getenv("YT_API_TOKEN", "aEtl1oH4o5")
NUB_YT_API_BASE_URL = os.getenv("NUB_YT_API_BASE_URL", "http://api.nubcoders.com")

# ── Working directory / startup ───────────────────────────────────────────────────
ggg       = os.getcwd()
StartTime = time.time()
