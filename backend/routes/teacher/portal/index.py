"""A portal for allowing teachers to see all classes."""

from flask import render_template, Response

from backend.route import Route
from backend.utils import authenticated


class TeacherPortal(Route):
    """A route for displaying classes."""

    name = "index"
    path = "/"

    @authenticated(user_type="teacher")  # skipcq: PYL-R0201
    def get(self) -> Response:
        """Display a portal page to the user."""
        return render_template("teacher/index.html")
