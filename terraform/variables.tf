variable "location" {
  description = "Azure region"
  type        = string
  default     = "canadacentral"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "contoso-devsecops"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "kubernetes_version" {
  description = "AKS Kubernetes version"
  type        = string
  default     = null
}
