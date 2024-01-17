ansible for [hbo ict basis ict platformen](https://canvas.hu.nl/courses/39838/assignments/291089?module_item_id=1035603)

running:
`op read 'op://Private/ansible_vault_canopy/credential' | ansible-playbook --vault-password-file /dev/stdin -i inventory main.yml`