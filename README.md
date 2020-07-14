# pymysql-json-cli

## install

```sh
pip install pymysql-json-cli
```

## usage

```sh
cat << EOF |
SHOW TABLES;
EOF
pymysql-json
```

```sh
cat <<EOF |
SELECT *
FROM %(table_name)s
EOF
pymysql-json --args '{"table_name": "performance_schema"}'
```

## development

- Need
  - cargo-make
  - docker

### lint & test

```sh
makers --env-file .env.test tests
```

### lint except python code

```sh
makers --env-file .env.test lints
```