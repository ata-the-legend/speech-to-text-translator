#!/bin/bash

# Set the RabbitMQ management plugin URL
RABBITMQ_URL="http://broker:15672/api/nodes"

# Set the RabbitMQ username and password
RABBITMQ_USERNAME="guest"
RABBITMQ_PASSWORD="guest"

# Check if RabbitMQ is up and running
function check_rabbitmq() {
    local status=$(curl -s -u "$RABBITMQ_USERNAME:$RABBITMQ_PASSWORD" "$RABBITMQ_URL" | jq -r '.[0].running')
    if [ "$status" == "true" ]; then
        echo "RabbitMQ is up and running."
        return 0
    else
        echo "RabbitMQ is not running. Retrying in 2 seconds..."
        return 1
    fi
}

# Continuously check if RabbitMQ is running
while true; do
    check_rabbitmq
    if [ $? -eq 0 ]; then
        break
    fi
    sleep 2
done

exec "$@"