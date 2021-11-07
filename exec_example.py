import subprocess

conf_timeout = 100
out_bytes = None

try:

    out_bytes = subprocess.check_output(['netstat', '-a'],
                                        timeout=conf_timeout,
                                        stderr=subprocess.STDOUT
                                        )

    # runs the command and gets its output in a form of a bytestream

    # print(type(out_bytes))
    # print(out_bytes)


except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode

except subprocess.TimeoutExpired as e:
    out_text = f"command timed out after {conf_timeout} seconds"

if out_bytes is not None:
    out_text = out_bytes.decode('utf-8')

print(out_text)
