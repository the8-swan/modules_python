import sys


def function():
    """Function that  display the system header, collect user input
    for archivist ID and status report, then output messages using the correct
     streams: standard messages via sys.stdout and alerts via sys.stderr."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print("")
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    idar = sys.stdin.readline().strip()
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status = sys.stdin.readline().strip()
    print("")

    sys.stdout.write(
        f"[STANDARD] Archive status from {idar}: {status}\n")
    sys.stderr.write(
                "[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("")
    sys.stdout.write("Three-channel communication test successful.\n")


function()
