 if command_name in commands_dict:
        return commands_dict[command_name]()
    return "Command not found"

print(invoke("start", {"start": lambda: "System started"}))