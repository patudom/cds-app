from traitlets import Unicode

from ipywwt import WWTWidget


class HubbleWWTWidget(WWTWidget):

    background = Unicode(
        "Black Sky Background",
        help="The layer to show in the background (`str`)",
    ).tag(wwt=None, wwt_reset=True)

    foreground = Unicode(
        "SDSS9 color",
        help="The layer to show in the foreground (`str`)",
    ).tag(wwt=None, wwt_reset=True)

    SURVEYS_URL = "https://gist.githubusercontent.com/Carifio24/447d69e14a3196665fa3cb59f93ec0ee/raw/040cb93508c47284b44435c413e3fc92dc601f2d/surveys_minimal.wtml"


    def __init__(self, *args, **kwargs):
        super().__init__(surveys_url=self.SURVEYS_URL, *args, **kwargs)
