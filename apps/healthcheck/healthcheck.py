"""AppDaemon healthcheck.

  @benleb / https://github.com/benleb/appdaemon-healthcheck

healthcheck:
  module: healthcheck
  class: Healthcheck
  endpoint: healthcheck
"""

from typing import Any, Dict, Tuple

import adutils
import hassapi as hass

APP_NAME = "Healthcheck"
APP_ICON = "🏥"
APP_VERSION = "0.4.2"


class Healthcheck(hass.Hass):  # type: ignore
    """Healthcheck."""

    def initialize(self) -> None:
        """Register API endpoint."""
        self.cfg: Dict[str, Any] = dict()
        self.cfg["endpoint"] = str(self.args.get("endpoint", APP_NAME))

        # register api endpoint
        self.register_endpoint(self.healthcheck, self.cfg["endpoint"])

        # set prefix
        self.cfg.setdefault("_prefixes", dict(endpoint="/"))

        # init adutils
        self.adu = adutils.ADutils(
            APP_NAME, self.cfg, icon=APP_ICON, ad=self, show_config=True
        )

    def healthcheck(self, _: Any) -> Tuple[Dict[str, Any], int]:
        """Handle incoming requests."""
        modules = list(set([self.app_config[app]["module"] for app in self.app_config]))
        return dict(appdaemon=self.get_ad_version(), modules=modules), 200
