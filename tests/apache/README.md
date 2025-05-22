# Apache

This directory contains files to test the redirects using a local Apache server run in a Docker container.

1. Make the config file

Run `/scripts/rdf2conf.py`. This remakes the `conf/pids.conf` file from all the RDF files.

2. Start Apache

Run `task aup`.

3. Test

To compare with current PID Proxy redirects, run `{PID-PROX-REPO}/apache/run-tests.py` with the `SERVER_ROOT_URL` variable set to the local Apache location running from Step 2. - likely `http://localhost:8080`.

To run current tests, run `python /tests/redirects_test.py`.

4. Stop Apache

Run `task adown`.