def stop_process_by_pid(pid):
    import os
    import signal
    try:
        os.kill(pid, signal.SIGINT)
        print(f"Process with PID {pid} stopped with interrupt signal (Ctrl+C) successfully.")
    except ProcessLookupError:
        print(f"Error: Process with PID {pid} not found.")
    except Exception as e:
        print(f"Error sending interrupt signal to process with PID {pid}: {e}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <pid>")
        sys.exit(1)

    pid_to_stop = sys.argv[1]

    try:
        pid_to_stop = int(pid_to_stop)
    except ValueError:
        print("Error: PID must be an integer.")
        sys.exit(1)

    stop_process_by_pid(pid_to_stop)
