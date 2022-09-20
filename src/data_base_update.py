import os
import logging
from zipfile import ZipFile

import utils
from .defines import AVAILABLE_MODELS


class UpdateController:
    def __init__(self):
        self.model = None
        self.update_zip_archive = None
        self._exe_filename = "data_base_update.exe"

    def update(self) -> None:
        self.__choice_model()

        if not self.__check_emptiness():
            self.__print_message_and_exit(
                "Убедитесь, что флешка отформатирована и попробуйте снова."
            )

        self.update_zip_archive = utils.download_udpate_with_message(
            url=AVAILABLE_MODELS.get(),
            out=os.getcwd(),
            msg="Скачивание обновления баз данных: ",
        )

        if not self.__extract_update(os.getcwd()):
            # TODO: properly handle the exception.
            self.__print_message_and_exit(
                "Расспаковка архива не удалась. Обратитесь к инструкции."
            )

        if self.__delete_update_zip_archive():
            self.update_zip_archive = None

        self.__print_message_and_exit("Обновление успешно скачаны !")

    def __extract_update(self, out: str) -> bool:
        with ZipFile(self.update_zip_archive, "r") as archive:
            archive_content = archive.infolist()
            archive.extractall(out)

        successful_unpacking = True
        for file in archive_content:
            if not os.path.exists(file.filename):
                successful_unpacking = False
                break

        return successful_unpacking

    def __delete_update_zip_archive(self) -> bool:
        os.remove(self.update_zip_archive)
        return not os.path.exists(self.update_zip_archive)

    def __check_emptiness(self) -> bool:
        list_of_files = os.listdir(os.getcwd())
        if len(list_of_files) > 1:
            print("Флешка не отформатирована. Хотите отформатировать ?")
            print("1. Да.")
            print("2. Нет.")
            if int(input("Введите цифру, подтверждающую выбор и нажмите Enter: ")) == 1:
                list_of_files.remove(self._exe_filename)
                # TODO: This code is untested
                os.remove(list_of_files)
        # TODO: Add formatting functional
        return True

    def __choice_model(self) -> None:
        print("-- Поддерживаемые модели регистраторов:\n")

        for idx, model in enumerate(AVAILABLE_MODELS):
            if (idx + 1) == len(AVAILABLE_MODELS):
                print(f"{idx + 1}. {model}\n")
            else:
                print(f"{idx + 1}. {model}")

        while self.model is None:
            self.model = AVAILABLE_MODELS.get(
                list(AVAILABLE_MODELS.keys())[
                    int(
                        input(
                            '-- Введите порядковый номер, соответствующий вашей модели и нажмите "Enter": '
                        )
                    )
                    - 1
                ]
            )
            if self.model is None:
                print("Ввод выполнен неправильно. Попробуйте еще раз.")

        LOGGER.info(f'Выбрана модель: "{self.model}"')

    @staticmethod
    def __print_message_and_exit(message) -> None:
        LOGGER.info(message)
        LOGGER.info("Для закрытия окна, нажмите Enter...")
        input()
        exit(1)


def setup_logger():
    global LOGGER
    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO,
    )
    # TODO: read doc 'hint' about
    LOGGER = logging.getLogger(__name__)


def main() -> None:
    setup_logger()
    UpdateController().update()


if __name__ == "__main__":
    main()
