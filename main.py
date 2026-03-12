import subprocess
import sys
import pytest
from multiprocessing import Process
import argparse


def run_mcp_server():
    """Start the MCP server (blocking)."""
    subprocess.run([sys.executable, "mcp_server/server.py"])


def run_tests():
    """Run pytest suite with reports."""
    pytest.main(["tests/", "--alluredir=reports/"])


def run_both():
    """Run MCP server and tests together using multiprocessing."""
    # Start MCP server in a separate process
    server_process = Process(target=run_mcp_server)
    server_process.start()

    try:
        # Run tests in the main process
        run_tests()
    finally:
        # Stop the server after tests complete
        server_process.terminate()
        server_process.join()


def main():
    parser = argparse.ArgumentParser(description="Playwright AI Framework")
    parser.add_argument("--server", action="store_true", help="Run MCP server")
    parser.add_argument("--tests", action="store_true", help="Run tests")
    parser.add_argument("--both", action="store_true", help="Run MCP server and tests together")

    args = parser.parse_args()

    if args.both:
        run_both()
    elif args.server:
        run_mcp_server()
    elif args.tests:
        run_tests()
    else:
        # Interactive mode if no args
        print("=== Playwright AI Framework ===")
        print("Options:")
        print("1. Run MCP server")
        print("2. Run tests")
        print("3. Run MCP server + tests together")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            run_mcp_server()
        elif choice == "2":
            run_tests()
        elif choice == "3":
            run_both()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
