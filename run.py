import sys

from cert_verifier.verifier import verify_certificate_file

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for cert_file in sys.argv[1:]:
            print(cert_file)
            result = verify_certificate_file(cert_file)
            print(result)
    else:
        result = verify_certificate_file('tests/data/2.0/valid.json')
        print(result)
