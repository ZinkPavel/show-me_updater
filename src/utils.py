import os
import shutil
import sys
from zipfile import ZipFile

EXE_FILENAME = "update.exe"


def print_message_and_exit(message) -> None:
    input()
    sys.exit(0)


def flash_card_is_empty() -> bool:
    list_of_files = os.listdir(os.getcwd())
    if len(list_of_files) > 1:
        print("Флешка не отформатирована. Хотите отформатировать ?\n")
        print("1. Да.")
        print("2. Нет.")
        if int(input("\nВведите цифру, подтверждающую выбор и нажмите Enter: ")) == 1:
            list_of_files.remove(EXE_FILENAME)
            map(
                lambda f: shutil.rmtree(f) if os.path.isdir(f) else os.remove(),
                list_of_files,
            )
        else:
            return False
    return True


def extract_archive(archive: str, outdir: str):
    with ZipFile(archive, "r") as a:
        archive_content = a.infolist()
        a.extractall(out)
