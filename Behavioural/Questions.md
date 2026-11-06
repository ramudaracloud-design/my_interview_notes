## Question 1: Assume you are the Administrator of application. What measures will you take to ensure the application runs successfully?

## Question 2:  How do you assess a junior developer's technical skills and performance when they rely on AI tools for coding?



----

# Answers:


**"Assume you are the Administrator of a application. What measures will you take to ensure the application runs successfully?"**


1. Key areas I would monitor and manage

I would divide my responsibilities into 10 important areas.

## 1. Application availability
- Monitor whether app services are up and running.
- Monitor application health checks.
- Check login, and other services (creation, updation , deletion).
- Maintain uptime and availability SLAs.
## 2. Performance monitoring
- Monitor CPU, memory and network utilization.
- Monitor application response time.
- Check latency, packet loss and jitter.
- Identify performance bottlenecks.
## 3. Security management
- Enforce MFA.
- Implement role-based access control (RBAC).
- Manage user permissions.
- Enable encryption and secure communication.
- Review audit logs.
- Prevent unauthorized meeting access.
## 4. User management
- Create and deactivate user accounts.
- Assign appropriate licenses.
- Manage admin and host privileges.
- Handle user onboarding and offboarding.
- Monitor license utilization.
## 5. Backup and disaster recovery
- Define backup policies for relevant configurations and business data.
- Maintain disaster recovery procedures.
- Define RPO and RTO.
- Test recovery procedures periodically.
## 6. Log management
- Monitor application and authentication logs.
- Analyze error logs.
- Identify failed login attempts.
- Integrate logs with centralized monitoring tools.
## 7. Alerting and incident management
- Configure alerts for service outages.
- Monitor unusual traffic and performance degradation.
- Define incident escalation procedures.
- Perform root cause analysis (RCA).
## 8. Patch and upgrade management
- Keep applications and infrastructure updated.
- Apply security patches.
- Test updates before production deployment.
- Maintain rollback plans.
## 9. Network management
- Monitor bandwidth utilization.
- Check firewall rules and connectivity.
- Monitor DNS resolution.
- Check UDP/TCP connectivity and latency.
- Ensure sufficient network capacity for meetings.
## 10. Compliance and governance
- Review audit trails.
- Apply data retention policies.
- Restrict recording and sharing permissions where necessary.
- Follow organizational security and compliance policies.

---

# 2. Tools I would use as an Administrator
If your app is deployed or integrated into an AWS environment, these tools would be useful:
|Area|Tools|
|-----|------|
|Infrastructure monitoring|AWS CloudWatch|
|Log management|ELK / Splunk|
|Infrastructure automation|Terraform|
|Configuration management|Ansible|
|CI/CD|Jenkins / GitHub Actions|
|Container monitoring|Prometheus / Grafana|
|Security|AWS WAF, IAM, MFA|
|Incident management|ServiceNow / Jira |
|Network monitoring|Wireshark, CloudWatch |

---

# 3. Real-time production incident scenario
The interviewer may ask:

"Suppose users complain that application not working. What will you do?"

You can explain your troubleshooting process:
-**Identify the issue**: Check whether the issue affects one user, multiple users, or all users.
-**Check service availability**: Check the official app service status page and any ongoing incidents.
-**Check network connectivity**: Verify DNS, firewall rules, bandwidth, latency and packet loss.
-**Check authentication**: Verify SSO, MFA, user permissions and account status.
-**Analyze logs**: Review available logs and error messages to identify the root cause.
-**Implement corrective action**: Apply the appropriate fix, such as correcting firewall rules or resolving an authentication issue.
-**Validate and communicate**:  check health status, confirm recovery and update affected users.

--- 
# Question 2:  How do you assess a junior developer's technical skills and performance when they rely on AI tools for coding?
# 1. How I measure my junior developers' performance

I would use these 8 parameters.

|Parameter|What I evaluate|
|Technical knowledge|Understanding of Python, APIs, databases, AWS, etc.|
|Problem-solving|Ability to understand and solve real-world problems|
|Code quality|Clean, reusable, readable and maintainable code|
|AI utilization|How effectively they use AI and validate its output|
|Debugging skills|Ability to identify and resolve issues independently|
|Ownership|Responsibility for assigned tasks from development to deployment|
|Team collaboration|Communication, code reviews and knowledge sharing|
|Delivery|Meeting deadlines without compromising quality|

# 2. How do I evaluate developers when everyone uses AI?

I would follow these practices:
## 1. Don't evaluate based on code generation
- Just because someone generates 500 lines of code using ChatGPT doesn't mean they are a good developer.
- I would check whether they understand every important part of the generated code.
## 2. Conduct code review sessions
- I would ask developers to explain:
- Why did you choose this approach?
- Why did you use this particular function?
- What happens if the API fails?
- How are exceptions handled?
- Is the code optimized?
- What are the security risks?
## 3. Give real-world problem-solving tasks
- For example:
- Develop a Python REST API.
- Connect the API to a database.
- Implement authentication.
- Handle exceptions.
- Write unit test cases.
- Debug an existing application.
- I would evaluate their approach, not just the final output.
## 4. Test their debugging capabilities
- Sometimes I would intentionally provide a piece of code containing bugs and ask them to identify and fix the issues.
- This helps me understand whether they have genuine technical knowledge.
## 5. Evaluate AI usage
- I would encourage AI tools but expect developers to:
- Validate AI-generated code.
- Identify incorrect or insecure suggestions.
- Understand the generated logic.
- Avoid sharing confidential company code or sensitive data with unauthorized AI tools.
- Take responsibility for the final implementation.
