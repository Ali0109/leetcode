
d = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "organization_ids": [],
}
temp_dict = {k: v for k, v in d.items() if k != 'organization_ids'}

print(temp_dict)
