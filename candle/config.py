import yaml
import pathlib

# TODO make config file overridable

class Config:
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    content = yaml.load(open(f"{ROOT_DIR}/candle.yaml", encoding="utf-8"), Loader=yaml.FullLoader)

    def get_emojis(self):
        return self.content.get("emojis")
