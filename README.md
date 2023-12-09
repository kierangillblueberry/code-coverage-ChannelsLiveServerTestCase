# code coverage reproduction

Reproduction for [django/channels/issues/2063](https://github.com/django/channels/issues/2063).

```
docker compose -f local.yml build
docker compose -f local.yml up -d

# Run using `LiveServerTestCase`. Code coverage is collected as expected.
sh coverage-live.sh

# Run using `ChannelsLiveServerTestCase`. Code coverage is not collected as expected.
sh coverage-channels.sh
```

I tried also adding different `concurrency` options in `.coveragerc` but was unable to find a setup that made coverage get collected.

## Another attempt

Also attempted manually editing `sitecustomize.py`

```
docker exec -t -i coverage_repro_local_django bash

# find site path
python -m site --user-site
/root/.local/lib/python3.11/site-packages
mkdir /root/.local/lib/python3.11/site-packages

# edit site path
vim /root/.local/lib/python3.11/site-packages/sitecustomize.py

    print("start: sitecustomize.py ")
    import coverage
    coverage.process_startup()

# exit docker container
exit

# rerun tests
sh coverage-channels.sh
start: sitecustomize.py 
start: sitecustomize.py 
Found 2 test(s).
Creating test database for alias 'default'...
...
```

This did not produce the correct coverage.