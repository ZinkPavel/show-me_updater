from urllib import request

from src.utils import print_message_and_exit


class VideoRegistrator:
    AVAILABLE_MODELS = dict(
        {
            "combo_1": "https://sho-me.ru/media/amk/downloads/database/archive/sho-me-combo-1-db.zip",
            "combo_1_a7": "https://speedcam.online/rd.online/shome/combo_database.zip",
            "combo_1_signature (lexus)": "https://speedcam.online/rd.online/shome/shome3/combo_database.zip",
        }
    )

    def __init__(self, model: int = None) -> None:
        self.model = model or self.choice_model()
        self.update_link = __class__.AVAILABLE_MODELS.get(self.model)

        _validate()

    def choice_model(self) -> None:
        for idx, model in enumerate(__class__.AVAILABLE_MODELS):
            print(
                f"{idx + 1}. {model}\n"
                if (idx + 1) == len(__class__.AVAILABLE_MODELS)
                else f"{idx + 1}. {model}"
            )

        while self.model is None:
            self.model = list(__class__.AVAILABLE_MODELS.keys())[int(input()) - 1]

    def _validate(self) -> None:
        try:
            request.urlopen(self.update_link)
        except request.URLError(ex) as ex:
            print_message_and_exit(f"URL: {self.update_link} not available.")
