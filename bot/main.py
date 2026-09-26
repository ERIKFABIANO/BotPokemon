import logging

from bot.core.config import get_settings
from bot.core.webhook_server import create_app

settings = get_settings()
logging.basicConfig(level=settings.log_level)

app = create_app()
