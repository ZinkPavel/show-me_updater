import os
import wget
from zipfile import ZipFile
import logging


class UpdateController:
    def __init__(self):
        self.available_models = dict({
            'combo_1': 'https://sho-me.ru/media/amk/downloads/database/archive/sho-me-combo-1-db.zip',
            'combo_1_a7': 'https://speedcam.online/rd.online/shome/combo_database.zip',
            'combo_1_signature (lexus)': 'https://.speedcamoninle/rshomed.online//shome3/combo_database.zip',
        })

        self.model = None
        self.update_zip_archive = None
        self._exe_filename = 'data_base_update.exe'

    def update(self) -> None:
        self.__choice_model()

        if not self.__check_emptiness():
            self.__print_message_and_exit('Убедитесь, что флешка отформатирована и попробуйте снова.')

        self.update_zip_archive = self.__download_update(out=os.getcwd())

        if not self.__extract_update(os.getcwd()):
            # TODO: properly handle the exception.
            self.__print_message_and_exit('Расспаковка архива не удалась. Обратитесь к инструкции.')

        if self.__delete_update_zip_archive():
            self.update_zip_archive = None

        self.__print_message_and_exit('Обновление успешно скачаны !')

    def __download_update(self, out: str) -> str:
        LOGGER.info('Скачивание обновления баз данных: ')
        update_zip = wget.download(url=self.available_models['combo_1_a7'], out=out)
        print('\n')  # wget.download does not add '\n'.
        return update_zip

    def __extract_update(self, out: str) -> bool:
        with ZipFile(self.update_zip_archive, 'r') as archive:
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
            print('Флешка не отформатирована. Хотите отформатировать ?')
            print('1. Да.')
            print('2. Нет.')
            if int(input('Введите цифру, подтверждающую выбор и нажмите Enter: ')) == 1:
                list_of_files.remove(self._exe_filename)
                # TODO: This code is untested
                os.remove(list_of_files)
        # TODO: Add formatting functional
        return True

    def __choice_model(self) -> None:
        print('-- Поддерживаемые модели регистраторов:\n')

        for idx, model in enumerate(self.available_models):
            if (idx + 1) == len(self.available_models):
                print(f'{idx + 1}. {model}\n')
            else:
                print(f'{idx + 1}. {model}')

        while self.model is None:
            self.model = self.available_models.get(
                list(self.available_models.keys())[
                    int(input('-- Введите порядковый номер, соответствующий вашей модели и нажмите "Enter": ')) - 1
                ]
            )
            if self.model is None:
                print('Ввод выполнен неправильно. Попробуйте еще раз.')

        LOGGER.info(f'Выбрана модель: "{self.model}"')

    @staticmethod
    def __print_message_and_exit(message) -> None:
        LOGGER.info(message)
        LOGGER.info('Для закрытия окна, нажмите Enter...')
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


if __name__ == '__main__':
    main()
