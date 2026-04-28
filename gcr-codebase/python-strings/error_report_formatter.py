def format_errors(log):
    lines = log.split("\n")
    result = []
    
    for line in lines:
        if "ERROR" in line:
            line = line.replace("ERROR at line", "Error: line ").replace(":", " -")
        elif "WARNING" in line:
            line = line.replace("WARNING at line", "Warning: line ").replace(":", " -")
        result.append(line.strip())
    
    return "\n".join(result)

log = "ERROR at line12: missing ; \nWARNING at line15: unused variable"
print(format_errors(log))