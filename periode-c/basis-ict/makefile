# terraform variables
TF_DIRS=${shell find . -name "*.tf" -exec dirname {} \; | sort --unique}
COMPONENTS=${shell for d in $(DIRS); do basename $$d; done}

# ansible variables
ANSIBLE_DIR=./ansible
ANSIBLE_VAULT_PASS=$(shell op read 'op://Private/ansible_vault_canopy/credential')


configure: set_up_pub_keys set_up_tf set_up_keys
run: run_tf run_ansible

# setup the public keys for the servers to use. we use github because all mine keys are here
set_up_pub_keys:
ifeq (,test -f $(ANSIBLE_DIR)/files/authorized_keys)
	@echo downloading pub keys and saving them
<<<<<<< Updated upstream
	@curl https://github.com/cvanh.keys > $(ANSIBLE_DIR)/files/authorized_keys --silent
endif
=======
	@curl https://github.com/cvanh.keys > ansible/files/authorized_keys --silent
>>>>>>> Stashed changes

# generate pub and private key if they do not exist already
set_up_keys: 
ifeq (,test -f ./.ssh/id_rsa*)
	mkdir -p .ssh
	ssh-keygen -t rsa -b 4096 -f .ssh/id_rsa -N ''
endif
	
# setup terraform. assuming tf is already installed
set_up_tf:
	@for c in $(COMPONENTS); do \
		cd $(c) && terraform init || exit 1; \
	done
	

run_ansible:
	@echo $(ANSIBLE_VAULT_PASS) | ansible-playbook --vault-password-file /dev/stdin -i inventory main.yml

run_tf:
	@for c in $(TF_DIRS); do 
	(
		terraform plan chdir="$c" -out plan 
		terraform apply chdir="$c" 
	)
	done



.PHONY: run_tf, run_ansible, set_up_tf, set_up_keys, set_up_pub_keys 
