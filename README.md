# pymysql-json-cli

## install

```sh
pip install pymysql-json-cli
```

## usage

```sh
cat << EOF |
SHOW DATABASES;
EOF
pymysql-json
# [{"Database": "information_schema"}, {"Database": "test"}]
```

```sh
cat <<EOF |
SELECT *
FROM %(table_name)s
EOF
pymysql-json --args '{"table_name": "test_table"}'
# [{"test_column": "arg_value"}, {"test_column": "test_value"}]
```

```sh
echo "SHOW DATABASES;" > db.sql
pymysql-json --sqlfile ./db.sql
# [{"Database": "information_schema"}, {"Database": "test"}]
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