"""
mkdocs-macros-plugin main file
"""

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
