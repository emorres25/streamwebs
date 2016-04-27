export POSTGRES_HOST=`getent hosts postgres | awk '{ print $1 }'`
