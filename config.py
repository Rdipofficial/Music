import os
import time

# ── Telegram (non-sensitive — safe as defaults) ─────────────────────────────────
API_ID      = os.getenv("API_ID", "2040")
API_HASH    = os.getenv("API_HASH", "b18441a1ff607e10a989891a5462e627")
OWNER_ID    = int(os.getenv("OWNER_ID", "6076474757"))
GROUP       = os.getenv("GROUP", "nub_coder_s")

# ── Sensitive — must be set via environment, no defaults ────────────────────────
BOT_TOKEN      = os.getenv("BOT_TOKEN", "8975766165:AAENEio15whYE0FmOObR8xVlFZ1x1hNsMto")
STRING_SESSION = os.getenv("STRING_SESSION", "BQFGMU4AQYjaTl5KGFywai_fk4ILzgKy0h66BURPla6j92kyov_G2WtBBcKmzfdETS9fiQHM5QKc3J5azp16PGsyCiFu1wXvVJIE_ln4xHfQxxFr-cVku47xSMSYW4jHakdXZbqF2i_ia92nfNEt4vUXg80Hvh5rB76qwokhOIsd6YnpCUkfoa7700FgROyc0k1clNlD373JXGwVk9r3LhbbXws7aS67zdppk8k2rpTnxcJFewKUcTO3ztMQZffSFszodsxgJArLlWObrU_vuO5wnv366nj267zJdqThLrl_6mirIvSDpIegjGVoIa6130ZwS2t_-cdf-GZGV72O2Bjf-UxMygAAAAH-pi3FAA")
MONGODB_URI    = os.getenv("MONGODB_URI", "mongodb+srv://nubcoders:nubcoders@music.8rxlsum.mongodb.net/?retryWrites=true&w=majority&appName=music")

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
