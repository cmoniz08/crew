# Generated by Django 5.0.3 on 2024-03-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruthSocial',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('assignee', models.CharField(max_length=3)),
                ('viewed', models.CharField(max_length=3)),
                ('created_at', models.DateTimeField()),
                ('username', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
                ('card', models.CharField(max_length=350)),
                ('media_attachments_type', models.CharField(max_length=20)),
                ('media_attachments_url', models.CharField(max_length=150)),
                ('highlight', models.CharField(max_length=1)),
                ('ElectionConspiracies', models.CharField(max_length=1)),
                ('ElectionCorruption', models.CharField(max_length=1)),
                ('Fedsurrection', models.CharField(max_length=1)),
                ('ConstitutionThreat', models.CharField(max_length=1)),
                ('PraisingDictators', models.CharField(max_length=1)),
                ('AttackingMedia', models.CharField(max_length=1)),
                ('Violence', models.CharField(max_length=1)),
                ('VulnerableCommunities', models.CharField(max_length=1)),
                ('ExistentialThreat', models.CharField(max_length=1)),
                ('PoliticizingInstitutions', models.CharField(max_length=1)),
                ('WeaponizingInstitutions', models.CharField(max_length=1)),
                ('PressuringCourts', models.CharField(max_length=1)),
                ('WeaponizingMilitary', models.CharField(max_length=1)),
                ('AbusingPower', models.CharField(max_length=1)),
                ('StayinOffice', models.CharField(max_length=1)),
                ('TargetingOpponents', models.CharField(max_length=1)),
                ('Factchecked', models.CharField(max_length=2)),
                ('Mark', models.CharField(max_length=1)),
                ('mentions', models.CharField(max_length=30)),
                ('in_reply_to_id', models.CharField(max_length=4)),
                ('quote_id', models.CharField(max_length=25)),
                ('in_reply_to_account_id', models.CharField(max_length=4)),
                ('visibility', models.CharField(max_length=10)),
                ('tags', models.CharField(max_length=100)),
                ('indexRAW', models.CharField(max_length=10)),
                ('idRAW', models.CharField(max_length=18)),
            ],
        ),
    ]
