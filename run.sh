#!/bin/env bash
python -m uvicorn loc_service.app:app --host 0.0.0.0  --port 8088 --timeout-keep-alive 4 --workers 10

# NOTE:
# - we want to hear from all (0.0.0.0) - we are in container!


# We do NOT want:
# --reload  # reloading for developers only! CI / CD  deployment does this for us


