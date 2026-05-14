import subprocess

def execute_commands(commands: list) -> list:
    seen = set()
    results = []

    for cmd in commands:
        if cmd in seen:
            continue
        seen.add(cmd)

        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True
            )
            results.append({
                cmd: {
                    "output": result.stdout.strip(),
                    "error": result.stderr.strip(),
                    "status": "success" if result.returncode == 0 else "Failed"
                }
            })
        except Exception as e:
            results.append({
                cmd: {
                    "output": "",
                    "error": str(e),
                    "status": "Failed"
                }
            })

    return results


# --- Main ---
if __name__ == "__main__":
    commands = ["ls", "pwd", "df", "ls", "invalidcmd123"]  # 'ls' is duplicate
    output = execute_commands(commands)

    import json
    print(json.dumps(output, indent=4))