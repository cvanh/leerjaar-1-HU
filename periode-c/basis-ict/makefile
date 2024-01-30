configure: set_up_pub_keys set_up_tf
run: run_tf run_ansible

# setup the public keys for the servers to use. we use github because all mine keys are here
set_up_pub_keys:
	@echo downloading pub keys and saving them
	curl https://github.com/cvanh.keys > ansible/files/authorized_keys --silent

# setup terraform. assuming tf is already installed
set_up_tf:
	cd tf && terraform init

run_ansible:
	op read 'op://Private/ansible_vault_canopy/credential' | ansible-playbook --vault-password-file /dev/stdin -i inventory main.yml

run_tf:
	cd tf && terraform plan -out plan
	cd tf && terraform apply

