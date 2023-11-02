#!/bin/env bash
python -m uvicorn loc_service.app:app --host 0.0.0.0 --port 8088 --loop asyncio --timeout-keep-alive 4 --workers 2 --reload

# NOTE:
# APP loc_service.app:app
# --timeout-keep-alive 4 is the time limit
# --loop [auto|asyncio|uvloop]  # we want asyncio as we use it!

# We do not want currently in dev:

# --workers <int> (# of workers)  # in dev 1 is enought

# --log-config <path>  --log-config <path> - Logging configuration file. Options: dictConfig() formats: .json, .yaml. Any other format will be processed with fileConfig(). Set the formatters.default.use_colors and formatters.access.use_colors values to override the auto-detected behavior.
#    If you wish to use a YAML file for your logging config, you will need to include PyYAML as a dependency for your project or install uvicorn with the [standard] optional extras.

# --no-use-colors  # for log processing better no colors

# --log-level info OR debug # for production

# --http httptools # Set the HTTP protocol implementation. The httptools implementation provides greater performance, but it not compatible with PyPy. Options: 'auto', 'h11', 'httptools'. Default: 'auto'

# --no-server-header ?

# --no-date-header ?

# SSL config by:
#--ssl-keyfile <path> - The SSL key file.
#--ssl-keyfile-password <str> - The password to decrypt the ssl key.
#--ssl-certfile <path> - The SSL certificate file.
#--ssl-version <int> - The SSL version to use.
#--ssl-cert-reqs <int> - Whether client certificate is required.
#--ssl-ca-certs <str> - The CA certificates file.
#--ssl-ciphers <str> - The ciphers to use.



