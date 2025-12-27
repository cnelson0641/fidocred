#!/usr/bin/env bash
set -eux

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"

$SCRIPT_DIR/_db_deploy_local.sh
$SCRIPT_DIR/_api_deploy_local.sh
