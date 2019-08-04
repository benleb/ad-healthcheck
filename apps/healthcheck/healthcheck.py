"""AppDaemon healthcheck.

  @benleb / https://github.com/benleb/appdaemon-healthcheck

healthcheck:
  module: healthcheck
  class: Healthcheck
  endpoint: healthcheck
"""

from typing import Any, Dict, Tuple

import appdaemon.plugins.hass.hassapi as hass

import adutils

APP_NAME = "Healthcheck"
APP_ICON = "🏥"


class Healthcheck(hass.Hass):  # type: ignore
    """Healthcheck."""

    def initialize(self) -> None:
        """Register API endpoint."""
        self.cfg: Dict[str, str] = dict()
        self.cfg["endpoint"] = str(self.args.get("endpoint", APP_NAME))

        # register api endpoint
        self.register_endpoint(self.healthcheck, self.cfg["endpoint"])

        # output app configuration
        adutils.show_info(self.log, APP_NAME, self.cfg, list(), icon=APP_ICON)

    def healthcheck(self, _: Any) -> Tuple[Dict[str, Any], int]:
        """Handle incoming requests."""
        modules = list(set([self.app_config[app]["module"] for app in self.app_config]))
        return dict(appdaemon=self.get_ad_version(), modules=modules), 200
