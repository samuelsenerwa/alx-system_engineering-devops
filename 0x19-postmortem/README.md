# Postmortem: Web Stack Outage

## Issue Summary:
Duration: June 9, 2023, 6:00 PM - June 10, 2023, 10:00 AM (EAT)
Impact: User authentication service downtime affecting 25% of users
Root Cause: Database connectivity issue due to misconfigured firewall rules

## Timeline:

6:00 PM: The issue was detected when the monitoring system alerted a sudden drop in successful user logins.
Investigation began immediately by the operations team.
Assumption: The issue might be related to a recent deployment of a new authentication module.
Misleading Path: The authentication module was rolled back, but the issue persisted, ruling out the module as the root cause.
7:00 PM: The incident escalated to the engineering team responsible for the user authentication service.
Further investigation revealed potential issues with the database connectivity.
Misleading Path: Initially, the focus was on the database server itself, leading to unnecessary configuration changes and restarts.
10:00 PM: The incident escalated to the database administration team.
12:00 AM: The database administration team identified misconfigured firewall rules that were blocking the application server's access to the database.
1:00 AM: The issue was resolved by updating the firewall rules to allow the required database connections.
2:00 AM: User authentication service was fully restored, and successful logins returned to normal levels.

## Root Cause and Resolution:
The root cause of the web stack outage was determined to be misconfigured firewall rules, which prevented the application server from establishing a connection with the database. The rules were inadvertently modified during a recent security update, causing the interruption in the service. The issue was fixed by updating the firewall rules to allow the necessary database connections. Once the rules were corrected, the user authentication service resumed normal operation.

Corrective and Preventative Measures:
To prevent similar issues in the future, the following measures will be implemented:

Regularly review and validate firewall rules to ensure they align with the required connectivity.
Enhance monitoring and alerting mechanisms to quickly detect and respond to authentication service disruptions.
Implement automated testing and verification for critical system configurations, including firewall rules.
Improve communication and collaboration between teams during incident escalation to streamline troubleshooting efforts.
Tasks to Address the Issue:

Conduct a comprehensive review of firewall rules across the infrastructure and validate their correctness.
Enhance monitoring system alerts to include specific metrics related to user authentication service health.
Implement automated testing scripts to regularly verify database connectivity from the application server.
Schedule regular training sessions to educate teams about incident escalation and effective collaboration during troubleshooting.
Update the incident response plan to include steps for verifying and reviewing system configurations during outages.
By implementing these corrective and preventative measures, we aim to minimize the occurrence of similar web stack outages and improve our incident response capabilities. Our goal is to provide a more reliable and seamless experience for our users while maintaining the integrity of our web services.


