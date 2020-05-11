from django.contrib.auth.models import User
from social.models import TextPost, ImagePost

def get_feed_data():
    '''Return a merged concatenation of all . no matter their type '''
    textposts = list(TextPost.objects.all())
    imageposts = list(ImagePost.objects.all())

    feed_data = textposts + imageposts
    return feed_data