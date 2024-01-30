variable "proxmox_host" {
	type = map
     default = {
       pm_api_url = "https://hetzner.imaretarded.dev:8006/api2/json"
       pm_user = "terraform-prov@pve"
       target_node = "hetzner"
     }
}

variable "vmid" {
	default     = 400
	description = "Starting ID for the CTs"
}


variable "hostnames" {
  description = "VMs to be created"
  type        = list(string)
  default     = ["prod-vm", "staging-vm", "dev-vm"]
}

variable "rootfs_size" {
	default = "2G"
}

variable "ips" {
    description = "IPs of the VMs, respective to the hostname order"
    type        = list(string)
	default     = ["10.10.10.10", "10.10.10.11", "10.10.10.12"]
}

variable "ssh_keys" {
	type = map
     default = {
       pub  = "../.ssh/id_rsa.pub"
       priv = "../.ssh/id_rsa"
     }
}

# variable "ssh_password" {}

variable "user" {
	default     = "notroot"
	description = "User used to SSH into the machine and provision it"
}