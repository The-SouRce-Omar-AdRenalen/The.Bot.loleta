from OmarMuSic.core.bot import Mody
from OmarMuSic.core.dir import dirr
from OmarMuSic.core.git import git
from OmarMuSic.core.userbot import Userbot
from OmarMuSic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Mody()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
