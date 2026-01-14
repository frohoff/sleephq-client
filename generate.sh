#!/bin/bash
set -e
cd "$(dirname "$0")"

curl -s https://sleephq.com/api/swagger.json | jq -f fix-spec.jq > swagger.json

docker run --rm -v "$PWD:/local" openapitools/openapi-generator-cli generate \
  -i /local/swagger.json -g python -o /local/generated \
  --package-name sleephq --skip-validate-spec \
  --additional-properties=packageVersion=0.1.0 >/dev/null 2>&1

rm -rf src/sleephq docs tests README.md
mv generated/sleephq src/
mv generated/docs generated/README.md .
mv generated/test tests
sed -i 's|http://sleephq|https://sleephq|g' src/sleephq/configuration.py
rm -rf generated swagger.json

# Inject hand-written auth module
cp extras/auth.py src/sleephq/

# Add auth exports to __init__.py
cat >> src/sleephq/__init__.py << 'EOF'

# Hand-written auth helpers (injected by generate.sh)
from sleephq.auth import Client as Client
from sleephq.auth import TokenResponse as TokenResponse
from sleephq.auth import get_token as get_token

__all__ += ["Client", "TokenResponse", "get_token"]
EOF

echo "Done! Run: uv sync"
