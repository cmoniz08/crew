from django.db import models

class TruthSocial(models.Model):
	id = models.IntegerField(primary_key=True)
	assignee = models.CharField(max_length=3, null=True, blank=True)
	viewed = models.CharField(max_length=3, null=True, blank=True)
	created_at = models.DateTimeField(null=True, blank=True)
	username = models.CharField(max_length=30, null=True, blank=True)
	url	= models.CharField(max_length=100, null=True, blank=True)
	content = models.CharField(max_length=2000, null=True, blank=True)
	card = models.CharField(max_length=350, null=True, blank=True)
	media_attachments_type = models.CharField(max_length=20, null=True, blank=True)
	media_attachments_url = models.CharField(max_length=150, null=True, blank=True)
	highlight = models.CharField(max_length=1, null=True, blank=True)
	ElectionConspiracies = models.CharField(max_length=1, null=True, blank=True)
	ElectionCorruption = models.CharField(max_length=1, null=True, blank=True)
	Fedsurrection = models.CharField(max_length=1, null=True, blank=True)
	ConstitutionThreat = models.CharField(max_length=1, null=True, blank=True)
	PraisingDictators = models.CharField(max_length=1, null=True, blank=True)
	AttackingMedia = models.CharField(max_length=1, null=True, blank=True)
	Violence = models.CharField(max_length=1, null=True, blank=True)
	VulnerableCommunities = models.CharField(max_length=1, null=True, blank=True)
	ExistentialThreat = models.CharField(max_length=1, null=True, blank=True)
	PoliticizingInstitutions = models.CharField(max_length=1, null=True, blank=True)
	WeaponizingInstitutions = models.CharField(max_length=1, null=True, blank=True)
	PressuringCourts = models.CharField(max_length=1, null=True, blank=True)
	WeaponizingMilitary = models.CharField(max_length=1, null=True, blank=True)
	AbusingPower = models.CharField(max_length=1, null=True, blank=True)
	StayinOffice = models.CharField(max_length=1, null=True, blank=True)
	TargetingOpponents = models.CharField(max_length=1, null=True, blank=True)
	Factchecked = models.CharField(max_length=2, null=True, blank=True)
	Mark = models.CharField(max_length=1, null=True, blank=True)
	mentions = models.CharField(max_length=30, null=True, blank=True)
	in_reply_to_id = models.CharField(max_length=4, null=True, blank=True)
	quote_id = models.CharField(max_length=25, null=True, blank=True)
	in_reply_to_account_id = models.CharField(max_length=4, null=True, blank=True)
	visibility = models.CharField(max_length=10, null=True, blank=True)
	tags = models.CharField(max_length=100, null=True, blank=True)
	indexRAW = models.CharField(max_length=10, null=True, blank=True)
	idRAW = models.CharField(max_length=18, null=True, blank=True)

	def __str__(self):
		return self.url

	class Meta():
		db_table = 'Trump_Truth_Social'


