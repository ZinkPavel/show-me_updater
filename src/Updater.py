import os
import wget

import src.utils
from src.VideoRegitstrator import VideoRegistrator


def update(self, video_registrator: VideoRegistrator) -> None:
    if not utils.flash_card_is_empty():
        utils.print_message_and_exit(
            "Убедитесь, что флешка отформатирована и попробуйте снова."
        )

    archive = wget.download(
        url=video_registrator.update_link,
        out=os.getcwd(),
    )

    utils.extract_archive(archive=archive, outdir=os.getcwd())
    os.remove(archive)

    utils.print_message_and_exit("\nОбновление успешно скачаны !")
