# 🚀 Serverless AI Image Recognition Pipeline
A production-grade cloud pipeline that uses **AWS Lambda** and **Amazon Rekognition** to automatically identify objects in uploaded images.

## 🏗️ The Architecture
* **Storage:** Amazon S3 (Input Bucket)
* **Compute:** AWS Lambda (Python 3.9)
* **AI Engine:** Amazon Rekognition (Deep Learning)
* **Monitoring:** Amazon CloudWatch Logs

## 🛠️ Skills Demonstrated
* **Infrastructure as Code:** Managed AWS resources via **AWS CLI**.
* **Linux Mastery:** Developed using **Ubuntu (WSL)**.
* **Security:** Configured **IAM Policies** and **Execution Roles**.
* **Troubleshooting:** Resolved Permission and Event-trigger issues.

## 📸 Results
When an image is uploaded (e.g., a Chihuahua), the system automatically triggers and outputs:
- **Dog:** 98.96%
- **Chihuahua:** 98.91%
- **Puppy:** 97.25%
