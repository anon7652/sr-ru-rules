# Shadowrocket Russia Rules (sr-ru-rules)
#### **THIS IS NOT AN OFFICIAL REPO OF [russia-v2ray-rules-dat](https://github.com/runetfreedom/)**
##### AND IT IS HEAVILY RELIANT ON [runetfreedom/russia-v2ray-rules-dat](https://github.com/runetfreedom/russia-v2ray-rules-dat) AND [SagerNet/sing-box](https://github.com/SagerNet/sing-box)

### Purpose:
Periodically generate a new release containing rule-sets from [runetfreedom/russia-v2ray-rules-dat](https://github.com/runetfreedom/russia-v2ray-rules-dat), but converted to [Shadowrocket](https://shadowrocketvpn.com/) format.

### Example Shadowrocket config
This config assumes that GeoLite2 Databases for Shadowrocket are set to the following URLs:

COUNTRY: https://github.com/runetfreedom/russia-blocked-geoip/releases/latest/download/Country.mmdb<br>
ASN: https://github.com/runetfreedom/russia-blocked-geoip/releases/latest/download/Country-asn.mmdb

```
# Example Rules for Shadowrocket
[Rule]
RULE-SET,https://github.com/anon7652/sr-ru/rules/releases/latest/download/geosite-refilter.list,PROXY
RULE-SET,https://github.com/anon7652/sr-ru/rules/releases/latest/download/geosite-ru-blocked.list,PROXY
RULE-SET,https://github.com/anon7652/sr-ru/rules/releases/latest/download/geosite-ru-available-only-inside.list,DIRECT

GEOIP,RU,DIRECT
GEOIP,RE-FILTER,PROXY
GEOIP,RU-BLOCKED-COMMUNITY,PROXY
GEOIP,RU-BLOCKED,PROXY
GEOIP,PRIVATE,DIRECT

FINAL,PROXY
```
