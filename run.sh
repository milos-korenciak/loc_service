#!/bin/env bash
python -m uvicorn loc_service.app:app --host 0.0.0.0 --port 8088 --loop asyncio --timeout-keep-alive 4 --workers 10

# NOTE:
# APP loc_service.app:app
# --timeout-keep-alive 4 is the time limit
# - we want to hear from all (0.0.0.0) - we are in container!
# --loop [auto|asyncio|uvloop]  # we want asyncio as we use it!


# We do NOT want:
# --reload  # reloading for developers only! CI / CD  deployment does this for us


