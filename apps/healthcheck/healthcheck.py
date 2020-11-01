"""AppDaemon healthcheck.

  @benleb / https://github.com/benleb/ad-healthcheck

healthcheck:
  module: healthcheck
  class: Healthcheck
  endpoint: healthcheck
"""

__version__ = "0.4.4"

from typing import Any, Dict, Optional, Tuple, Union

import hassapi as hass

APP_NAME = "Healthcheck"
APP_ICON = "🏥"


def hl(text: Union[int, float, str]) -> str:
    return f"\033[1m{text}\033[0m"


class Healthcheck(hass.Hass):  # type: ignore
    """Healthcheck."""

    def lg(self, msg: str, *args: Any, icon: Optional[str] = None, repeat: int = 1, **kwargs: Any) -> None:
        kwargs.setdefault("ascii_encode", False)
        message = f"{f'{icon} ' if icon else ' '}{msg}"
        _ = [self.log(message, *args, **kwargs) for _ in range(repeat)]

    async def initialize(self) -> None:
        """Register API endpoint."""
        endpoint = str(self.args.get("endpoint", APP_NAME))

        # register api endpoint
        await self.register_endpoint(self.healthcheck, endpoint)

        # show active config / init adutils
        self.lg("")
        self.lg(f"{hl(APP_NAME)} v{hl(__version__)}", icon=APP_ICON)
        self.lg("")
        self.lg(f"    endpoint: /{hl(endpoint)}")
        self.lg("")

    async def healthcheck(self, _: Any) -> Tuple[Dict[str, Any], int]:
        """Handle incoming requests."""
        modules = list(set([self.app_config[app]["module"] for app in self.app_config]))
        return dict(appdaemon=self.get_ad_version(), modules=modules), 200
