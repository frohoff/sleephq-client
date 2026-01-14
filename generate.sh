#!/bin/bash
set -e
cd "$(dirname "$0")"

echo "Fetching and fixing Swagger spec..."
curl -s https://sleephq.com/api/swagger.json | jq -f fix-spec.jq > swagger.json

echo "Converting Swagger 2.0 to OpenAPI 3.0..."
npx swagger2openapi -p swagger.json -o openapi.json

echo "Generating Python client..."
rm -rf src/sleephq
uv run openapi-python-client generate \
  --path openapi.json \
  --config openapi-config.yaml \
  --output-path generated \
  --meta none \
  --overwrite

mkdir -p src/sleephq
mv generated/* src/sleephq/
rm -rf generated swagger.json openapi.json

# Inject hand-written auth module
cp extras/auth.py src/sleephq/

# Add py.typed marker for PEP 561
touch src/sleephq/py.typed

# Add auth exports to __init__.py
cat >> src/sleephq/__init__.py << 'EOF'

# Hand-written auth helpers (injected by generate.sh)
from sleephq.auth import create_client as create_client
from sleephq.auth import TokenResponse as TokenResponse
from sleephq.auth import get_token as get_token
EOF

echo "Done! Run: uv sync"
