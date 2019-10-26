import os
import fs
from fs import open_fs
import gnupg

gpg = gnupg.GPG(gnupghome="C:/hackathon/api/.gnupg")

home_fs = open_fs(".")