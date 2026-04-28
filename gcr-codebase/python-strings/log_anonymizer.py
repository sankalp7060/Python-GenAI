import re

def anonymize(log):
    log = re.sub(r'\S+@\S+', '[EMAIL_MASKED]', log)
    log = re.sub(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', '[IP_MASKED]', log)
    return log

print(anonymize("Error reported by user john.doe@corp.com from 192.168.0.21"))