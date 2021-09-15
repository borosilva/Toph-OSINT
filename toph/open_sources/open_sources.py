from toph.open_sources.email_rep import email_rep

from toph.open_sources.facebook import facebook
from toph.open_sources.youtube import youtube
from toph.open_sources.pinterest import pinterest
from toph.open_sources.flickr import flickr
from toph.open_sources.medium import medium
from toph.open_sources.github import github
from toph.open_sources.about_me import about_me
from toph.open_sources.spotify import spotify
from toph.open_sources.telegram import telegram
from toph.open_sources.tiktok import tiktok

def searchOnAllOpenSourcesByEmail(email):
    email_rep.checkEmailRep(email)

def searchOnAllOpenSourcesByUsername(username):
    facebook.checkByUserName(username)
    youtube.checkByUserName(username)
    pinterest.checkByUserName(username)
    flickr.checkByUserName(username)
    medium.checkByUserName(username)
    github.checkByUserName(username)
    about_me.checkByUserName(username)
    spotify.checkByUserName(username)
    telegram.checkByUserName(username)
    tiktok.checkByUserName(username)