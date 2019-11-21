"""Entry point for Swot application."""

from backend.route_manager import RouteManager

manager = RouteManager()

if __name__ == "__main__":
    manager.run()
