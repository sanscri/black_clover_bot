from aiogram.utils.formatting import Text, TextLink, Bold, as_list, as_line
from settings import settings
def start_caption():
  return Text(as_list(as_line(Bold("")),
                        as_line(TextLink("Чат", url=settings.GROUP_URL), 
                                TextLink("Новости", url=settings.CHANNEL_URL), end="", sep="|"),
                        )).as_html()