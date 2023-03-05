#!/bin/bash

if python -c 'import sys; assert sys.version_info >= (3,11)' > /dev/null; then

    # update necessary python resources at global level
    python -m pip install --upgrade setuptools wheel pip

    # setup and activate virtual environment
    python -m venv .venv
    source "./.venv/bin/activate" && python -m pip install --upgrade setuptools wheel pip

    if [ -f requirements.txt ]; then
        # install from requirements
        python -m pip install -r requirements.txt
    
    fi

else

    echo "python version should be >= 3.11"

fi
