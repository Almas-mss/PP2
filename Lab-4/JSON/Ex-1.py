import json

def connection():
    with open("sample-data.json", "r") as file:
        fromFile = json.load(file)
        array = fromFile["imdata"]


        print("Interface Status")
        print("=" * 80)
        print(f"{'DN'.ljust(50)} {'Description'.ljust(20)} {'Speed'.ljust(8)} {'MTU'}")
        print("-" * 80)


        for item in array:
            attributes = item["l1PhysIf"]["attributes"]
            dn = attributes["dn"]
            description = attributes.get("descr", "")
            speed = attributes.get("speed", "")
            mtu = attributes.get("mtu", "")

            print(f"{dn.ljust(50)} {description.ljust(20)} {speed.ljust(8)} {mtu}")

connection()
