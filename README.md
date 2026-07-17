
# AWS DynamoDB CLI Project

This project demonstrates how to perform basic Amazon DynamoDB operations using the AWS Command Line Interface (AWS CLI).

## Prerequisites

- AWS Account
- IAM User with DynamoDB permissions
- AWS CLI Version 2 installed
- AWS CLI configured

### Configure AWS CLI

```bash
aws configure
```

Enter:

- AWS Access Key ID
- AWS Secret Access Key
- Default Region: `us-east-1`
- Output Format: `json`

---

## Verify AWS Configuration

### Check configured region

```bash
aws configure get region
```

### Verify AWS Identity

```bash
aws sts get-caller-identity
```

---

## Create a DynamoDB Table

```bash
aws dynamodb create-table \
--table-name Student \
--attribute-definitions AttributeName=StudentID,AttributeType=S \
--key-schema AttributeName=StudentID,KeyType=HASH \
--billing-mode PAY_PER_REQUEST
```

---
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/e8ff3800-973b-4cb2-813c-d078994d9e5d" />


## List Available Tables

```bash
aws dynamodb list-tables
```

---

## Describe the Table

```bash
aws dynamodb describe-table \
--table-name Student
```

---

## Insert an Item

```bash
aws dynamodb put-item \
--table-name Student \
--item '{
    "StudentID":{"S":"STU001"},
    "Name":{"S":"Rahul Sharma"},
    "City":{"S":"Pune"}
}'
```

---

## Insert Another Item

```bash
aws dynamodb put-item \
--table-name Student \
--item '{
    "StudentID":{"S":"STU002"},
    "Name":{"S":"Priya Singh"},
    "City":{"S":"Mumbai"}
}'
```

---

## Insert Third Item

```bash
aws dynamodb put-item \
--table-name Student \
--item '{
    "StudentID":{"S":"STU003"},
    "Name":{"S":"Ram Kapoor"},
    "City":{"S":"Nagaj"}
}'
```

---

## Retrieve All Items

```bash
aws dynamodb scan \
--table-name Student
```

---

## Retrieve a Single Item

```bash
aws dynamodb get-item \
--table-name Student \
--key '{"StudentID":{"S":"STU001"}}'
```

---

<img width="926" height="412" alt="image" src="https://github.com/user-attachments/assets/6ff9cd87-345f-43ab-a8db-a1f7e4dab259" />

## Update an Item

```bash
aws dynamodb update-item \
--table-name Student \
--key '{"StudentID":{"S":"STU001"}}' \
--update-expression "SET City = :city" \
--expression-attribute-values '{":city":{"S":"Nepal"}}'
```

---
<img width="938" height="396" alt="image" src="https://github.com/user-attachments/assets/c8176d35-145e-4382-888e-b48753899ea0" />


## Delete an Item

```bash
aws dynamodb delete-item \
--table-name Student \
--key '{"StudentID":{"S":"STU003"}}'
```

---

## Delete the Table

```bash
aws dynamodb delete-table \
--table-name Student
```

---

## Verify Table Deletion

```bash
aws dynamodb list-tables
```

---

## Useful Commands

### Display AWS CLI Version

```bash
aws --version
```

### Display AWS Configuration

```bash
aws configure list
```

### Display Current IAM Identity

```bash
aws sts get-caller-identity
```

---

## Technologies Used

- Amazon DynamoDB
- AWS CLI
- IAM
- Linux (Ubuntu/WSL)
- Git
- GitHub

---

## Learning Outcomes

- Configure AWS CLI
- Create a DynamoDB table
- Insert records
- Retrieve records
- Update records
- Delete records
- Delete a table
- Manage DynamoDB using AWS CLI
````

After creating or updating `README.md`, push it with:

```bash
git add README.md
git commit -m "Add DynamoDB CLI documentation"
git push origin main
```

This format is clean, professional, and suitable for a GitHub portfolio or resume project.
# dynamodb
