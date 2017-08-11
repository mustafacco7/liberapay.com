from __future__ import absolute_import, division, print_function, unicode_literals

from liberapay.elsewhere._base import PlatformOAuth2
from liberapay.elsewhere._extractors import any_key, key
from liberapay.elsewhere._paginators import query_param_paginator


class Youtube(PlatformOAuth2):

    # Platform attributes
    based_on = 'google'
    name = 'youtube'
    display_name = 'Youtube'
    account_url = 'https://youtube.com/channel/{user_id}'
    optional_user_name = True
    user_type = 'channel'

    # Auth attributes
    auth_url = 'https://accounts.google.com/o/oauth2/auth?access_type=offline'
    access_token_url = 'https://accounts.google.com/o/oauth2/token'
    oauth_default_scope = ['https://www.googleapis.com/auth/youtube.readonly']

    # API attributes
    api_format = 'json'
    api_paginator = query_param_paginator('pageToken',
                                          next='nextPageToken',
                                          page='items',
                                          total=('pageInfo', 'totalResults'))
    api_url = 'https://www.googleapis.com/youtube/v3'
    api_user_info_path = '/channels?part=snippet&id={user_id}'
    api_user_self_info_path = '/channels?part=snippet&mine=true'
    api_friends_path = '/subscriptions?part=snippet&mine=true'
    api_search_path = '/search?part=snippet&type=channel&q={query}'

    # User info extractors
    x_user_info = key('items', clean=lambda o: o[0] if isinstance(o, list) and len(o) == 1 else o)
    x_user_id = any_key(('snippet', 'resourceId', 'channelId'), 'id')
    x_display_name = any_key(('snippet', 'title'))
    x_avatar_url = any_key(('snippet', 'thumbnails', 'medium', 'url'))
