docker exec -t -i coverage_repro_local_django sh -c 'coverage erase'

docker exec -t -i coverage_repro_local_django sh -c "DATABASE_URL=postgres://YKeyITyVKJmGQBSFocVhacJTxZbSgtjt:AoZV2HeFGw5sf0o2UNSpzvhrJzKgiGz0MiZgezxJBBuZDq0GaqYvVMLNWgeZeID3@postgres:5432/coverage_repro COVERAGE_PROCESS_START=/app/.coveragerc DJANGO_SETTINGS_MODULE=config.settings.local coverage run --source='.' manage.py test --tag=live-server-test-case --parallel --noinput"

docker exec -t -i coverage_repro_local_django sh -c 'coverage combine'

docker exec -t -i coverage_repro_local_django sh -c 'coverage html'