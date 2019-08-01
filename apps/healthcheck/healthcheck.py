"""AppDaemon healthcheck.

  @benleb / https://github.com/benleb/appdaemon-healthcheck

healthcheck:
  module: healthcheck
  class: Healthcheck
  endpoint: healthcheck
"""

import appdaemon.plugins.hass.hassapi as hass

import adutils

APP_NAME = "healthcheck"
APP_ICON = "🏥"


class Healthcheck(hass.Hass):
    """Healthcheck."""

    def initialize(self):
        """Register API endpoint."""
        self.cfg = dict()
        self.cfg["endpoint"] = str(self.args.get("endpoint", APP_NAME))

        # register api endpoint
        self.register_endpoint(self.healthcheck, self.cfg["endpoint"])

        # output app configuration
        adutils.show_info(self.log, APP_NAME, self.cfg, list(), icon=APP_ICON)

    def healthcheck(self, _):
        """Handle incoming requests."""
        modules = list(set([self.app_config[app]["module"] for app in self.app_config]))
        return dict(appdaemon=self.get_ad_version(), modules=modules), 200
