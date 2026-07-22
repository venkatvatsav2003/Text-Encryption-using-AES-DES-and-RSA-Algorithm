#!/usr/bin/env bash
set -euo pipefail

VERSION="2.0.0"
KEYDIR="${KEYDIR:-./keys}"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'

usage() {
    cat <<EOF
CryptoShell v$VERSION — Encryption Toolkit (AES / 3DES / RSA)

Usage: $0 <algorithm> <operation> [data]

Algorithms:
  aes    AES-256-CBC (Fernet-compatible)
  des    TripleDES (24-byte key, CBC mode)
  rsa    RSA-2048 (OAEP SHA-256)

Operations:
  gen                    Generate a new key
  enc <data>             Encrypt data (reads stdin if omitted)
  dec <data>             Decrypt data

Options:
  -k, --key FILE         Custom key file
  -o, --out DIR          Key output directory (default: ./keys)
  -b, --bench            Run performance benchmarks
  -j, --json             JSON output
  -h, --help             Show this help

Examples:
  $0 aes gen
  $0 aes enc "Hello World"
  $0 rsa gen
  $0 rsa enc "Secret message"
  $0 des dec "base64_ciphertext"
  echo "data" | $0 aes enc
EOF
    exit 0
}

log_info()  { echo -e "${CYAN}[*]${NC} $1" >&2; }
log_ok()    { echo -e "${GREEN}[+]${NC} $1" >&2; }

ALGO="${1:-help}"; shift || true
OP="${1:-help}"; shift || true

case "$ALGO" in
    aes|aes-256|aes256)
        PY_ALGO="aes"
        case "$OP" in
            gen) python3 crypto.py aes-gen --json ${JSON:+--json} ;;
            enc) DATA="${1:-$(cat)}"; python3 crypto.py aes-enc "$DATA" ${KEY:+-k "$KEY"} ${JSON:+--json} ;;
            dec) DATA="${1:-$(cat)}"; python3 crypto.py aes-dec "$DATA" ${KEY:+-k "$KEY"} ${JSON:+--json} ;;
            *) usage ;;
        esac
        ;;
    des|3des|tripledes)
        case "$OP" in
            gen) python3 crypto.py des-gen --json ${JSON:+--json} ;;
            enc) DATA="${1:-$(cat)}"; python3 crypto.py des-enc "$DATA" ${KEY:+-k "$KEY"} ${JSON:+--json} ;;
            dec) DATA="${1:-$(cat)}"; python3 crypto.py des-dec "$DATA" ${KEY:+-k "$KEY"} ${JSON:+--json} ;;
            *) usage ;;
        esac
        ;;
    rsa)
        case "$OP" in
            gen) python3 crypto.py rsa-gen --json ${JSON:+--json} ;;
            enc) DATA="${1:-$(cat)}"; python3 crypto.py rsa-enc "$DATA" ${JSON:+--json} ;;
            dec) DATA="${1:-$(cat)}"; python3 crypto.py rsa-dec "$DATA" ${JSON:+--json} ;;
            *) usage ;;
        esac
        ;;
    bench|benchmark)
        log_info "Running cryptographic benchmarks..."
        python3 crypto.py benchmark
        ;;
    help|*) usage ;;
esac
