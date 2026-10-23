"""Default configuration for Halyard.

Values here can be overridden in halyard.yml or with CLI flags.
"""

DEFAULTS = {
    # Seconds before a single file scan is abandoned
    "timeout": 60,
    # How many directory levels deep to scan
    "max_depth": 8,
    # Supported output formats
    "formats": ["text", "json", "sarif"],
    # Default output format
    "format": "text",
    # Glob patterns skipped by default
    "exclude": ["node_modules/**", ".git/**", "*.min.js"],
    # Minimum severity reported: low, medium, high, critical
    "min_severity": "medium",
}

CONFIG_FILE = "halyard.yml"
