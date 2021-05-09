statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(statuses):
    count = 0
    for status in statuses.values():
        if status == 'online':
            count +=1
    return count

print(online_count(statuses))