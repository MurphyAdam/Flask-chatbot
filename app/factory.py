import re
import bleach
from flask import url_for


def kill_html(text):
    tags = []
    attributes={}
    styles=[]
    # Nuke all html, scripts, etc
    text = bleach.clean(text, 
    	tags, 
    	attributes, 
    	styles, 
    	strip=False, 
    	strip_comments=True)
    return text


def is_empty(text):
    return False if (text and 
    	isinstance(text, str) and not 
    	text.isspace() and 
    	len(text) > 0) else True
