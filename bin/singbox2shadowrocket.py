# Largely based off of this issue https://github.com/runetfreedom/russia-v2ray-rules-dat/issues/10 @Master-Yoba
# https://github.com/Master-Yoba/shadowrocket-rules

import datetime
import glob
import json
import os

# Prepare conversion dict
conversion_dict = {
    'domain': 'DOMAIN',
    'domain_suffix': 'DOMAIN-SUFFIX',
    'domain_regex': 'URL-REGEX',
    'domain_keyword': 'DOMAIN-KEYWORD',
    'ip_cidr': 'IP-CIDR'
}


# read in JSON file and translate it to the Shadowrocket format
def parse_ruleset(source_file):
    header_totals = ""
    sr_list_file = ""
    total_count = 0

    with open(source_file) as f:
        ruleset = json.load(f)

    for item in ruleset['rules']:
        for rule_type, rule_value in item.items():
            if isinstance(rule_value, str):
                header_totals += f"# {conversion_dict[rule_type]}: 1\n"
                total_count += 1
                sr_list_file += f"{conversion_dict[rule_type]},{rule_value}\n"
            else:
                header_totals += f"# {conversion_dict[rule_type]}: {len(rule_value)}\n"
                total_count += len(rule_value)
                for element in rule_value:
                    sr_list_file += f"{conversion_dict[rule_type]},{element}\n"
        header_totals += f"# TOTAL: {total_count}\n"

    return(header_totals+sr_list_file)


def main():
    # get paths to all JSON files from sing-box
    files = glob.glob(f"sing-box-json/*.json")

    for source_file in files:
        # [:-5] to remove ".json" extension
        name = os.path.basename(source_file)[:-5]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Add notes on converion (source name, rule type, date)
        header =  f'''# NAME: {name}
# UPDATED: {timestamp}
'''
        shadowrocket_list_file = header
        
        shadowrocket_list_file += parse_ruleset(source_file)
        
        with open(os.path.join(f"sr-lists/{name}.list"), 'w') as f:
            f.write(shadowrocket_list_file)

        print(f"Converted {source_file} to sr-lists/{name}.list!")


if __name__ == "__main__":
    main()
