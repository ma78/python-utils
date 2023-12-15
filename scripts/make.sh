#!/bin/bash

set -e

###
# FUNCTIONS
###

# make venv target
run_venv() {
  # Create venv
  if [ ! -d ".venv" ]; then
    python3 -m venv .venv
  fi

  # Activate venv
  source .venv/bin/activate

  # Upgrade pip
  pip install --upgrade pip

  # Install packages
  pip install -r requirements.txt

  # Finished
  echo
}

# make test target
run_test() {
  # Activate venv
  source .venv/bin/activate

  # Run tests
  coverage run -m pytest -v
  coverage xml -o reports/coverage.xml
  echo

  echo "COVERAGE REPORT:"
  coverage report

  # Finished
  echo
}


###
# MAIN
###

TASK="$1"
echo

# Perform task, default to "make test"
case $TASK in
  "venv" | "test" )
    run_$TASK;;

  *)
    run_test
esac

echo " * Done."
echo
