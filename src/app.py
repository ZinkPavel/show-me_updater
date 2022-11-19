from Updater import update
from VideoRegitstrator import VideoRegistrator


def main() -> None:
    video_registrator = VideoRegistrator()
    update(video_registrator=video_registrator)


if __name__ == "__main__":
    main()
