# enforcement-mcp-parsers

Hardened parsers for SELinux, fapolicyd, MLS, and AIDE CLI output. Zero dependencies beyond pydantic.

Designed for consumption by MCP servers that need to parse security tool output from remote hosts over SSH. All parsers validate input size (10MB limit) and sanitize file paths (null byte rejection).

## Modules

- `parsers.selinux_cli` — getenforce, getsebool, sesearch, matchpathcon, semanage
- `parsers.ausearch` — AVC denials, FANOTIFY denials
- `parsers.fapolicyd_cli` — trust list, dump-db, rules
- `parsers.aide_cli` — AIDE check reports, config parsing
- `parsers.time_utils` — human time specs to ausearch format
- `parsers._hardening` — input validation, path sanitization

## Usage

```python
from enforcement_mcp_parsers import parse_avc_denials, parse_aide_check

denials = parse_avc_denials(ausearch_stdout)
report = parse_aide_check(aide_stdout)
```

## License

Apache-2.0
