from VCSProjectParser import VCSProjectParser


def main():
    parser = VCSProjectParser()
    parser.load_project(r'C:/work/OWLNext_git/VS10/OWLNext_10.vcxproj')
    parser.parse_data()
    if parser.parse_data():
        for f in parser.iipr.files:
            print(f.attrib['type'],':', f.path)


if __name__ == '__main__':
    main()
