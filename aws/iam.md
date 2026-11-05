- AWS IAM Interview Questions (100 Total)
- Organized by Category and Topic (Beginner → Intermediate → Advanced → Scenario-Based)

## Section 1: IAM Fundamentals (Questions 1–10)
- Core Concepts
- What is AWS IAM, and why is it important?
- What are the key components of IAM?
- What is the difference between authentication and authorization in AWS?
- What is the AWS account root user, and why should it rarely be used?
- What are IAM users?
- What are IAM groups, and why are they useful?
- What is an IAM role?
- How is an IAM role different from an IAM user?
- What is an IAM policy?
- What types of IAM policies are available in AWS?
 
## Section 2: IAM Users, Groups, Roles & Policies (Questions 11–20)
- Identity Management
- What are managed policies?
- What is the difference between AWS-managed and customer-managed policies?
- What are inline policies, and when would you use them?
- How do you attach policies to users, groups, and roles?
- Can a user belong to multiple IAM groups?
- How do IAM groups simplify permission management?
- What happens if multiple policies are attached to a user?
- Can an IAM role have long-term credentials?
- How do applications running on EC2 obtain AWS credentials?
- What are service-linked roles?

## Section 3: IAM Policy Language (Questions 21–30)
- JSON Policy Structure
- What are the main elements of an IAM policy document?
- What is the purpose of the Version element?
- What does the Effect field do?
- What is the difference between Action and NotAction?
- What is the Resource element used for?
- What is the Principal element?
- What are IAM policy Conditions?
- What is the difference between Allow and Explicit Deny?
- What happens if no policy explicitly allows an action?
- How does AWS evaluate multiple IAM policies?
 
## Section 4: IAM Security Best Practices (Questions 31–40)
- Security
- Why should MFA be enabled for IAM users?
- What is the difference between virtual MFA and hardware MFA?
- What are access keys?
- Why is it risky to use long-term access keys?
- How do you rotate access keys?
- How do you enforce strong password policies in AWS?
- What is the principle of least privilege?
- How can IAM Access Analyzer improve security?
- How do you identify unused IAM users and roles?
- What AWS services help monitor IAM activity?
 
## Section 5: IAM Policy Evaluation & Permissions (Questions 41–50)
- Intermediate Concepts
- Explain the IAM policy evaluation logic.
- What is an explicit deny?
- What is an implicit deny?
- Which takes precedence: Allow or Deny?
- What are permission boundaries?
- How do permission boundaries differ from IAM policies?
- What are session policies?
- What are resource-based policies?
- What is the difference between identity-based and resource-based policies?
- How does AWS evaluate permissions when multiple policy types exist?
 
## Section 6: IAM Conditions & Advanced Policies (Questions 51–60)
- Conditions & Controls
- What are IAM condition keys?
- What are global condition keys?
- Explain aws:SourceIp.
- Explain aws:MultiFactorAuthPresent.
- Explain aws:PrincipalArn.
- What is aws:RequestedRegion?
- How can you restrict access to specific IP ranges?
- How do you restrict users to specific AWS regions?
- How do tag-based conditions work?
- What is Attribute-Based Access Control (ABAC)?
 
## Section 7: Cross-Account Access & Federation (Questions 61–70)
- Identity Federation
- What is cross-account access?
- How do IAM roles enable cross-account access?
- What is a trust policy?
- What is the AssumeRole API?
- What are temporary security credentials?
- What is AWS STS?
- What is identity federation?
- How does SAML federation work with AWS?
- How does OpenID Connect (OIDC) federation work?
- What is IAM Identity Center (formerly AWS SSO), and when would you use it?
 
## Section 8: AWS Organizations & Enterprise IAM (Questions 71–80)
- Enterprise Security
- What are AWS Organizations?
- What are Organizational Units (OUs)?
- What are Service Control Policies (SCPs)?
- How are SCPs different from IAM policies?
- Can SCPs grant permissions?
- What happens when an SCP explicitly denies an action?
- How do SCPs and IAM policies work together?
- What is delegated administration?
- How do you implement centralized identity management across hundreds of AWS accounts?
- What IAM design considerations are important in a multi-account AWS environment?
 
## Section 9: Governance, Auditing & Optimization (Questions 81–90)
- Governance
- How do you audit IAM activity?
- What information does CloudTrail provide for IAM events?
- How do you identify overly permissive IAM policies?
- What is IAM Access Advisor?
- What is IAM Access Analyzer?
- How do you detect unused permissions?
- How would you implement least privilege across an enterprise?
- What are the common IAM security misconfigurations?
- How do you prepare IAM for compliance frameworks such as PCI DSS or SOC 2?
- How would you review and optimize IAM permissions for a large AWS environment?
 
## Section 10: Scenario-Based & Real Interview Questions (Questions 91–100)
- Real-World Scenarios
- A developer reports "Access Denied" when uploading files to an S3 bucket, even though an IAM policy allows s3:PutObject. How would you troubleshoot the issue?
- An EC2 instance needs to access DynamoDB without storing AWS access keys. How would you design the solution?
- Your company wants developers to manage EC2 instances but prevent them from deleting production resources. How would you implement this using IAM?
- An external vendor requires temporary access to resources in your AWS account. How would you securely grant that access?
- An employee accidentally receives administrator privileges. How would you investigate the issue and prevent similar incidents?
- Your organization has 500 AWS accounts. How would you design centralized identity, access management, and governance for all accounts?
- A security audit finds several IAM users with full administrator permissions and long-term access keys. What remediation steps would you take?
- A user can list S3 buckets but cannot read objects inside a specific bucket. What IAM and resource-based policy checks would you perform?
- Your organization wants to migrate from IAM users to a centralized workforce identity solution. How would you plan and execute the migration using IAM Identity Center?
- Design an enterprise IAM architecture for a global organization that supports least privilege, cross-account access, federation with a corporate identity provider, temporary credentials, auditing, governance, disaster recovery, and compliance. What services, policies, and best practices would you include, and why?
 
