import subprocess

def run_command(command, timeout=60):
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        output_lines = []

        for line in process.stdout:
            print(line.strip())
            output_lines.append(line.strip())

        process.wait(timeout=timeout)

        return "\n".join(output_lines)

    except subprocess.TimeoutExpired:
        process.kill()
        return "[!] Command timed out"

    except Exception as e:
        return f"[ERROR] {str(e)}"
