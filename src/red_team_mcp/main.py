#!/usr/bin/env python3
"""
Main entry point for Red Team MCP Server.

This module provides the main function to start the FastMCP server.
"""
import argparse
import sys
from .fastmcp_server import app


def main():
    """Main entry point to start the MCP server."""
    parser = argparse.ArgumentParser(description="Red Team MCP Server")
    parser.add_argument(
        "--host", "-H",
        default="127.0.0.1",
        help="Host or IP to bind (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port", "-P",
        type=int,
        default=5678,
        help="TCP port for the MCP server (default: 5678)"
    )
    parser.add_argument(
        "--debug", "-d",
        action="store_true",
        help="Enable debug logging"
    )
    parser.add_argument(
        "--transport",
        default="stdio",
        choices=["stdio", "streamable-http"],
        help="Transport protocol to use (default: stdio)"
    )
    args = parser.parse_args()

    if args.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG)

    if args.transport == "stdio":
        print(f"[MCP Server] Starting in stdio mode", file=sys.stderr)
        app.run(transport="stdio")
    else:
        print(f"[MCP Server] Listening on {args.host}:{args.port} (streamable-http transport)", file=sys.stderr)
        app.run(transport="streamable-http", host=args.host, port=args.port)


if __name__ == "__main__":
    main()