FILE_CONTENTS = {

    "hostname.txt": [
        [
            "nox-machine",
            "Local hostname assigned during system initialization.",
            "Environment: development",
            "Machine role: workstation",
            "Hostname source: local configuration",
            "Status: active"
        ],
        [
            "investigator-deb",
            "Local hostname for the investigation workstation.",
            "Environment: laboratory",
            "Machine role: user workstation",
            "Hostname source: system configuration",
            "Status: active"
        ],
        [
            "lab-workstation",
            "Hostname assigned to the local laboratory machine.",
            "Environment: testing",
            "Machine role: general workstation",
            "Hostname source: local configuration",
            "Status: active"
        ]
    ],

    "hosts.txt": [
        [
            "# Local host configuration",
            "127.0.0.1 localhost",
            "127.0.1.1 nox-machine",
            "",
            "# IPv6 local addresses",
            "::1 localhost ip6-localhost ip6-loopback",
            "ff02::1 ip6-allnodes",
            "ff02::2 ip6-allrouters"
        ],
        [
            "# Hostname resolution table",
            "127.0.0.1 localhost",
            "127.0.1.1 investigator-deb",
            "",
            "# IPv6 configuration",
            "::1 localhost ip6-localhost ip6-loopback",
            "ff02::1 ip6-allnodes",
            "ff02::2 ip6-allrouters"
        ],
        [
            "# Local hosts",
            "127.0.0.1 localhost",
            "127.0.1.1 lab-workstation",
            "",
            "# Multicast addresses",
            "::1 localhost ip6-localhost ip6-loopback",
            "ff02::1 ip6-allnodes",
            "ff02::2 ip6-allrouters"
        ]
    ],

    "os-release.txt": [
        [
            "NAME=NoxOS",
            "VERSION=0.1",
            "ID=nox",
            "ID_LIKE=linux",
            "VERSION_ID=0.1",
            "PRETTY_NAME=NoxOS 0.1",
            "HOME_URL=https://nox.local/",
            "DOCUMENTATION_URL=https://docs.nox.local/",
            "SUPPORT_URL=https://support.nox.local/"
        ],
        [
            "NAME=NoxOS",
            "VERSION=0.2",
            "ID=nox",
            "ID_LIKE=linux",
            "VERSION_ID=0.2",
            "PRETTY_NAME=NoxOS 0.2",
            "HOME_URL=https://nox.local/",
            "DOCUMENTATION_URL=https://docs.nox.local/",
            "SUPPORT_URL=https://support.nox.local/"
        ],
        [
            "NAME=NoxOS",
            "VERSION=0.1-dev",
            "ID=nox",
            "ID_LIKE=linux",
            "VERSION_ID=0.1-dev",
            "PRETTY_NAME=NoxOS Development Environment",
            "BUILD_ID=development",
            "ENVIRONMENT=local-lab"
        ]
    ],

    "shells.txt": [
        [
            "# Available local shells",
            "/bin/noxsh",
            "",
            "# Default shell",
            "/bin/noxsh"
        ],
        [
            "# Shell configuration",
            "/bin/noxsh",
            "/bin/console",
            "",
            "# The default interactive shell is noxsh.",
            "/bin/noxsh"
        ],
        [
            "# Registered shells",
            "/bin/noxsh",
            "",
            "# Interactive environment",
            "# noxsh is the primary shell."
        ]
    ],

    "system-maintenance.txt": [
        [
            "# Weekly system maintenance",
            "# Check basic system state before maintenance.",
            "echo 'Starting weekly maintenance'",
            "echo 'Checking filesystem state'",
            "echo 'Checking system configuration'",
            "echo 'Checking available storage'",
            "echo 'Refreshing local status information'",
            "echo 'Weekly maintenance complete'",
            "",
            "# No external services are modified by this task."
        ],
        [
            "# Routine system maintenance",
            "# This task performs basic housekeeping.",
            "echo 'Beginning maintenance task'",
            "echo 'Reviewing filesystem'",
            "echo 'Reviewing system configuration'",
            "echo 'Checking temporary storage'",
            "echo 'Checking local logs'",
            "echo 'Updating maintenance timestamp'",
            "echo 'Maintenance finished successfully'"
        ],
        [
            "# Scheduled maintenance",
            "echo 'System maintenance started'",
            "echo 'Checking environment state'",
            "echo 'Checking storage usage'",
            "echo 'Checking recent system activity'",
            "echo 'Refreshing local information'",
            "echo 'System maintenance completed'",
            "",
            "# End of scheduled task"
        ]
    ],

    "log-cleanup.txt": [
        [
            "# Log cleanup task",
            "# Review local log storage.",
            "echo 'Starting log maintenance'",
            "echo 'Checking system logs'",
            "echo 'Checking authentication logs'",
            "echo 'Checking kernel logs'",
            "echo 'Checking available log storage'",
            "echo 'Removing expired temporary entries'",
            "echo 'Log maintenance complete'"
        ],
        [
            "# Routine log maintenance",
            "echo 'Beginning log review'",
            "echo 'Inspecting system log directory'",
            "echo 'Inspecting authentication records'",
            "echo 'Checking log file sizes'",
            "echo 'Checking for temporary records'",
            "echo 'Updating local log status'",
            "echo 'Log review completed successfully'"
        ],
        [
            "# Scheduled log cleanup",
            "# This task performs local housekeeping only.",
            "echo 'Checking old log data'",
            "echo 'Checking temporary records'",
            "echo 'Checking available storage'",
            "echo 'Cleaning expired temporary data'",
            "echo 'Recording cleanup result'",
            "echo 'Cleanup task finished'"
        ]
    ],

    "system-check.txt": [
        [
            "# Hourly system check",
            "echo 'Running hourly system check'",
            "echo 'Checking system availability'",
            "echo 'Checking filesystem state'",
            "echo 'Checking memory status'",
            "echo 'Checking local services'",
            "echo 'Checking system time'",
            "echo 'Hourly system check complete'"
        ],
        [
            "# Periodic health check",
            "echo 'Starting health check'",
            "echo 'Checking core environment'",
            "echo 'Checking active services'",
            "echo 'Checking filesystem access'",
            "echo 'Checking temporary storage'",
            "echo 'Checking current user session'",
            "echo 'Health check completed'"
        ],
        [
            "# Hourly environment check",
            "# Basic environment verification.",
            "echo 'Checking hostname'",
            "echo 'Checking filesystem'",
            "echo 'Checking system state'",
            "echo 'Checking available storage'",
            "echo 'Checking local configuration'",
            "echo 'Environment check complete'"
        ]
    ],

    "cleanup-temp.txt": [
        [
            "# Daily temporary file cleanup",
            "echo 'Starting temporary storage cleanup'",
            "echo 'Checking /tmp contents'",
            "echo 'Checking temporary session data'",
            "echo 'Checking expired temporary records'",
            "echo 'Removing expired entries'",
            "echo 'Temporary storage cleanup complete'"
        ],
        [
            "# Daily cleanup task",
            "echo 'Beginning daily cleanup'",
            "echo 'Reviewing temporary directory'",
            "echo 'Checking temporary storage usage'",
            "echo 'Removing expired temporary data'",
            "echo 'Verifying temporary directory state'",
            "echo 'Daily cleanup completed successfully'"
        ],
        [
            "# Temporary storage maintenance",
            "# Remove only temporary data that is no longer required.",
            "echo 'Scanning temporary storage'",
            "echo 'Checking session files'",
            "echo 'Checking expired data'",
            "echo 'Cleaning temporary entries'",
            "echo 'Verifying cleanup result'",
            "echo 'Maintenance finished'"
        ]
    ],

    "session.tmp": [
        [
            "# Temporary interactive session",
            "Session ID: local-001",
            "User: investigator",
            "Terminal: noxsh",
            "Working directory: /home/user",
            "Session state: active",
            "Last command: ls",
            "Environment: local"
        ],
        [
            "# Temporary session state",
            "Session ID: console-002",
            "User: investigator",
            "Terminal: noxsh",
            "Working directory: /home/user/Documents",
            "Session state: active",
            "Last command: pwd",
            "Environment: development"
        ],
        [
            "# Console session information",
            "Session ID: lab-003",
            "User: user",
            "Terminal: noxsh",
            "Working directory: /",
            "Session state: initialized",
            "Last command: help",
            "Environment: simulation"
        ]
    ],

    "system.log": [
        [
            "[INFO] System initialization started",
            "[INFO] Loading filesystem",
            "[INFO] Reading system configuration",
            "[INFO] Initializing environment",
            "[INFO] Loading local user configuration",
            "[INFO] Starting system services",
            "[INFO] Checking temporary storage",
            "[INFO] System initialization complete",
            "[INFO] Interactive environment ready",
            "[INFO] User session available"
        ],
        [
            "[INFO] Boot sequence started",
            "[INFO] Kernel environment loaded",
            "[INFO] Filesystem initialized",
            "[INFO] System configuration loaded",
            "[INFO] Local services initialized",
            "[INFO] Runtime environment ready",
            "[INFO] User environment loaded",
            "[INFO] Startup checks completed",
            "[INFO] System ready"
        ],
        [
            "[INFO] Starting local environment",
            "[INFO] Loading configuration files",
            "[INFO] Mounting simulated filesystem",
            "[INFO] Initializing runtime",
            "[INFO] Preparing user environment",
            "[INFO] Checking system state",
            "[INFO] Startup sequence completed",
            "[INFO] Environment is ready for use"
        ]
    ],

    "kernel.log": [
        [
            "[INFO] Kernel initialization started",
            "[INFO] Memory manager initialized",
            "[INFO] Process scheduler initialized",
            "[INFO] Device manager initialized",
            "[INFO] Filesystem interface initialized",
            "[INFO] System timer initialized",
            "[INFO] Scheduler started",
            "[INFO] Kernel initialization complete"
        ],
        [
            "[INFO] Kernel startup sequence beginning",
            "[INFO] Loading core subsystems",
            "[INFO] Initializing memory subsystem",
            "[INFO] Initializing process subsystem",
            "[INFO] Initializing filesystem subsystem",
            "[INFO] Initializing system clock",
            "[INFO] Core subsystems ready",
            "[INFO] Kernel ready"
        ],
        [
            "[INFO] Kernel loaded",
            "[INFO] Runtime environment detected",
            "[INFO] Memory subsystem ready",
            "[INFO] Scheduler ready",
            "[INFO] Device interface ready",
            "[INFO] Filesystem interface ready",
            "[INFO] System calls initialized",
            "[INFO] Kernel startup complete"
        ]
    ],

    "auth.log": [
        [
            "[INFO] Authentication subsystem initialized",
            "[INFO] Local login requested",
            "[INFO] User: investigator",
            "[INFO] Authentication successful",
            "[INFO] Session created",
            "[INFO] Working directory: /home/user",
            "[INFO] User environment loaded",
            "[INFO] Login completed successfully"
        ],
        [
            "[INFO] Authentication service started",
            "[INFO] Login attempt received",
            "[INFO] Account: investigator",
            "[INFO] Local authentication accepted",
            "[INFO] Session opened",
            "[INFO] User configuration loaded",
            "[INFO] Login session ready"
        ],
        [
            "[INFO] Local authentication initialized",
            "[INFO] Login request received",
            "[INFO] User credentials accepted",
            "[INFO] User session initialized",
            "[INFO] Default directory assigned: /home/user",
            "[INFO] Shell environment loaded",
            "[INFO] Authentication sequence complete"
        ]
    ],

    "readme.txt": [
        [
            "Welcome to the Nox environment.",
            "",
            "This directory contains shared documentation and information.",
            "The environment is designed as a small local system simulation.",
            "",
            "Available shell commands include:",
            "  pwd",
            "  cd",
            "  ls",
            "  cat",
            "  help",
            "  report",
            "  exit",
            "",
            "Use 'ls' to inspect directories and 'cat' to read files.",
            "Use 'help' to view available shell commands.",
            "",
            "End of document."
        ],
        [
            "NoxOS Development Environment",
            "============================",
            "",
            "This system is a local filesystem simulation.",
            "It provides a small Linux-like environment for experimentation.",
            "",
            "Basic navigation:",
            "  pwd     Show the current directory",
            "  cd      Change directory",
            "  ls      List directory contents",
            "  cat     Display file contents",
            "  help    Display command information",
            "  report  Start the reporting process",
            "  exit    End game"
            "",
            "Please keep experimental files organized.",
            "This environment is intended for educational use."
        ],
        [
            "Welcome.",
            "",
            "The local environment has been initialized successfully.",
            "You are currently operating inside the simulated filesystem.",
            "",
            "Useful commands:",
            "pwd",
            "ls",
            "cd <directory>",
            "cat <file>",
            "help",
            "report",
            "exit"
            "Explore the filesystem carefully.",
            "Configuration and documentation can be found under /etc and /usr/share."
        ]
    ],

    "license.txt": [
        [
            "NoxOS Simulation License",
            "Version 0.1",
            "",
            "Copyright (c) Nox Project",
            "",
            "This software is provided for educational and experimental use.",
            "Permission is granted to inspect, modify, and experiment with",
            "the simulated environment.",
            "",
            "This environment is provided without warranty.",
            "Use it responsibly."
        ],
        [
            "Nox Environment License",
            "Development Release",
            "",
            "This software is intended for learning, experimentation,",
            "and development purposes.",
            "",
            "The environment may contain incomplete or experimental",
            "components.",
            "",
            "No guarantee of functionality or compatibility is provided."
        ],
        [
            "NoxOS Experimental Software",
            "",
            "Release channel: development",
            "Intended use: educational and experimental",
            "",
            "Users may modify the simulated environment for learning",
            "and testing purposes.",
            "",
            "This software is provided as-is."
        ]
    ],

    "notes.txt": [
        [
            "Lab Notes",
            "=========",
            "",
            "Remember to check the cron configuration.",
            "Review system logs periodically.",
            "Keep the lab environment organized.",
            "",
            "Current tasks:",
            "- Review system configuration",
            "- Inspect recent logs",
            "- Check available storage",
            "- Document important changes",
            "",
            "General reminder:",
            "Do not modify configuration files without recording the change."
        ],
        [
            "Investigation Notes",
            "==================",
            "",
            "The local environment appears to be functioning normally.",
            "Filesystem initialization completed successfully.",
            "",
            "Things to check:",
            "- System logs",
            "- Authentication records",
            "- Temporary files",
            "- User configuration",
            "- Scheduled maintenance",
            "",
            "Next review:",
            "Check /var/log after the next system session."
        ],
        [
            "Things to Remember",
            "==================",
            "",
            "Finish the network setup.",
            "Review the current environment.",
            "Document important configuration changes.",
            "Check whether scheduled maintenance completed.",
            "",
            "Useful locations:",
            "/etc      System configuration",
            "/var/log  System logs",
            "/home     User files",
            "/tmp      Temporary data",
            "/usr/share Shared documentation"
        ]
    ],

    "settings.conf": [
        [
            "# Nox shell configuration",
            "",
            "theme=dark",
            "shell=noxsh",
            "show_hidden=false",
            "sort_entries=true",
            "show_directories=true",
            "confirm_exit=true",
            "history_enabled=true",
            "prompt_style=default",
            "",
            "# End of configuration"
        ],
        [
            "# User environment settings",
            "",
            "theme=dark",
            "shell=noxsh",
            "show_hidden=true",
            "sort_entries=true",
            "show_directories=true",
            "confirm_exit=false",
            "history_enabled=true",
            "prompt_style=minimal",
            "",
            "# Hidden files are currently visible."
        ],
        [
            "# Local shell preferences",
            "",
            "theme=default",
            "shell=noxsh",
            "show_hidden=false",
            "sort_entries=true",
            "show_directories=true",
            "confirm_exit=true",
            "history_enabled=true",
            "prompt_style=default",
            "",
            "# Default user preferences are active."
        ]
    ],

    "investigator.txt": [
        [
            "# User scheduled tasks",
            "# No user-defined tasks are currently configured.",
            "",
            "# Scheduled task storage initialized.",
            "# Entries may be added by the local user."
        ],
        [
            "# User crontab",
            "",
            "# No active user schedules.",
            "# This file is intentionally empty."
        ],
        [
            "# Local scheduled tasks",
            "",
            "# User has not configured any recurring tasks.",
            "# System maintenance tasks are stored separately."
        ]
    ],
    ".profile": [
        [
            "# Nox user profile",
            "# Loaded when the user session starts.",
            "",
            "export USER=investigator",
            "export HOME=/home/user",
            "export SHELL=/bin/noxsh",
            "export EDITOR=nano",
            "",
            "# Default working environment",
            "export PATH=/bin:/usr/bin",
            "",
            "# Profile initialization complete."
        ],
        [
            "# User environment configuration",
            "",
            "export USER=investigator",
            "export HOME=/home/user",
            "export SHELL=/bin/noxsh",
            "export TERM=nox-terminal",
            "",
            "# Session preferences",
            "export PAGER=cat",
            "export EDITOR=nano",
            "",
            "# End of profile"
        ],
        [
            "# Local login profile",
            "# Basic environment variables for interactive sessions.",
            "",
            "export USER=user",
            "export HOME=/home/user",
            "export SHELL=/bin/noxsh",
            "export TERM=nox-terminal",
            "",
            "# Default command search path",
            "export PATH=/bin:/usr/bin",
            "",
            "# Interactive session ready."
        ]
    ],
    
    "package-index.txt": [
        [
            "# Local package cache",
            "# Generated package information.",
            "",
            "core-utils 1.0 installed",
            "nox-shell 0.1 installed",
            "filesystem-tools 1.2 installed",
            "network-tools 0.8 installed",
            "",
            "# Cache status",
            "Last update: system-startup",
            "Status: valid"
        ],
        [
            "# Cached package information",
            "",
            "core-utils 1.1 installed",
            "nox-shell 0.2 installed",
            "filesystem-tools 1.2 installed",
            "text-tools 0.9 installed",
            "",
            "Package index loaded successfully.",
            "Cache state: current"
        ],
        [
            "# Package index cache",
            "",
            "core-utils 1.0",
            "filesystem-tools 1.1",
            "nox-shell 0.1",
            "network-tools 0.8",
            "",
            "Index entries: 4",
            "Cache verification: passed"
        ]
    ],

    "system-state.txt": [
        [
            "# Cached system state",
            "hostname=nox-machine",
            "environment=development",
            "filesystem=ready",
            "services=running",
            "user-session=active",
            "last-check=successful",
            "cache-status=valid"
        ],
        [
            "# System state cache",
            "hostname=investigator-deb",
            "environment=laboratory",
            "filesystem=ready",
            "services=running",
            "user-session=active",
            "last-check=successful",
            "cache-status=current"
        ],
        [
            "# Cached environment information",
            "hostname=lab-workstation",
            "environment=testing",
            "filesystem=ready",
            "services=initialized",
            "user-session=ready",
            "last-check=successful",
            "cache-status=valid"
        ]
        ],

    "user-cache.txt": [
        [
            "# User environment cache",
            "user=investigator",
            "home=/home/user",
            "shell=/bin/noxsh",
            "last-directory=/home/user",
            "theme=dark",
            "hidden-files=false",
            "status=loaded"
        ],
        [
            "# Cached user preferences",
            "user=investigator",
            "home=/home/user",
            "shell=/bin/noxsh",
            "last-directory=/home/user/Documents",
            "theme=dark",
            "hidden-files=true",
            "status=loaded"
        ],
        [
            "# Local user cache",
            "user=user",
            "home=/home/user",
            "shell=/bin/noxsh",
            "last-directory=/home/user",
            "theme=default",
            "hidden-files=false",
            "status=initialized"
        ]
    ],



}
