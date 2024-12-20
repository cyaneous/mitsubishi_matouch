"""Voluptuous schemas for mitsubishi_matouch."""

import voluptuous as vol

from homeassistant.const import CONF_MAC, CONF_PIN
from homeassistant.helpers import config_validation as cv

SCHEMA_USER = vol.Schema(
    {
        vol.Required(CONF_MAC): str,
        vol.Required(CONF_PIN, default=None): str,
    }
)

SCHEMA_BLUETOOTH = vol.Schema(
    {
        vol.Required(CONF_PIN, default=None): str,
    }
)