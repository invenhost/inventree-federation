"""Share specific stock items and inventory stats between plugin users ."""

from plugin import InvenTreePlugin
from plugin.mixins import (
    NavigationMixin,
    SettingsContentMixin,
    UrlsMixin,
)


class FederationPlugin(
    UrlsMixin, NavigationMixin, SettingsContentMixin, InvenTreePlugin
):
    """Share specific stock items and inventory stats between plugin users ."""

    NAME = "inventree_federation"
    SLUG = "inventree_federation"
    TITLE = "InvenTree Federation"
    MIN_VERSION = "0.13.0"

    def your_function_here(self):
        """Do something."""
        pass
