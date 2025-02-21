import xml.etree.ElementTree as ET
from lxml import etree

def update_xml_tags(xml_file, tags_1, tags_2, tags_3, new_last_activation_date, new_date, new_charging_contract_id):
    # Parse the XML file
    tree = etree.parse(xml_file)
    root = tree.getroot()

    # Update lastActivationDate
    last_activation_dates = root.findall(tags_1)
    if last_activation_dates:
        for last_activation_date in last_activation_dates:
            last_activation_date.text = new_last_activation_date
        print(f"Aggiornate {len(last_activation_dates)} occorrenze di lastActivationDate")
    else:
        print("Tag lastActivationDate non trovato")

    # Update date
    dates = root.findall(tags_2)
    if dates:
        for date in dates:
            date.text = new_date
        print(f"Aggiornate {len(dates)} occorrenze di date")
    else:
        print("Tag date non trovato")

    # Update chargingContractId
    charging_contract_ids = root.findall(tags_3)
    if charging_contract_ids:
        for charging_contract_id in charging_contract_ids:
            charging_contract_id.text = new_charging_contract_id
        print(f"Aggiornate {len(charging_contract_ids)} occorrenze di chargingContractId")
    else:
        print("Tag chargingContractId non trovato")

    # Save the modified XML
    tree.write(xml_file, encoding='utf-8', xml_declaration=False,pretty_print=True)

def print_current_values(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    print("Valori attuali:")
    for tag in ['lastActivationDate', 'date', 'chargingContractId']:
        elements = root.findall(f'.//{tag}')
        if elements:
            print(f"{tag}:")
            for i, elem in enumerate(elements, 1):
                print(f"  Occorrenza {i}: {elem.text}")
        else:
            print(f"{tag}: Non trovato")


def update_single_xml_tag(xml_file, tags, new_last_activation_date):
    # Parse the XML file
    tree = etree.parse(xml_file)
    
    root = tree.getroot()

    # Update lastActivationDate
    last_activation_dates = root.findall(tags)
    if last_activation_dates:
        for last_activation_date in last_activation_dates:
            last_activation_date.text = new_last_activation_date
        print(f"Aggiornate {len(last_activation_dates)} occorrenze di lastActivationDate")
    else:
        print("Tag lastActivationDate non trovato")
    
    # Save the modified XML
    tree.write(xml_file, encoding='utf-8', xml_declaration=False,pretty_print=True)