from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

LOGGER = {
    "path": str(Path(BASE_DIR / 'custom_logging/access.log')),
    "level": "info",
    "rotation": "20 days",
    "retention": "1 months"
}
