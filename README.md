![image (5)](https://github.com/user-attachments/assets/8aa8c3e0-d13a-41f8-84bb-f6b083e7eac0)
# SOC & DFIR Roadmap
## Introduction
I know—you’ve seen countless roadmaps for starting a cybersecurity career. But let’s face it: any path can get you there if you stick with it.

Here’s my suggested route to help you stay on track and avoid getting lost.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
## Zero Level: Building the Foundation

If you're starting out in cybersecurity, you've probably heard you need to know a bit of everything. But to really excel, it's essential to understand how systems work from all angles—grasp the basics, how data moves across networks, and get to know operating systems inside out. It’s not everything, but it's where you should start. Check out the next sections to dive deeper.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
## 1. Introduction to Cybersecurity
- **Goal**: Understand the basics of cybersecurity, including fundamental concepts, terminology, and the overall landscape.
- **Resources**:
    - **Free**:
        - [Introduction to Cyber Security - FutureLearn](https://www.futurelearn.com/courses/introduction-to-cyber-security) (Free Course)
        - [Cybersecurity Essentials - Cisco Networking Academy](https://www.netacad.com/courses/cybersecurity/cybersecurity-essentials) (Free with Registration)
- **Practice**:
    - Complete beginner challenges on [TryHackMe](https://tryhackme.com/) to apply basic cybersecurity concepts.
## 2. Networking Fundamentals
- **Goal**: Gain a solid understanding of networking principles, protocols, and devices, which are crucial for both SOC and DFIR roles.
- **Resources**:
    - **Free**:
        - [Networking Basics - Cisco Networking Academy](https://www.netacad.com/courses/networking/networking-basics) (Free with Registration)
    - **Paid**:
        - [CompTIA Network+ (N10-008) Certification](https://www.comptia.org/certifications/network) (Paid) - Covers networking concepts, troubleshooting, and security.
- **Practice**:
    - Use [Wireshark](https://www.wireshark.org/) to capture and analyze network traffic. Practice analyzing sample PCAP files from online repositories.
    - **Beginner** lab for pcap analysis: [Let's Defend](https://app.letsdefend.io/challenge/pcap-analysis)
## 3. Operating Systems: Windows and Linux
- **Goal**: Understand the basics of Windows and Linux operating systems, including file systems, processes, and user management.
- **Resources**:
    - **Free**:
        - [Windows Fundamentals Module - TryHackMe](https://tryhackme.com/) (Free and Paid Rooms)
        - [Linux Command Line Basics - Coursera](https://www.coursera.org/learn/linux-command-line) (Free with Registration)
        - [CompTIA LX0-101 Linux+ and LPIC-1 Training](https://www.professormesser.com/linux-plus/linux-training-videos/) (Free)
    - **Paid**:
        - [Linux Foundation Certified IT Associate (LFCA)](https://training.linuxfoundation.org/certification/lfca/) (Paid) - Comprehensive Linux certification.
        - [CompTIA Linux+](https://www.comptia.org/certifications/linux) (Paid) 
- **Practice**:
    - Set up virtual machines using VirtualBox or VMware for Windows and Linux environments.
    - Complete tasks on [TryHackMe](https://tryhackme.com/) and [Hack The Box](https://www.hackthebox.com/) to practice navigating and managing these operating systems.
## 4. Basic Security Operations
- **Goal**: Learn the basic functions of a SOC, including monitoring, detection, and incident response.
- **Resources**:
    - **Free**:
        - [Introduction to Security Operations Center (SOC) - Cybrary](https://www.cybrary.it/course/introduction-to-security-operations-center/) (Free with Registration)
    - **Paid**:
        - [SOC Analyst Level 1 - Udemy](https://www.udemy.com/course/soc-analyst-level-1/) (Paid) - Introduction to SOC operations and tools.
- **Practice**:
    - Participate in SOC-related challenges on [Blue Team Labs Online](https://blueteamlabs.online/) (Free and Paid Labs).
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# Beginner Level: SOC Roadmap
As a SOC analyst, you never know what challenges each day will bring—that's the exciting part of our job. But with the thrill comes risk. Staying up-to-date is crucial, which is why you should start by learning defense in depth, common attack techniques, widely used operating systems, threat identification, and incident handling. If you're up for it, dive into malware analysis too. And always remember: to defeat attackers, you need to think like them.
## Defense in Depth & Attacks
- **Goal**: Learn about layered security strategies and understand how different attack vectors are used to compromise systems. Study defense-in-depth tactics that combine multiple security layers to protect against various threats.
- **Resources**:
    - **Free**:
        - [Infosec Institute: Defense in Depth](https://resources.infosecinstitute.com/topic/defense-in-depth/) (Free articles)
    - **Paid**:
        - SANS SEC401.2: Defense In Depth (Paid) - A comprehensive module part of the SANS SEC401 course, focusing on layered security approaches.
- **Practice**:
    - Analyze case studies of layered security defenses using real-world scenarios.
    - Practice simulated attacks and defenses on Let's Defend.
## Windows Fundamentals
- **Goal**: Understand the basics of Windows operating systems, including their structure, security features, and common vulnerabilities. This knowledge is critical for identifying and mitigating threats within a Windows environment.
- **Resources**:
    - **Free**:
        - [Windows Fundamentals Module - TryHackMe](https://tryhackme.com/) (Free and Paid Rooms)
        - [Microsoft Learn: Windows Security](https://learn.microsoft.com/en-us/training/paths/learn-windows-security/) (Free)
    - **Paid**:
        - [Pluralsight: Windows Server Security](https://www.pluralsight.com/courses/windows-server-security) - Comprehensive course on Windows security best practices.
- **Practice**:
    - Explore free rooms on Active Directory on TryHackMe.
    - Use [Let's Defend](https://letsdefend.io/) (Free and Paid) to simulate SOC environments and handle incidents involving Windows security.
## Threat Management & Threat Investigation
- **Goal**:
  -  Understand the fundamentals of threat management, including threat detection, response, and mitigation. Develop the skills needed to manage security incidents effectively.
  -  Master techniques for conducting effective threat investigations, including identifying, containing, and eradicating threats.
- **Resources**:
    - **Free**:
        - [Threat Hunting with Splunk](https://www.splunk.com/en_us/form/free-online-splunk-education.html) (Free with Registration)
        - [YouTube Threat Hunting Playlist](https://www.youtube.com/playlist?list=PLdUDP-atVHBoDae43tcUZnW1YsjoPJRvP) (Arabic)
        - [IBM: Introduction to Cybersecurity Tools & Cyber Attacks](https://www.coursera.org/learn/ibm-cyber-security-tools) (Free on Coursera)
        - [MITRE](https://attack.mitre.org/)
    - **Paid**:
        - SANS SEC401.3: Threat Management (Paid) - This module covers the principles of threat management and how to implement a SOC effectively.
        - Mostafa Yahia’s Book - "Effective Threat Investigation for SOC Analysts" (Paid)
- **Practice**:
    - Implement a threat management process in a virtual or simulated environment.
    - Complete threat detection and management tasks on [CyberDefenders](https://cyberdefenders.org/) (Free and Paid).
    - Solve labs focused on threat investigation techniques on Let's Defend.
## Incident Handling Process
- **Goal**: Learn the incident handling process used by SOC analysts to respond to security incidents, from detection to remediation.
- **Resources**:
    - **Free**:
        - [Cyber Security Incident Handling and Response - Cybrary](https://www.cybrary.it/course/cyber-security-incident-handling-and-response/) (Free with Registration)
    - **Paid**:
        - SANS SEC504.1: Incident Handling Process (Paid) - Focuses on the incident response lifecycle and effective handling techniques.
- **Practice**:
    - Create and refine incident response playbooks for various attack scenarios.
    - Use Let's Defend to participate in real-time incident handling simulations.
## Malware Analysis Fundamentals
- **Goal**: Learn the fundamentals of malware analysis, including static and dynamic analysis techniques.
- **Resources**:
    - **Free**:
        - [Practical Malware Analysis & Triage - Triage Skills](https://www.open.edu/openlearn/digital-computing/practical-malware-analysis-triage/content-section-overview?active-tab=description-tab) (Free)
        - [Mahara-Tech Malware Analysis Course](https://maharatech.gov.eg/course/view.php?id=1404) - A comprehensive course covering various aspects of malware analysis. (Arabic)
- **Practice**:
    - Analyze malware samples using sandbox environments on Let's Defend.
## Hacker Tools and Techniques
- **Goal**: Learn about various hacker tools and techniques used in cyberattacks. Understand how these tools are used to exploit vulnerabilities.
- **Resources**:
    - **Free**:
        - [OWASP Top Ten](https://owasp.org/www-project-top-ten/) (Free)
        - [Hack Tricks](https://book.hacktricks.xyz/) (Free)
    - **Paid**:
        - SANS SEC504.2-5: Hacker Tools and Techniques (Paid) - In-depth exploration of hacker tools, techniques, and countermeasures.
- **Practice**:
    - Use simulated environments to practice using hacker tools on CyberDefenders.
# Your SOC Path
- **Goal**: Develop the necessary skills for a SOC analyst, focusing on basic network monitoring, log analysis, and incident response.
- **Resources**:
    - **Free**:
        - [SOC Level 1 Path - TryHackMe](https://tryhackme.com/path/outline/soclevel1) (Free and Paid Rooms)
        - [SOC Level 2 Path - TryHackMe](https://tryhackme.com/path/outline/soclevel2) (Free and Paid Rooms)
        - [Blue Team Labs Online](https://blueteamlabs.online/) (Free and Paid Labs)
        - [let's Defend](https://www.letsdefend.io/) (Free and Paid Labs)
- **Paid**:
    - [CompTIA CySA+ (Cybersecurity Analyst) Certification](https://www.comptia.org/certifications/cybersecurity-analyst) (Paid) - Covers fundamental skills for a cybersecurity analyst.
- **Practice**:
    - Participate in SOC-related challenges on TryHackMe, Blue Team Labs and Let's Defend Online.
    - Engage in practical SOC tasks on CyberDefenders and Let's Defend.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# Intermediate Level: DFIR Roadmap
If you're set to dive into digital forensics and incident response (DFIR), you've found your destination. Get ready to delve into the advanced sections and elevate your expertise in this critical field. But for the sake of avoiding redundancy, don’t skip the SOC section—make sure to cover it before jumping ahead.
## DFIR Fundamentals
- **Goal**: Understand the basics of Digital Forensics and Incident Response, including essential tools and techniques for acquiring and analyzing digital evidence.
- **Resources**:
    - **Free**:
        - [Intro to Digital Forensics - Coursera](https://www.coursera.org/learn/intro-to-digital-forensics) (Free with Registration)
        - [NetRiders eCIR Prep](https://netriders.academy/courses/incident-response/) - eLearnSecurity Certified Incident Responder (eCIR) by Ahmed Sultan
        - Read some blogs like:
            - [Before Forensics](https://a1l4m.medium.com/before-forensics-0e51a2224714)
            - [Introduction to DFIR](https://a1l4m.medium.com/introduction-to-dfir-290d77c60965)
    - **Paid**:
        - [CHFI](https://www.eccouncil.org/train-certify/computer-hacking-forensic-investigator-chfi/)
        - [eCDFP](https://ine.com/learning/certifications/external/elearnsecurity-certified-digital-forensics-professional)
- **Practice**:
    - Solve beginner challenges on Let's Defend and CyberDefenders to apply foundational DFIR skills.
## Practical Windows Forensics
- **Goal**: Learn in-depth Windows forensics, including the analysis of various Windows artifacts and the reconstruction of user activities.
- **Resources**:
    - **Free**:
        - [Windows Forensics Playlist](https://www.youtube.com/playlist?list=PLlv3b9B16ZacikAtT8NDXpNbGqU8vU4CE&si=9EnB4PbGoB-ftcqL)
    - **Paid**:
        - [TryHackMe - Practical Windows Forensics](https://academy.tcm-sec.com/p/practical-windows-forensics)
        - "Practical Windows Forensics" Book (Paid)
- **Practice**:
    - Analyze Windows artifacts and evidence in scenarios on CyberDefenders.
## Network Security
- **Goal**: Focus on network security principles and how they apply to DFIR, including packet analysis and intrusion detection.
- **Resources**:
    - **Free**:
        - [Wireshark Network Analysis](https://www.wireshark.org/docs/wsug_html_chunked/) (Free)
- **Practice**:
    - Solve network forensics and intrusion detection labs on CyberDefenders.
## Practical Labs & Challenges
- **Goal**: Apply DFIR knowledge in practical scenarios to gain hands-on experience with common forensic tools and techniques.
- **Resources**:
    - **Free & Paid**:
        - [Blue Team Labs Online](https://blueteamlabs.online/) (Free and Paid Labs)
        - [CyberDefenders Labs](https://cyberdefenders.org/) (Paid) - Offers realistic DFIR labs and challenges.
        - [Hack The Box | Sherlocks](https://app.hackthebox.com/sherlocks)
        - [MMOX Labs](https://mmox.me/mylabs)
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# Advanced DFIR Challenges
- **Goal**: Deepen DFIR skills with advanced challenges that cover complex scenarios such as advanced persistent threats (APTs) and ransomware attacks.
- **Resources**:
    - **Paid**:
        - [SANS FOR500: Windows Forensic Analysis](https://www.sans.org/cyber-security-courses/windows-forensic-analysis/) (Paid) - Comprehensive introduction to Windows forensics.
        - [SANS FOR508: Advanced Digital Forensics, Incident Response, and Threat Hunting](https://www.sans.org/cyber-security-courses/advanced-digital-forensics-incident-response-and-threat-hunting/) (Paid)
- **Practice**:
    - Complete advanced DFIR challenges on CyberDefenders and Let's Defend.
## Practical Memory Forensics
- **Goal**: Master memory forensics techniques to analyze volatile data and uncover hidden threats and processes.
- **Resources**:
    - **Free**:
        - [Volatility Framework](https://volatilityfoundation.org/) (Free Tool)
        - [MemLabs](https://github.com/stuxnet999/MemLabs) (Free Challenges)
        - [Memlabs Writeups](https://mmox.me/tags/memlabs/)
    - **Paid**:
        - "Practical Memory Forensics" Book (Paid)
        - "The Art Of Memory Forensics" Book (Paid)
- **Practice**:
    - Analyze memory dumps for malware and other malicious activities on Let's Defend.
## Real Cases Analysis
- **Goal**: Analyze real-life DFIR cases to understand how digital evidence is used in investigations and legal proceedings.
- **Resources**:
    - **Free**:
        - [Case Studies on Forensics Wiki](https://forensicswiki.org/wiki/Case_Studies) (Free)
        - Ali Hadi’s Real Cases - Detailed analysis of real-world DFIR cases.
- **Practice**:
    - Apply learned skills to analyze provided case studies on CyberDefenders - Let’s Defend - BTLO.
## Additional Resources & Continuous Learning
- **Free SOC Courses & Certifications** 
  - [Splunk Courses](https://www.splunk.com/en_us/training/free-courses/overview.html)
  - [Fortinet Courses](https://training.fortinet.com/)
  - [AttackIQ Mitre Att&ck Courses](https://www.academy.attackiq.com/courses/foundations-of-operationalizing-mitre-attck)
  - [Microsoft SC-200 Course](https://learn.microsoft.com/en-us/training/courses/sc-200t00)
  - [Awesome OSINT Courses](https://training.dfirdiva.com/listing-category/osint)
  - [CSILinux Forensic Trainings](https://training.csilinux.com/)
  - [Cybrary Trainings](https://www.cybrary.it/)
  - [DFIR Diva](https://training.dfirdiva.com/)
  - https://training.sleuthkitlabs.com/collections
- **CTF Platforms**:
    - Regularly participate in CTFs on platforms like [TryHackMe](https://tryhackme.com/),[Let's Defend](https://letsdefend.io/) , [Hack The Box](https://www.hackthebox.com/), [Blue Team Labs Online](https://blueteamlabs.online/), and [CyberDefenders](https://cyberdefenders.org/) to keep skills sharp and stay current with new techniques.
    - A List of all labs Created by  MM0X: [MM0X Labs](https://mmox.me/mylabs)
**Note:** This roadmap provides a structured guide for developing skills in both SOC and DFIR roles. Progress through each stage at your own pace and ensure a thorough understanding before moving on to the next.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# Other resources
[1731094859793.pdf](https://github.com/user-attachments/files/18014278/1731094859793.pdf)
- https://www.withsandra.dev/p/here-are-the-best-free-soc-analyst-courses-for-beginners
