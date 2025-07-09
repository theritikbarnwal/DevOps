Here is your finalized `README.md` for GitHub, documenting your **first AWS IAM user setup** with the updated screenshot (`user_ritik.png`).

---

### ✅ Final `README.md` (Markdown file for GitHub)

````markdown
# 🔐 AWS IAM User Creation & Permissions Setup

This repository documents the **first step** of my AWS journey — creating a secure IAM user with the appropriate permissions for AWS CLI and console access.

---

## 📌 Objective

Establish a non-root IAM user for administrative and DevOps tasks, following AWS best practices for security and access control.

---

## 🧾 Summary

- ✅ Created an IAM user: `ritik`
- ✅ Attached necessary permissions via inline and managed policies
- ✅ Configured AWS CLI locally using programmatic access
- ⚠️ MFA not yet enabled (next step for hardening access)

---

## 📁 Steps Performed

### 1. 🔐 Created IAM User

- Username: `ritik`
- Access types:
  - ☑️ Programmatic access (for CLI use)
  - ☑️ AWS Management Console access

---

### 2. 🛡️ Assigned Permissions

IAM user added to group: **`DevOpsAdmin`**  
Attached policies:
- ✅ `AdministratorAccess` (inline policy)
- ✅ `AmazonEC2FullAccess` (AWS managed)
- ✅ `AmazonS3FullAccess` (AWS managed)

> This provides full access to EC2 and S3 services, along with admin capabilities for learning and testing.

---

### 3. ⚙️ AWS CLI Setup

Configured AWS CLI using:

```bash
aws configure
````

Then verified:

```bash
aws sts get-caller-identity
aws iam list-users
```

---

### 🖼️ Screenshot

Below is the screenshot from the IAM console showing the user configuration and permission setup:

![IAM user setup](user_ritik.png)

---

## 📌 Next Steps

* 🔒 Enable Multi-Factor Authentication (MFA)
* ✅ Explore IAM Groups and Role-based access
* 🔄 Practice attaching least-privilege policies
* 🚀 Start using services like S3, EC2, and IAM automation

---

## 🔗 References

* [AWS IAM Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
* [AWS CLI Official Guide](https://docs.aws.amazon.com/cli/latest/userguide/)
* [Security Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

---

## 🛠️ Author

**Ritik Barnwal**
Aspiring DevOps & Cloud Engineer
[GitHub: @theritikbarnwal](https://github.com/theritikbarnwal)

```

---

### 🧱 Repo Structure Suggestion:

```

aws-iam-user-setup/
│
├── README.md
└── user\_ritik.png

```

You can now:
1. Create a new GitHub repo.
2. Upload this `README.md` and your `user_ritik.png` file.
3. Push it as your **first documented cloud/DevOps activity**. ✅

Let me know if you want the `git init` + push commands too.
```
