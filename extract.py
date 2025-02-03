import argparse, json, os, sys

def run():
    parser = argparse.ArgumentParser(
                        prog='eduroam-cert-extractor',
                        description='Get the certificate for UQ Eduroam for Android devices')
    parser.add_argument('filename', help='Name of .onc file for ChromeOS devices from cat.eduroam.org', nargs='?')
    args = parser.parse_args()
    if args.filename is None:
        path = input("Navigate to https://cat.eduroam.org/. Select The University of Queensland in the university dropdown. Select ChromeOS (in the 'Choose another installer...' menu) and drag the resulting .onc file to this window, and press enter.\n")
    else:
        path = args.filename
    extract(path)

def extract(path):
    path = path.strip()
    if path[-4:].lower() != '.onc':
        print("Invalid file type. Please make sure you downloaded the file for ChromeOS")
        sys.exit(1)
    with open(path, 'r') as f:
        filedata = json.load(f)
        cert = filedata["Certificates"][0]["X509"]
    with open(os.getcwd() + "/eduroam_quest.pem", "w") as fo:
        fo.write(cert)
    print(f"Wrote certificate to {os.getcwd() + '/eduroam_quest.pem'} - this can now be copied to Meta Quest or other Android device.")

if __name__ == "__main__":
    run()
