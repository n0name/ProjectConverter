from Importers.VCSProjectImporter import VCSProjectImporter


def main():
    parser = VCSProjectImporter()
    parser.load_project(r'C:/work/OWLNext_git/VS10/OWLNext_10.vcxproj')
    parser.parse_data()
    if parser.parse_data():
        for f in parser.iipr.files:
            print(f.attrib['type'], ':', f.path)
            if "exclude_from" in f.attrib and len(f.attrib["exclude_from"]) > 0:
                print('\t-\texcluded in : ', f.attrib["exclude_from"])

        for c in parser.iipr.configurations:
            print("Configuration: ", c.name)
            for name, param in c.params.items():
                print('\t-\t', name, ":", param)


if __name__ == '__main__':
    main()
