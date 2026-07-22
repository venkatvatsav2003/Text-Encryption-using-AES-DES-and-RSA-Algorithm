#!/usr/bin/env bash

KEYDIR="./keys"
mkdir -p "$KEYDIR"

cmd="${1:-help}"
shift 2>/dev/null || true

case "$cmd" in
    aes-gen)
        openssl rand -base64 32 > "$KEYDIR/aes.key"
        echo "AES-256 key -> $KEYDIR/aes.key" ;;
    aes-enc)
        openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -pass file:"$KEYDIR/aes.key" -base64 <<< "$1" ;;
    aes-dec)
        openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -pass file:"$KEYDIR/aes.key" -base64 -d <<< "$1" ;;
    des-gen)
        openssl rand -base64 24 > "$KEYDIR/des.key"
        echo "3DES key -> $KEYDIR/des.key" ;;
    des-enc)
        openssl enc -des-ede3-cbc -pbkdf2 -iter 100000 -pass file:"$KEYDIR/des.key" -base64 <<< "$1" ;;
    des-dec)
        openssl enc -des-ede3-cbc -pbkdf2 -iter 100000 -pass file:"$KEYDIR/des.key" -base64 -d <<< "$1" ;;
    rsa-gen)
        openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out "$KEYDIR/rsa_priv.pem"
        openssl rsa -pubout -in "$KEYDIR/rsa_priv.pem" -out "$KEYDIR/rsa_pub.pem"
        echo "RSA-2048 keys -> $KEYDIR/rsa_priv.pem (private), $KEYDIR/rsa_pub.pem (public)" ;;
    rsa-enc)
        openssl pkeyutl -encrypt -pubin -inkey "$KEYDIR/rsa_pub.pem" <<< "$1" | base64 ;;
    rsa-dec)
        base64 -d <<< "$1" | openssl pkeyutl -decrypt -inkey "$KEYDIR/rsa_priv.pem" ;;
    *)
        echo "Usage: $0 {aes-gen|aes-enc|aes-dec|des-gen|des-enc|des-dec|rsa-gen|rsa-enc|rsa-dec} [data]"
        echo ""
        echo "  $0 aes-gen"
        echo "  $0 aes-enc 'Hello World'"
        echo "  $0 aes-dec 'U2FsdGVkX1...'"
        echo "  $0 rsa-gen"
        echo "  $0 rsa-enc 'Secret message'"
        echo "  $0 rsa-dec 'ciphertext_base64'"
        ;;
esac
