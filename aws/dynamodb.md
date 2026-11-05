# AWS DynamoDB 

## 1. DynamoDB Fundamentals (Questions 1–15)
- Core Concepts
- What is Amazon DynamoDB?
- What type of database is DynamoDB?
- What are the key characteristics of DynamoDB?
- What are the advantages of DynamoDB over traditional relational databases?
- What are some common use cases for DynamoDB?
- What is a DynamoDB table?
- What is an item in DynamoDB?
- What is an attribute?
- What data types are supported by DynamoDB?
- What is the difference between scalar, document, and set data types?
- What are nested attributes in DynamoDB?
- How does DynamoDB achieve high availability?
- How is DynamoDB serverless?
- What AWS services commonly integrate with DynamoDB?
- When would DynamoDB not be the right database choice?
 
## 2. Data Modeling (Questions 16–30)
- Designing Schemas
- Why is data modeling different in DynamoDB compared to relational databases?
- What is access-pattern-based data modeling?
- What is denormalization in DynamoDB?
- Why is normalization generally discouraged?
- What is a single-table design?
- What is a multi-table design?
- When should you use multiple tables?
- What are entity types in DynamoDB?
- How do you model one-to-one relationships?
- How do you model one-to-many relationships?
- How do you model many-to-many relationships?
- What are adjacency lists?
- How do composite keys improve schema design?
- What are sparse indexes?
- What are common DynamoDB data modeling mistakes?

##  3. Primary Keys and Partition Design (Questions 31–45)
- Keys
- What is a primary key?
- What is a partition key?
- What is a sort key?
- What is the difference between a simple primary key and a composite primary key?
- How does DynamoDB partition data?
- How is a partition key selected?
- What makes a good partition key?
- What causes hot partitions?
- How do you prevent hot partitions?
- What is write sharding?
- What is random suffix partitioning?
- What is calculated sharding?
- How do partition keys affect scalability?
- How does the sort key improve querying?
- How do you design partition keys for high-traffic applications?

## 4. CRUD Operations (Questions 46–60)
- Data Access
- What is PutItem?
- What is GetItem?
- What is UpdateItem?
- What is DeleteItem?
- What is BatchWriteItem?
- What is BatchGetItem?
- What are the limitations of batch operations?
- What is the maximum item size?
- What happens if PutItem overwrites an existing item?
- How do Update Expressions work?
- What are Expression Attribute Names?
- What are Expression Attribute Values?
- How do you increment numeric attributes?
- How do you update nested attributes?
- How do you remove an attribute?
## 5. Query, Scan, and Filter Expressions (Questions 61–75)
- Reading Data
- What is the difference between Query and Scan?
- When should Query be preferred?
- Why should Scan be avoided on large tables?
- What is a Filter Expression?
- What is a Key Condition Expression?
- Does FilterExpression reduce read capacity usage?
- What is ProjectionExpression?
- How does pagination work?
- What is LastEvaluatedKey?
- What is ExclusiveStartKey?
- What are begins_with and BETWEEN?
- How do you retrieve items in descending order?
- What is the maximum Query response size?
- How do you optimize Query performance?
- What are common Query performance problems?

## 6. Secondary Indexes (GSI & LSI) (Questions 76–90)
- Indexes
- What is a secondary index?
- What is a Global Secondary Index (GSI)?
- What is a Local Secondary Index (LSI)?
- What are the differences between GSI and LSI?
- When should you choose a GSI?
- When should you choose an LSI?
- How many GSIs can a table have?
- How many LSIs can a table have?
- Can GSIs have different partition keys?
- Can LSIs have different sort keys?
- What is index projection?
- What are KEYS_ONLY projections?
- What are INCLUDE projections?
- What are ALL projections?
- What are common mistakes when designing GSIs?

## 7. Capacity Modes and Auto Scaling (Questions 91–105)
- Performance Capacity
- What are Read Capacity Units (RCUs)?
- What are Write Capacity Units (WCUs)?
- What is Provisioned Capacity mode?
- What is On-Demand Capacity mode?
- When should you use On-Demand mode?
- When should Provisioned mode be preferred?
- How does Auto Scaling work?
- What CloudWatch metrics influence Auto Scaling?
- What happens if capacity is exceeded?
- What is throttling?
- What causes throttling?
- How do you prevent throttling?
- What are burst credits?
- How do adaptive capacity and partition balancing work?
- How do you estimate required RCUs and WCUs?

## 8. Consistency Models (Questions 106–115)
- Read Consistency
- What is eventually consistent read?
- What is strongly consistent read?
- Which consistency model is the default?
- Which operations support strong consistency?
- Can GSIs use strongly consistent reads?
- Why are strongly consistent reads more expensive?
- When should eventually consistent reads be used?
- When is strong consistency required?
- How does consistency affect latency?
- How does consistency affect cost?
## 9. Transactions and Conditional Operations (Questions 116–130)
- Transactions
- What are DynamoDB transactions?
- What operations are included in a transaction?
- What is TransactWriteItems?
- What is TransactGetItems?
- What are conditional writes?
- What is ConditionExpression?
- How do optimistic locking mechanisms work?
- What is a version attribute?
- How do conditional updates prevent race conditions?
- What happens when a transaction fails?
- What are transaction limits?
- How do transactions affect performance?
- When should transactions be avoided?
- How do conditional deletes work?
- What are idempotent writes?
## 10. DynamoDB Streams (Questions 131–140)
- Event Processing
- What are DynamoDB Streams?
- What events can DynamoDB Streams capture?
- What stream view types are available?
- How long are stream records retained?
- How does Lambda integrate with Streams?
- What are common use cases for Streams?
- Can Streams guarantee ordering?
- How do Streams support event sourcing?
- What are stream shards?
- What are limitations of DynamoDB Streams?

## 11. Global Tables (Questions 141–150)
- Multi-Region
- What are Global Tables?
- How do Global Tables replicate data?
- What conflict resolution mechanism is used?
- What are advantages of Global Tables?
- What are disadvantages of Global Tables?
- How do Global Tables improve availability?
- What happens during a regional outage?
- How does latency improve with Global Tables?
- What are cost considerations for Global Tables?
- What are best practices for Global Tables?

## 12. Backup, Restore, and Disaster Recovery (Questions 151–160)
- Data Protection
- What backup options are available?
- What is Point-in-Time Recovery (PITR)?
- How long can PITR retain backups?
- How do on-demand backups work?
- How do you restore a DynamoDB table?
- Can backups be restored to another region?
- Can backups restore individual items?
- What is the difference between backup and export?
- How do you implement disaster recovery with DynamoDB?
- What RPO and RTO considerations exist?

## 13. Security, IAM, and Encryption (Questions 161–170)
- Security
- How does IAM control access to DynamoDB?
- How do resource-based permissions work with DynamoDB?
- How do fine-grained access controls work?
- What is attribute-level access control?
- How do condition keys restrict DynamoDB access?
- How is data encrypted at rest?
- What encryption options are supported?
- How is data encrypted in transit?
- How do customer-managed KMS keys work?
- What are DynamoDB security best practices?
## 14. Monitoring, Logging, and Performance Tuning (Questions 171–180)
- Monitoring
- Which CloudWatch metrics are important for DynamoDB?
- What does ConsumedReadCapacityUnits indicate?
- What does ThrottledRequests indicate?
- How do you identify hot partitions?
- What is Contributor Insights?
- How do you monitor DynamoDB Streams?
- How do CloudTrail logs help with auditing?
- How do you troubleshoot slow queries?
- What tools help analyze DynamoDB performance?
- How do you optimize table performance?

## 15. Cost Optimization (Questions 181–185)
- Cost Management
- How do you reduce DynamoDB costs?
- When should On-Demand mode be avoided?
- How do GSIs affect cost?
- How do scans increase costs?
- What DynamoDB best practices minimize operational expenses?

## 16. Integration with AWS Services (Questions 186–190)
- AWS Integrations
- How does API Gateway integrate with DynamoDB?
- How does AWS Lambda interact with DynamoDB?
- How can EventBridge work with DynamoDB events?
- How do SQS and SNS integrate with DynamoDB-based applications?
- How can Step Functions orchestrate DynamoDB operations?

## 17. Best Practices and Design Patterns (Questions 191–195)
- Design Patterns
- What are the most important DynamoDB design best practices?
- What is the single-table design pattern, and when is it appropriate?
- How do you design DynamoDB for microservices?
- How do caching solutions such as DAX improve DynamoDB performance?
- What anti-patterns should be avoided when designing DynamoDB applications?

## 18. Senior/Architect-Level Questions (Questions 196–198)
- Architecture
- How would you design a DynamoDB data model for a global-scale e-commerce platform handling millions of requests per second while maintaining low latency and cost efficiency?
- What architectural considerations are essential when using DynamoDB in a multi-account, multi-region enterprise environment with strict governance, compliance, and high availability requirements?
- How would you optimize a DynamoDB deployment supporting unpredictable workloads, complex access patterns, and stringent performance SLAs while minimizing operational overhead and total cost of ownership?

## 19. Scenario-Based and Troubleshooting Questions (Questions 199–200)
- Real-World Scenarios
- Your production application experiences frequent throttling during peak traffic despite using Provisioned Capacity with Auto Scaling. How would you identify the root cause, determine whether hot partitions, capacity limits, or inefficient access patterns are responsible, and implement a long-term solution?
- You are migrating a large, mission-critical relational application to DynamoDB. Describe how you would redesign the schema around access patterns, select partition and sort keys, plan data migration with minimal downtime, implement security and IAM controls, validate performance under production workloads, enable monitoring and backups, and ensure a successful cutover with rollback capabilities.
