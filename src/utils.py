import logging
import wget

from .defines import AVAILABLE_MODELS

global logger
logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def download_udpate_with_message(url=None: str, out=None: str, msg=None: str) -> str:
    if not url:
        raise(RuntimeErro('Incorrect argument "url". Try again.'))

    if not out:
        raise(RuntimeErro('Incorrect argument "out". Try again.'))

    logger.info(msg or "")
    update_zip = wget.download(url=url, out=out)
    print("\n")  # wget.download does not add '\n'.
    return update_zip
