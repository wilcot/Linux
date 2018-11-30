# Distrobutions

| Name | Description | Based off Distro | Comments | 
| ---- | ----------- | --------------- | -------- |
| Ubuntu | Beginner fiendly distribution | Debian | Most popular Linux distribution |
| Debian | | |
| SUSE | Managed by Novell at one point. Enterprise offering with free openSUSE distro | |
| FreeBSD | | |
| Solaris | | |
| Linux Mint | | |
| Fedora | RedHat sponsored, developed by community | | Quick release cycles, shorter LTS (faster development) |
| Red Hat Enterprise Linux (RHEL) | Enterprise Linux Distrobution: expen$$ive! | Fedora | |
| CentOS | Community Enterprise Operating System | RHEL | Community based version of RHEL (via Fedora) |
| Amazon Linux | Built by Amazon to easily work with AWS | RHEL|

## Package Managers
2 different types of package managers:
**package managers**: handle installing of packages locally from a file. Define the archive type and how configuration on how to update a system. Example: RPM and APT

**meta packagers**: wrapper around package manager that allows packages to be downloaded and installed from external sources. Examples: Yum and apt-get


| Short Name | Full Name | Based on Package Manger | file types | 
| ---------- | --------- | ------ | ----- |
| rpm | Red Hat Package Manager | | .rpm |
| dpkg | Debian Package Management | | deb | 
| yum | Yellowdog Updater Modified / Your Update Manager | Wrapper around RPM | .rpm |
| apt-get | Advanced Package Tool | Wrapper around dpkg | deb |
| YaST | Yet another Setup Tool | | |

### Misc
- `yumdownloader` allows you to download packages from yum and store the rpm file locally on your computer.
`yumdownloader zsh -destdir downloads`
## Links
- [About Fedora, CentOs, RedHat](https://danielmiessler.com/study/fedora_redhat_centos/)
