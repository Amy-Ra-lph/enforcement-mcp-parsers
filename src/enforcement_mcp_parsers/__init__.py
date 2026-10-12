"""Hardened parsers for SELinux, fapolicyd, AIDE, and audit CLI output.

Zero-dependency beyond pydantic. Designed for consumption by any MCP server
that needs to parse security tool output from remote hosts.

All parsers validate input size (10MB limit) and sanitize paths
(null byte rejection) to handle untrusted remote command output.
"""

from .parsers import (
    InputTooLargeError,
    parse_aide_check,
    parse_aide_config,
    parse_avc_denials,
    parse_fanotify_denials,
    parse_fapolicyd_dumpdb,
    parse_fapolicyd_list,
    parse_fapolicyd_rules,
    parse_getenforce,
    parse_getsebool,
    parse_matchpathcon,
    parse_semanage_login,
    parse_sesearch_allow,
    parse_time_spec,
    sanitize_parsed_path,
    validate_input_size,
)
from .models import (
    AIDEChange,
    AIDEConfig,
    AIDEReport,
    MlsCategory,
    MlsFileLevel,
    MlsUserMapping,
)

__all__ = [
    "AIDEChange",
    "AIDEConfig",
    "AIDEReport",
    "InputTooLargeError",
    "MlsCategory",
    "MlsFileLevel",
    "MlsUserMapping",
    "parse_aide_check",
    "parse_aide_config",
    "parse_avc_denials",
    "parse_fanotify_denials",
    "parse_fapolicyd_dumpdb",
    "parse_fapolicyd_list",
    "parse_fapolicyd_rules",
    "parse_getenforce",
    "parse_getsebool",
    "parse_matchpathcon",
    "parse_semanage_login",
    "parse_sesearch_allow",
    "parse_time_spec",
    "sanitize_parsed_path",
    "validate_input_size",
]
