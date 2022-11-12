from pathlib import Path

from erdpy_accounts import Address
from erdpy_wallet import pem
from erdpy_wallet.generator import generate_pair


def generate_pem_file(pem_file: Path):
    secret_key, pubkey = generate_pair()
    address = Address(pubkey)
    pem.write(pem_file, secret_key, pubkey, name=address.bech32())