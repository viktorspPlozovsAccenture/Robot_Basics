import xml.etree.ElementTree as ET

def analyze_xml_structure(xml_file):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        print("Detailed XML Structure:")
        print_detailed_structure(root)

        print("\nSearching for specific tags:")
        search_specific_tags(root)

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_detailed_structure(element, level=0):
    namespace = element.tag.split('}')[0] + '}' if '}' in element.tag else 'No namespace'
    tag_name = element.tag.split('}')[-1]
    print("  " * level + f"{namespace} : {tag_name}")
    for key, value in element.attrib.items():
        print("  " * (level + 1) + f"Attribute: {key} = {value}")
    if element.text and element.text.strip():
        print("  " * (level + 1) + f"Text: {element.text.strip()}")
    for child in element:
        print_detailed_structure(child, level + 1)

def search_specific_tags(root):
    tags_to_search = ['lastActivationDate', 'date', 'chargingContractId']
    
    for tag in tags_to_search:
        elements = root.findall(f".//*{tag}")
        elements.extend(root.findall(f".//*{{*}}{tag}"))  # Search with any namespace
        
        if elements:
            print(f"Found {len(elements)} occurrences of {tag}:")
            for elem in elements:
                print(f"  Full path: {get_xpath(elem)}")
                print(f"  Namespace: {elem.tag.split('}')[0] + '}' if '}' in elem.tag else 'No namespace'}")
                print(f"  Value: {elem.text}")
        else:
            print(f"Tag {tag} not found")

def get_xpath(element):
    path = []
    while element is not None:
        parent = element.find("..")
        if parent is not None:
            i = list(parent).index(element)
            namespace = element.tag.split('}')[0] + '}' if '}' in element.tag else ''
            tag_name = element.tag.split('}')[-1]
            path.append(f"{namespace}{tag_name}[{i+1}]")
        else:
            path.append(element.tag)
        element = parent
    return '/'.join(reversed(path))

# Usage
xml_file = 'C://WorkspaceNew//TELEPASS Project SAP BRIM//SP2A//qa-sap-rpa//Tests//Rigenerazione Canoni//request_1.xml'
analyze_xml_structure(xml_file)