# midi-summer-school-analytics-on-fhir

## Open Codespaces (with options)
1. Click `< > Code`, select `Codespaces`, select `...` and `+ New with options...`
   ![](docs/codespace_with_options.png)
1. Under `Machine type`, select `4-core, 16 GB RAM, 32 GB`
   ![](docs/codespace_machine_type.png)
1. Click `Create Codespaces` and run the following commands there.


## Getting started

```sh
# this automatically starts a Pathling server and kicks-off the resource $import.
# run this without `--file compose.synthea.yaml` to avoid re-downloading trino and synthea cli
USER_ID=$(id -u) GROUP_ID=$(id -g) docker compose --file compose.yaml --file compose.synthea.yaml --env-file=.demo.env up warehousekeeper --attach-dependencies --abort-on-container-failure
# after the import is done, we no longer need the Pathling server itself
docker compose --env-file=.demo.env stop pathling
```

Cleanup when you're done:

```sh
docker compose --env-file=.demo.env down -v --remove-orphans
```

Install Python packages (Already done on GitHub Codespaces):

```sh
pip install --require-hashes -r requirements.txt
```

## Query the data

```sh
java -jar bin/trino.jar http://localhost:8080 --output-format=ALIGNED -f sql/table-counts.sql
```

## Superset

```sh
docker compose -f compose.superset.yaml up
```

On Codespaces, forward port `8088`:
![](docs/codespace-port-forward.png).

Open <http://localhost:8088/> and login as `admin` with password `admin`.

### Connect to Trino

1. `Settings` -> `Database Connections`
   ![](docs/superset-db-connections.png)
1. `+ Database`
   ![](docs/superset-add-database.png)
1. Under `Supported databases` select `Trino`
   ![](docs/superset-add-database-select-trino.png)
1. Copy and paste `trino://trino@trino:8080/` into the `SQLAlchemy URI` field. Click `Test connection`.
   ![](docs/superset-add-database-set-uri.png)
1. Click `Connect`

### Open SQL Lab

1. In the top-left hover over `SQL` and click `SQL Lab`
1. Copy and paste
   ```sql
   SELECT *
   FROM fhir.default.patient;
   ```
   And click `Run`.
