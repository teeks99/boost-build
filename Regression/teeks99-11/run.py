#!/usr/bin/env python

# Copyright Rene Rivera 2007-2013
#
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import os.path
import shutil
import sys
import urllib

### ----------------------------- Unique --------------------------------------
# Needed for running on GCC build farm
import ssl

# Patch SSL to load correct cafile
debian_cafile='/etc/ssl/certs/ca-certificates.crt'

def patch_create_default_context(purpose=Purpose.SERVER_AUTH,
                           cafile=debian_cafile,
                           capath=None, cadata=None):
    """Create a SSLContext object with default settings.
    NOTE: The protocol and settings may change anytime without prior
          deprecation. The values represent a fair balance between maximum
          compatibility and security.
    """
    if not isinstance(purpose, _ASN1Object):
        raise TypeError(purpose)

    # SSLContext sets OP_NO_SSLv2, OP_NO_SSLv3, OP_NO_COMPRESSION,
    # OP_CIPHER_SERVER_PREFERENCE, OP_SINGLE_DH_USE and OP_SINGLE_ECDH_USE
    # by default.
    context = SSLContext(PROTOCOL_TLS)

    if purpose == Purpose.SERVER_AUTH:
        # verify certs and host name in client mode
        context.verify_mode = CERT_REQUIRED
        context.check_hostname = True
    elif purpose == Purpose.CLIENT_AUTH:
        context.set_ciphers(_RESTRICTED_SERVER_CIPHERS)

    if cafile or capath or cadata:
        context.load_verify_locations(cafile, capath, cadata)
    elif context.verify_mode != CERT_NONE:
        # no explicit cafile, capath or cadata but the verify mode is
        # CERT_OPTIONAL or CERT_REQUIRED. Let's try to load default system
        # root CA certificates for the given purpose. This may fail silently.
        context.load_default_certs(purpose)
    return context

keep_ssl_create_default_context = ssl.create_default_context
ssl.create_default_context = patch_create_default_context
### -----------------------------End Unique -----------------------------------

#~ Using --skip-script-download is useful to avoid repeated downloading of
#~ the regression scripts when doing the regression commands individually.
no_update_argument = "--skip-script-download"
no_update = no_update_argument in sys.argv
if no_update:
    del sys.argv[sys.argv.index(no_update_argument)]

use_local_argument = '--use-local'
use_local = use_local_argument in sys.argv
if use_local:
    del sys.argv[sys.argv.index(use_local_argument)]

#~ The directory this file is in.
if use_local:
    root = os.path.abspath(os.path.realpath(os.path.curdir))
else:
    root = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
print '# Running regressions in %s...' % root

script_sources = [ 'collect_and_upload_logs.py', 'process_jam_log.py', 'regression.py' ]
script_local = root
if use_local:
    script_remote = 'file://'+os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
else:
    script_remote = 'https://raw.githubusercontent.com/boostorg/regression/develop/testing/src'
script_dir = os.path.join(root,'boost_regression_src')

if not no_update:
    #~ Bootstrap.
    #~ * Clear out any old versions of the scripts
    print '# Creating regression scripts at %s...' % script_dir
    if os.path.exists(script_dir):
        shutil.rmtree(script_dir)
    os.mkdir(script_dir)
    #~ * Get new scripts, either from local working copy, or from remote
    if use_local and os.path.exists(script_local):
        print '# Copying regression scripts from %s...' % script_local
        for src in script_sources:
            shutil.copyfile( os.path.join(script_local,src), os.path.join(script_dir,src) )
    else:
        print '# Downloading regression scripts from %s...' % script_remote
        proxy = None
        for a in sys.argv[1:]:
            if a.startswith('--proxy='):
                proxy = {'https' : a.split('=')[1] }
                print '--- %s' %(proxy['https'])
                break
        for src in script_sources:
            #urllib.FancyURLopener(proxy).retrieve(
            urllib.FancyURLopener(proxy, context=tls_context).retrieve(
                '%s/%s' % (script_remote,src), os.path.join(script_dir,src) )

#~ * Make the scripts available to Python
sys.path.insert(0,os.path.join(root,'boost_regression_src'))

#~ Launch runner.
from regression import runner
runner(root)
