#!/usr/bin/env python
# -*- coding:utf-8 -*-
############################################
# File Name: discuz_feature.py
# Purpose:
# Creation Date: 2017-01-05
# Last Modified: 2017-01-05 13:02:38
# Actor by: Suluo - sampson.suluo@gmail.com
############################################

import logging
import logging.handlers
import traceback
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


matches = {
    'robots_for_Xx':[
        "Disallow: /forum.php?mod=rediret*",
        "Disallow: /forum.php?mod=post*",
        "Disallow: /forum.php?mod=spacecp*",
        "Disallow: /forum.php?mod=app&*",
        "Disallow: /forum.php?mod=misc*",
        "Disallow: /forum.php?mod=attachment*",
        "Disallow: /forum.php?mod=yes*"
    ],
    'robots_for_xx':[
        "Disallow: /forumdata/",
        "Disallow: /ipddata/",
        "Disallow: /modcp/",
        "Disallow: /wap/",
        "Disallow: /ajax.php",
        "Disallow: /logging.php",
        "Disallow: /memcp.php",
        "Disallow: /my.php",
        "Disallow: /pm.php",
        "Disallow: /post.php",
        "Disallow: /rss.php",
        "Disallow: /seccode.php",
        "Disallow: /topicadmin.php",
        "Disallow: /space.php",
        "Disallow: /modcp.php"
    ],
    'intext':[
        '<p>Powered by <strong><a href="http://www.discuz.net" target="_blank">Discuz!</a></strong> ',
        '<p class="xs0">&copy; 2001-2009 <ahref="http://www.comsenz.com" target="_blank">Comsenz Inc.</a></p>'
    ],
    'meta':[
        'Discuz!',
        'Comsenz'
    ]
}

def main(argv):
    pass

if __name__ == "__main__":
    main(argv)


