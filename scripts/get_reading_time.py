"""
Install `readtime` if you haven't got it
> pip install readtime

Reading Time calculation:
seconds = num_words / 265 * 60 + img_weight * num_images

WPM is 265 by default
"""

import count_words

total_words = count_words.get_tut_words()

