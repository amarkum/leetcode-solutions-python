# Google Cloud Command Reference

## Overview
This document provides a reference for commonly used **Google Cloud (gcloud) commands**, including organization details, project migration, authentication, and project management. These commands help in managing Google Cloud projects and their organizational structure.

---

## 1. View Organization Details
### **List Organizations and their IDs**
```sh
gcloud organizations list
```
Example Output:
```
DISPLAY_NAME      ID              DIRECTORY_CUSTOMER_ID
askthepros.com    123456789012    XXXX
bridlewood.in     519669926361    XXXX
```

---

## 2. Migration: Move Projects to Organizations

### **I. Move `AskTheProsLive` to `askthepros.com`**
```sh
gcloud beta projects move bridlewoodgmb --organization 123456789012
```

### **II. Move `Bridlewood GMB` to `bridlewood.in` (Already correct)**
```sh
gcloud beta projects move shining-bazaar-305605 --organization 519669926361
```

### **III. Move `asktheproslogin` to `askthepros.com`**
```sh
gcloud beta projects move asktheproslogin --organization 123456789012
```

### **Cross-check Migration Status**
```sh
gcloud projects describe innate-marking-445519-j9 --format="value(parent.id)"
```

---

## 3. Google Cloud General Commands

### **Check Currently Authenticated Accounts**
```sh
gcloud auth list
```
Example Output:
```
Credentialed Accounts
ACTIVE  ACCOUNT
        amar.mailsbox@gmail.com
        amarxkumar93@gmail.com
*       growth.arctic@gmail.com
```

To sign into another account:
```sh
gcloud auth login
```

### **Switch to a Specific Account**
```sh
gcloud config set account growth.arctic@gmail.com
```

---

## 4. Project Management Commands

### **Get a List of Projects for the Current Account**
```sh
gcloud projects list
```
Example Output:
```
PROJECT_ID                NAME              PROJECT_NUMBER
innate-marking-445519-j9  My First Project  466191251452
```

### **Set a Specific Project as Active**
```sh
gcloud config set project innate-marking-445519-j9
```

### **Authenticate Application Default Credentials**
```sh
gcloud auth application-default login
```

### **Set Quota Project for Application Default Credentials (ADC)**
```sh
gcloud auth application-default set-quota-project innate-marking-445519-j9
```

### **Describe a Project in Detail**
```sh
gcloud projects describe innate-marking-445519-j9
```
Example Output:
```
createTime: '2024-12-22T19:56:08.863430Z'
lifecycleState: ACTIVE
name: My First Project
projectId: innate-marking-445519-j9
projectNumber: '466191251452'
```

---

## 5. Organization and IAM Policy Management

### **View Organizations Linked to Your Account**
```sh
gcloud organizations list
```

### **Check Current Active Project**
```sh
gcloud config list --format="value(core.project)"
```

### **List All Projects with Parent Organization Info**
```sh
gcloud projects list --format="table(projectId, name, projectNumber, parent.id, parent.type, lifecycleState)"
```

### **View All Projects Under a Specific Organization**
```sh
gcloud projects list --filter="parent.id=<ORG_ID>"
```

### **View IAM Policy for a Project**
```sh
gcloud projects get-iam-policy <PROJECT_ID> --format=json
```

### **List All Projects Available to the Account**
```sh
gcloud projects list
```

---

## 6. Troubleshooting and Useful Checks

### **Check If a Project Has Been Deleted**
```sh
gcloud projects list --filter="lifecycleState=DELETE_REQUESTED"
```

### **Restore a Deleted Project (Within 30 Days)**
```sh
gcloud projects undelete <PROJECT_ID>
```

### **Check What Account is Currently Used**
```sh
gcloud auth list
```

### **Find the Parent Organization of a Project**
```sh
gcloud projects describe <PROJECT_ID> --format="value(parent.id, parent.type)"
```

---

## Summary of Key Checks
| Command | Purpose |
|---------|---------|
| `gcloud config list` | Shows current project |
| `gcloud projects list` | Lists all projects with parent info |
| `gcloud organizations list` | Lists organizations linked to your account |
| `gcloud projects describe <PROJECT_ID>` | Shows parent org/folder of a project |
| `gcloud projects get-iam-policy <PROJECT_ID>` | Checks IAM roles for a project |
| `gcloud organizations get-iam-policy <ORG_ID>` | Checks IAM roles for an org |
| `gcloud projects list --filter="parent.type=organization"` | Lists projects inside an org |
| `gcloud projects list --filter="lifecycleState=DELETE_REQUESTED"` | Checks if a project is deleted |

---

## Notes
- Always verify the **project ID** and **organization ID** before running migration commands.
- Use **IAM policies** to ensure your account has the necessary permissions.
- If facing access issues, try switching accounts using `gcloud auth login`.

---

### 🔹 **Need Help?**
For official documentation, visit: [Google Cloud CLI Documentation](https://cloud.google.com/sdk/docs/)

---

This document serves as a quick reference for Google Cloud command-line operations. 🚀
