# proxmox-automation

Automations for Proxmox using Terraform and Ansible. Can be used to setup and provision containers and virtual machines. Read [my post](https://vanmieghem.io/automating-proxmox-with-terraform-ansible/) for more information.

### Usage

2. Install `ansible` and `terraform` (on a Mac `brew install ansible terraform`)
4. run `export PM_PASS='your-PVE-password'` and replace the password of with the NORMAL user pass of `terraform-prov@pve`

5. `make configure` if you are prompted with replacing the ssh keys press no
6. `make run`


### Creating a cloud-init VM template

On the pve host:

1. `apt install cloud-init`
2. Create a template VM (in this case Ubuntu 20.04):
```
wget http://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img
export VM_ID="9000"
qm create 9000 --memory 2048 --net0 virtio,bridge=vmbr0 --sockets 1 --cores 2 --vcpu 2  -hotplug network,disk,cpu,memory --agent 1 --name cloud-init-focal --ostype l26
qm importdisk $VM_ID focal-server-cloudimg-amd64.img local
qm set $VM_ID --scsihw virtio-scsi-pci --virtio0 local:vm-$VM_ID-disk-0
qm set $VM_ID --ide2 local:cloudinit
qm set $VM_ID --boot c --bootdisk virtio0
qm set $VM_ID --serial0 socket
qm template $VM_ID
rm focal-server-cloudimg-amd64.img
```

