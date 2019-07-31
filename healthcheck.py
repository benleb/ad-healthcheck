"""AppDaemon healthcheck.

  @benleb / https://github.com/benleb/appdaemon-healthcheck

healthcheck:
  module: healthcheck
  class: Healthcheck
  endpoint: healthcheck
"""

from pprint import pformat

import appdaemon.plugins.hass.hassapi as hass

APP_NAME = "healthcheck"
APP_ICON = "🏥"


class Healthcheck(hass.Hass):
    """Healthcheck."""

    def initialize(self):
        """Register API endpoint."""
        self.config = dict()
        self.config["endpoint"] = str(self.args.get("endpoint", APP_NAME))
        self.register_endpoint(self.healthcheck, self.config["endpoint"])

        self.log(f"{APP_ICON} {APP_NAME}: {pformat(self.config)}", ascii_encode=False)

    def healthcheck(self, _):
        """Handle incoming requests."""
        return dict(appdaemon=self.get_ad_version(), app=APP_NAME), 200
