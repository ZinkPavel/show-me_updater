import logging
import wget

from defines import AVAILABLE_MODELS

global logger
logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def download_file_with_message(
    url: str = None,
    out: str = None,
    msg: str = None,
) -> str:
    if not url:
        raise (RuntimeError('Incorrect argument "url". Try again.'))

    if not out:
        raise (RuntimeError('Incorrect argument "out". Try again.'))

    logger.info(msg or "")
    file_path = wget.download(url=url, out=out)
    logger.info("")

    return file_path
