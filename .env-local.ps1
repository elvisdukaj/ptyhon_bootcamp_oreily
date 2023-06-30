$pg_db_user = "postgres"
$pg_db_password = "postgres"
$pg_db_address = "localhost"
$pg_db_name = "postgres"
$pg_db_port = "5432"

$Env:pg_db_host = "postgresql+psycopg2://${db_user}:${db_password}@${db_address}:${db_port}/${db_name}"

Write-Output "db_host is ${Env:pg_db_host}"