"""
mkdocs-macros-plugin main file
"""

import math

DEFAULT_WPM = 265  # Medium says they use 275 WPM but they actually use 265
TIME_DURATION_UNITS = (
    ("week", 60*60*24*7),
    ("day", 60*60*24),
    ("hour", 60*60),
    ("min", 60),
    ("sec", 1)
)

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    """
    Returns a YouTube embed

    Usage:

    {{ youtube_embed("dQw4w9WgXcQ") }}
    """
    @env.macro
    def youtube_embed(
        url: str,
        div_class="iframe-container",
        iframe_class="responsive-iframe",
        frameborder="0",
        allow="accelerometer; autoplay; encrypted-media; gyroscope;\
  picture-in-picture",
    ) -> str:
        return f"<div class=\"{div_class}\">\
  <iframe\
  class=\"{iframe_class}\"\
  frameborder=\"{frameborder}\"\
  allow=\"accelerometer; autoplay; encrypted-media; gyroscope;\
  picture-in-picture\"\
  allowfullscreen\
  src=\"https://www.youtube.com/embed/{url}\"></iframe>\
</div>"

    """
    Gets read time based on word count

    Credit to:
    https://github.com/alanhamlett/readtime/blob/master/readtime/utils.py
    Copyright: (c) 2016 by Alan Hamlett.
    Licence (BSD): https://github.com/alanhamlett/readtime/blob/master/LICENSE
    """
    @env.macro
    def readtime_as_seconds(num_words: int, images=0, wpm=None) -> int:
        """Returns the read time as seconds of some plain text.

        :param num_words: Number of words in plain text.
        :param images: The number of inline images in the text.
        """

        if not wpm:
            wpm = DEFAULT_WPM
        
        seconds = int(math.ceil(num_words / wpm * 60))

        # add extra seconds for inline images
        delta = 12
        for img in range(images):
            seconds += delta
            if delta > 3:
                delta -= 1

        return seconds
    
    """
    Displays the Words and Reading Time section in the Releases
    """
    @env.macro
    def words_format(word_count: int, images: int) -> str:
        reading_time = readtime_as_seconds(word_count, images)

        return f"_Words: {word_count:,}_\n\n\
_Reading Time: {human_readable_time(reading_time)}_"

""" --- Local functions --- """

"""
Get human-readable time
From here: https://gist.github.com/borgstrom/936ca741e885a1438c374824efb038b3
"""
def human_readable_time(seconds):
    if seconds == 0:
        return "inf"

    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'.format(amount, unit, "" if amount == 1 else "s"))

    return ", ".join(parts)
