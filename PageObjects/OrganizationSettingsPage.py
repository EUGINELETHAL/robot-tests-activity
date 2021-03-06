""" Organization Settings Page Locators

    [TODO] ADD DESC
"""

breadcrumb = '//ul[@class="breadcrumb"]'
hl_bc_org_settings = breadcrumb + '/li/a[./text()="Organization Settings"]'
lbl_bc_profile = breadcrumb + '/li[./text()="Profile"]'
lbl_bc_configurations = breadcrumb + '/li[./text()="Configurations"]'
lbl_bc_people = breadcrumb + '/li[./text()="People"]'
hl_bc_people = breadcrumb + '/li/a[./text()="People"]'
lbl_bc_pending_invite = breadcrumb + '/li[./text()="Pending Invitations"]'
lbl_org_settings_title = '//h4[@class="page-title"][contains(text(),"Organization Settings")]'
hl_tab_profile = '//a[@aria-controls="profile"]'
hl_tab_configurations = '//a[@aria-controls="configurations"]'
hl_tab_people = '//a[@aria-controls="people"]'
hl_tab_usage = '//a[@aria-controls="usage"]'
btn_save = '//button[text()="Save"]'

# Profile Tab
pnl_org_logo = 'div[@for="organizationLogo"]'
tb_org_logo = 'organizationLogo'
tb_org_name = 'name'
tb_org_desc = 'id:description'
btn_org_save = 'updateOrganization'
btn_reset = 'org-logo-reset'
img_profile_org_logo = '//img[@alt="Organization Logo"]'

# Configurations Tab
# Workflow Level Labels
tb_workflowlevel1 = 'workflowlevel1'
# lbl_workflowlevel1 = '//label[@for="workflowlevel1"]'
txt_workflowlevel1 = 'Workflow Level 1:'
tb_workflowlevel2 = 'workflowlevel2'
# lbl_workflowlevel2 = '//label[@for="workflowlevel2"]'
txt_workflowlevel2 = 'Workflow Level 2:'
tb_workflowlevel3 = 'workflowlevel3'
# lbl_workflowlevel3 = '//label[@for="workflowlevel3"]'
txt_workflowlevel3 = 'Workflow Level 3:'
tb_workflowlevel4 = 'workflowlevel4'
# lbl_workflowlevel4 = '//label[@for="workflowlevel4"]'
txt_workflowlevel4 = 'Workflow Level 4:'
# Other Labels
tb_indicator = 'indicator'
tb_site = 'site'
tb_stakeholder = 'stakeholder'
tb_form = 'form'
# Default Settings
tb_default_currency = 'name:"default_currency"'
tb_date_format = 'name:"date_format"'
tb_default_language = 'name:"default_language"'
tb_theme_color = 'name:"theme_color"'

# People Tab
btn_roles = '//button[contains(text(),"Role(s)")]'
hl_role_all = btn_roles + '/..//a[./text()="--All--"]'
hl_role_editor = '//a[./text()="Editor"]'
hl_role_owner = '//a[./text()="Owner"]'
hl_role_viewer = '//a[./text()="Viewer"]'
btn_status = '//button[contains(text(),"Status")]'
hl_status_all = btn_status + '/..//a[./text()="--All--"]'
hl_status_active = '//a[./text()="Active"]'
hl_status_inactive = '//a[./text()="inctive"]'
btn_invite_users = '//div[@class="sub-nav-item"][4]//button'
hl_invite_users = '//a[contains(text(),"Invite Users")]'
hl_pending_invite = '//a[contains(text(),"Pending Invitations")]'
tbl_users = 'userTable'
# Invite People Modal
mdl_invite_user = 'inviteUserModal'
lbl_invite_people_title = 'inviteUserLabel'
txt_invite_people_title = 'Invite people'
icon_close = '//button[@data-dismiss="modal"][@type="button"]'
tb_email_address = 'css:.select2-search__field'
lbi_email_choice = '//li[@class="select2-selection__choice"]'
icon_remove_choice = '/span[@class="select2-selection__choice__remove"]'
dd_invite_org = '//span[@aria-labelledby="select2-id_organization-container"]'
lbl_org_fbh = '//li[contains(text(),"For Better Humans")]'  # User Create Data
btn_close = '//button[@data-dismiss="modal"][@type="reset"]'
btn_invite = 'inviteUser'
# Pending Invitations Page
lbl_pending_invite_title = '//h4[@class="page-title"][contains(text(),"Pending Invitations")]'
btn_organizations = '//button[contains(text(),"Organizations")]'
hl_org_all = btn_organizations + '/..//a[./text()="--All--"]'
hl_org_fbh = '//a[contains(text(),"For Better Humans")]'
tbl_pending_invites = '//table[@id="invitationTable"]'
btn_more = '//button[contains(text(),"More")]'
btn_toggle_dropdown = '//button[@data-toggle="dropdown"]'
hl_resend = '//a[contains(text(),"Resend")]'
hl_revoke = '//a[@href="#deleteItemModal"]'
mdl_confirm_revoke = '//div[contains(@id,"revokeInviteModal")]'
lbl_confirm_revoke_title = '//h4[@class="modal-title"][contains(text(),"Confirm Revoke")]'
lbl_confirm_revoke_msg = mdl_confirm_revoke + '//p'
btn_revoke = '//button[contains(@id,"revokeInvite")]'

# Toast Messages
txt_toast_invite_title = 'Invitation Successful'
# [TODO: Undo "successfuly" typo once fixed]
txt_toast_invite_msg = 'You have successfully invited '
# [TODO: Undo "Succesfully" typo once fixed]
txt_toast_update_title = 'Succesfully Updated'
txt_toast_update_msg = 'Your update has been saved.'
txt_toast_revoke_invite_msg = 'You have successfully revoked the invitation'
txt_toast_resend_invite_msg = 'Invitation was successfully sent'

# Text Messages
txt_org_logo_updated = 'Your organization logo has been updated.'
txt_confirm_revoke_msg = 'Are you sure you want to revoke invation to '
