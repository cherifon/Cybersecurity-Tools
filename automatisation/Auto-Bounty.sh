#!/bin/bash

# Colors for better readability
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

# ASCII Art for Auto Bounty branding
ascii_art() {
    echo -e "${CYAN}"
    echo "  ___        _             ______                   _         "
    echo " / _ \      | |            | ___ \                 | |        "
    echo "/ /_\ \_   _| |_ ___ ______| |_/ / ___  _   _ _ __ | |_ _   _ "
    echo "|  _  | | | | __/ _ \______| ___ \/ _ \| | | | '_ \| __| | | |"
    echo "| | | | |_| | || (_) |     | |_/ / (_) | |_| | | | | |_| |_| |"
    echo "\_| |_/\__,_|\__\___/      \____/ \___/ \__,_|_| |_|\__|\__, |"
    echo "                                                         __/ |"
    echo "                 Made by Cherif Jebali                  |___/ "
    echo -e "${NC}"
}

# Check if URL is provided
if [ -z "$1" ]; then
    ascii_art
    echo -e "${RED}Usage: ./Auto-Bounty.sh <target-url>${NC}"
    exit 1
fi

TARGET=$1
LOG_DIR="$TARGET/logs"
RECON_DIR="$TARGET/recon"
SCAN_DIR="$TARGET/scan"

# Create necessary directories
mkdir -p "$RECON_DIR" "$SCAN_DIR" "$LOG_DIR"

# Function to check if a command exists
check_command() {
    command -v "$1" >/dev/null 2>&1 || { echo -e "${RED}Error: The tool '$1' is not installed.${NC}"; exit 1; }
}

# Check for required tools before execution
check_tools() {
    tools=("sublist3r" "amass" "nmap" "nuclei" "gobuster" "sqlmap" "subjack" "python3")
    for tool in "${tools[@]}"; do
        check_command "$tool"
    done
}

# Function to run reconnaissance
run_recon() {
    echo -e "${CYAN}[*] Starting reconnaissance on $TARGET${NC}"

    echo -e "${GREEN}[1] Subdomain enumeration with Sublist3r${NC}"
    sublist3r -d "$TARGET" -o "$RECON_DIR/subdomains.txt" | tee "$LOG_DIR/sublist3r.log"

    echo -e "${GREEN}[2] Subdomain enumeration with Amass${NC}"
    amass enum -d "$TARGET" -o "$RECON_DIR/amass_subdomains.txt" | tee -a "$LOG_DIR/amass.log"

    echo -e "${CYAN}Reconnaissance completed.${NC}"
}

# Function to perform vulnerability scans
run_scan() {
    echo -e "${CYAN}[*] Starting vulnerability scans on $TARGET${NC}"

    echo -e "${GREEN}[1] Port scanning with Nmap${NC}"
    nmap -sV -p- "$TARGET" -oN "$SCAN_DIR/nmap_scan.txt" | tee "$LOG_DIR/nmap.log"

    echo -e "${GREEN}[2] Vulnerability scanning with Nuclei${NC}"
    nuclei -u "$TARGET" -t ~/nuclei-templates/ -o "$SCAN_DIR/nuclei_scan.txt" | tee -a "$LOG_DIR/nuclei.log"

    echo -e "${GREEN}[3] Directory and file discovery with Gobuster${NC}"
    gobuster dir -u "$TARGET" -w /usr/share/wordlists/dirb/common.txt -o "$SCAN_DIR/gobuster.txt" | tee -a "$LOG_DIR/gobuster.log"

    echo -e "${GREEN}[4] SQL injection testing with SQLmap${NC}"
    sqlmap -u "$TARGET" --batch --crawl=2 --output-dir="$SCAN_DIR/sqlmap" | tee -a "$LOG_DIR/sqlmap.log"

    echo -e "${CYAN}Scanning completed.${NC}"
}

# Function to check for subdomain takeovers
run_subdomain_takeover() {
    echo -e "${CYAN}[*] Checking for subdomain takeovers${NC}"

    echo -e "${GREEN}[1] Analyzing with Subjack${NC}"
    subjack -w "$RECON_DIR/subdomains.txt" -t 100 -timeout 30 -ssl -o "$SCAN_DIR/subjack_takeover.txt" -v | tee "$LOG_DIR/subjack.log"

    echo -e "${CYAN}Subdomain takeover check completed.${NC}"
}

# Function to exploit vulnerabilities
run_exploit() {
    echo -e "${CYAN}[*] Starting vulnerability exploitation${NC}"

    echo -e "${GREEN}[1] XSS testing with XSStrike${NC}"
    if [ ! -d "XSStrike" ]; then
        echo -e "${RED}XSStrike is not installed. Clone it from https://github.com/s0md3v/XSStrike.${NC}"
        return
    fi
    cd XSStrike || exit
    python3 xsstrike.py -u "$TARGET" --crawl --skip --log-file "$SCAN_DIR/xsstrike_xss.txt" | tee "$LOG_DIR/xsstrike.log"
    cd - || exit

    echo -e "${CYAN}Exploitation completed.${NC}"
}

# Main Menu
ascii_art
echo -e "${CYAN}Target: $TARGET${NC}"
echo "-----------------------------------"
PS3='Select an option: '
options=("Reconnaissance" "Vulnerability Scanning" "Subdomain Takeover" "Exploitation" "Run All" "Quit")
select opt in "${options[@]}"; do
    case $opt in
        "Reconnaissance")
            run_recon
            ;;
        "Vulnerability Scanning")
            run_scan
            ;;
        "Subdomain Takeover")
            run_subdomain_takeover
            ;;
        "Exploitation")
            run_exploit
            ;;
        "Run All")
            run_recon
            run_scan
            run_subdomain_takeover
            run_exploit
            ;;
        "Quit")
            echo -e "${GREEN}Exiting Auto Bounty. Goodbye!${NC}"
            break
            ;;
        *) echo -e "${RED}Invalid option. Try again.${NC}";;
    esac
done
